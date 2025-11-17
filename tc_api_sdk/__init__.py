from __future__ import annotations

from ._version import __version__
from .base import APIModel, PaginatedResponse
from .client import DEFAULT_BASE_URL, TutorCruncherClient
from . import models as _models
from .models import *  # noqa: F401,F403

__all__ = ['TutorCruncherClient', 'APIModel', 'PaginatedResponse', 'DEFAULT_BASE_URL', '__version__']
__all__ += list(getattr(_models, '__all__', []))

del _models
