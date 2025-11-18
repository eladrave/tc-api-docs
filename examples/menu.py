"""Interactive examples demonstrating the TutorCruncher SDK."""
from __future__ import annotations

import os
import sys
from textwrap import dedent
from typing import Dict, Tuple
from urllib.parse import parse_qsl, urlparse

from tc_api_sdk import (
    AppointmentsAppointmentObject,
    ClientsClientObjectVersion2,
    TutorCruncherClient,
)

MENU: Dict[str, Tuple[str, str]] = {
    '1': ('List the 10 most recently added clients.', 'list_recent_clients'),
    '2': ('Show the next five upcoming appointments.', 'show_upcoming_appointments'),
    '3': ('Demonstrate paginated traversal of prospect clients.', 'paginate_prospects'),
    'q': ('Quit', 'quit_menu'),
}


def list_recent_clients(client: TutorCruncherClient) -> None:
    response = client.clients.list_all_clients(
        params={'limit': 10},
        model=ClientsClientObjectVersion2,
    )
    print(f'Reported total clients: {response.count}')
    for item in response.results:
        print(f'  #{item.id} {item.first_name} {item.last_name} — email={item.email}')


def show_upcoming_appointments(client: TutorCruncherClient) -> None:
    response = client.appointments.list_all_appointments(
        params={'limit': 5, 'status': 'planned'},
        model=AppointmentsAppointmentObject,
    )
    print(f'Reported total appointments: {response.count}')
    for item in response.results:
        contractor_count = len(item.cjas)
        recipient_count = len(item.rcras)
        print(
            f'  #{item.id} "{item.topic}" start={item.start} '
            f'contractors={contractor_count} recipients={recipient_count}'
        )


def paginate_prospects(client: TutorCruncherClient, pages: int = 2, page_size: int = 5) -> None:
    params: Dict[str, str] = {'limit': str(page_size), 'status': 'prospect'}
    for current_page in range(1, pages + 1):
        response = client.clients.list_all_clients(
            params=params,
            model=ClientsClientObjectVersion2,
        )
        print(f'Prospect page {current_page} / reported total {response.count}')
        for item in response.results:
            print(f'  #{item.id} {item.first_name} {item.last_name}')
        if not response.next:
            print('No additional pages available.')
            break
        next_query = dict(parse_qsl(urlparse(response.next).query))
        params = {key: next_query[key] for key in ('limit', 'offset', 'status') if key in next_query}
    else:
        print('Reached the requested page limit.')


def quit_menu(_: TutorCruncherClient) -> None:
    print('Goodbye!')
    raise SystemExit(0)


def main() -> None:
    api_key = os.environ.get('TC_API_KEY')
    if not api_key:
        print(
            dedent(
                '''
                Please set the TC_API_KEY environment variable with a TutorCruncher API token:
                  export TC_API_KEY="token <API KEY>"
                '''
            ).strip()
        )
        sys.exit(1)

    print(
        dedent(
            '''
            TutorCruncher SDK examples
            -------------------------
            Select an option to perform a predefined query.
            '''
        ).strip()
    )

    actions = {key: globals()[fn_name] for key, (_, fn_name) in MENU.items()}
    with TutorCruncherClient(api_key=api_key) as client:
        while True:
            for key, (label, _) in MENU.items():
                print(f'[{key}] {label}')
            choice = input('Choose an option: ').strip().lower()
            action = actions.get(choice)
            if action is None:
                print('Unknown selection, please try again.\n')
                continue
            print()
            action(client)
            print()


if __name__ == '__main__':  # pragma: no cover
    main()
