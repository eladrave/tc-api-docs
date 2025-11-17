from __future__ import annotations

from typing import Any, Dict, Optional


class TutorCruncherAPIError(Exception):
    """Base exception for every TutorCruncher API failure."""

    def __init__(self, response, message: Optional[str] = None) -> None:
        self.response = response
        self.status_code = response.status_code
        self.payload: Any = self._extract_payload()
        detail = self._extract_detail(self.payload)
        if message:
            final_message = message
        elif detail:
            final_message = f'{self.status_code} {response.reason}: {detail}'
        else:
            final_message = f'{self.status_code} {response.reason}'
        super().__init__(final_message)

    def _extract_payload(self) -> Any:
        try:
            return self.response.json()
        except Exception:
            return self.response.text

    @staticmethod
    def _extract_detail(payload: Any) -> Optional[str]:
        if isinstance(payload, dict):
            for key in ('detail', 'message', 'error'):
                if payload.get(key):
                    return str(payload[key])
        return None


class TutorCruncherAuthenticationError(TutorCruncherAPIError):
    """Raised when authentication fails."""


class TutorCruncherNotFoundError(TutorCruncherAPIError):
    """Raised when a requested resource cannot be found."""


class TutorCruncherRateLimitError(TutorCruncherAPIError):
    """Raised when the API rate limit has been exceeded."""


HTTP_ERROR_MAP = {
    401: TutorCruncherAuthenticationError,
    403: TutorCruncherAuthenticationError,
    404: TutorCruncherNotFoundError,
    429: TutorCruncherRateLimitError,
}


def raise_for_status(response) -> None:
    if 200 <= response.status_code < 300:
        return
    exc_class = HTTP_ERROR_MAP.get(response.status_code, TutorCruncherAPIError)
    raise exc_class(response)
