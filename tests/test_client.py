import json
import unittest

from tc_api_sdk import AgentsAgentObjectVersion2, TutorCruncherClient
from tc_api_sdk.exceptions import TutorCruncherNotFoundError


class FakeResponse:
    def __init__(self, *, status_code=200, json_data=None, reason='OK'):
        self.status_code = status_code
        self._json_data = json_data
        self.reason = reason
        self.headers = {}
        if json_data is None:
            self.content = b''
            self.text = ''
        else:
            self.text = json.dumps(json_data)
            self.content = self.text.encode()

    def json(self):
        if self._json_data is None:
            raise ValueError('No JSON body set.')
        return self._json_data


class FakeSession:
    def __init__(self):
        self.headers = {}
        self.requests = []
        self.next_response = FakeResponse()

    def request(self, **kwargs):
        self.requests.append(kwargs)
        return self.next_response

    def close(self):
        pass


class TutorCruncherClientTests(unittest.TestCase):
    def test_list_agents_returns_paginated_models(self):
        session = FakeSession()
        session.next_response = FakeResponse(
            json_data={
                'count': 1,
                'next': None,
                'previous': None,
                'results': [{'id': 1, 'first_name': 'Billy', 'last_name': 'Holiday'}],
            }
        )
        client = TutorCruncherClient(api_key='test', base_url='https://example.com', session=session)
        result = client.agents.list_all_agents(model=AgentsAgentObjectVersion2)
        self.assertEqual(result.count, 1)
        self.assertEqual(len(result.results), 1)
        self.assertIsInstance(result.results[0], AgentsAgentObjectVersion2)
        request = session.requests[-1]
        self.assertEqual(request['method'], 'GET')
        self.assertEqual(request['url'], 'https://example.com/api/agents/')
        self.assertEqual(request['headers']['Authorization'], 'token test')

    def test_create_agent_sends_payload(self):
        session = FakeSession()
        session.next_response = FakeResponse(json_data={'id': 99})
        client = TutorCruncherClient(api_key='abc', base_url='https://api.test', session=session)
        payload = AgentsAgentObjectVersion2(first_name='Ada', last_name='Lovelace')
        client.agents.create_an_agent(payload=payload)
        request = session.requests[-1]
        self.assertEqual(request['method'], 'POST')
        self.assertEqual(request['url'], 'https://api.test/api/agents/')
        self.assertEqual(request['json']['first_name'], 'Ada')
        self.assertEqual(request['json']['last_name'], 'Lovelace')

    def test_not_found_error_bubbles_up(self):
        session = FakeSession()
        session.next_response = FakeResponse(status_code=404, json_data={'detail': 'Not found'}, reason='Not Found')
        client = TutorCruncherClient(api_key='abc', base_url='https://api.test', session=session)
        with self.assertRaises(TutorCruncherNotFoundError):
            client.agents.get_an_agent(id=1)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
