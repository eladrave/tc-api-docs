# tc-api-docs
Documentation for TutorCruncher's API

## Python SDK

The repository now ships a fully generated Python package (`tc_api_sdk`) that exposes dataclasses for every documented object as well as a high-level client with methods for each endpoint.

### Quick start

```bash
python3 -m pip install -e .
python3 -m unittest discover tests  # optional: run the unit tests
```

```python
from tc_api_sdk import (
    TutorCruncherClient,
    AgentsAgentObjectVersion2,
    ClientsClientObjectVersion2,
    AppointmentsAppointmentObject,
)

# instantiate the reusable HTTP client
client = TutorCruncherClient(api_key="token <API KEY>")

# list endpoints return PaginatedResponse objects when a model is supplied
agents = client.agents.list_all_agents(
    params={"limit": 10},
    model=AgentsAgentObjectVersion2,
)
for item in agents.results:
    print(item.id, item.first_name, item.last_name)

# filtering works through params dicts or the generated filter dataclasses
prospects = client.clients.list_all_clients(
    params={"status": "prospect", "limit": 25},
    model=ClientsClientObjectVersion2,
)

# show how nested dataclasses keep types intact
appointments = client.appointments.list_all_appointments(
    params={"limit": 5},
    model=AppointmentsAppointmentObject,
)
for appt in appointments.results:
    print(appt.id, appt.topic, appt.status, len(appt.cjas))

# Any dataclass can also be used as a payload for POST/PUT endpoints:
new_agent = AgentsAgentObjectVersion2(
    first_name="Ada",
    last_name="Lovelace",
    email="ada@example.com",
)
client.agents.create_an_agent(payload=new_agent)
```

#### More examples

- **Path parameters** – any endpoint whose URL contains `<id>` accepts an `id` keyword argument: `client.agents.get_an_agent(id=123, model=AgentsAgentObjectVersion2)`.
- **Raw access** – pass `raw=True` to receive the underlying `requests.Response` (useful for streaming or inspecting headers).
- **Error handling** – unsuccessful responses raise subclasses of `TutorCruncherAPIError`. Inspect `exc.status_code` or `exc.payload` for details.
- **Custom headers/timeouts** – all resource methods accept `headers={...}` and `timeout=<seconds>` overrides which are forwarded to the underlying request.

For larger scripts consider wrapping the client in a `with` block to ensure the session is properly closed:

```python
with TutorCruncherClient(api_key="token <API KEY>") as client:
    reports = client.reports.list_all_reports(model=ReportsReportsObject)
    ...
```

### Regenerating schema/models

Run `python3 scripts/build_sdk_schema.py` whenever the documentation changes. It refreshes `tc_api_sdk/generated/api_schema.json` and the auto-generated dataclasses in `tc_api_sdk/models.py`.

## Local Installation

1. create virtual environment

2. Install dependencies
```bash
make install
```

3. Run Local
```bash
harrier dev
```

## Editing

The visual content is setup in the api-content.jinja template stype page

The content set by this template is referred to as sections, each section is set out in api.yml

## Deploying

This PR has automatic deploys, after merging a PR, it will be deployed. 

Please create a new tag/release after making changes.
