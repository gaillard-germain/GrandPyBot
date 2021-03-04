from grandpybot_app import Seeker
import requests


class MockResponse:
    def __init__(self, result_type):
        """Mocks the Requests response object"""

        if result_type == 'loc':
            self.results = {"candidates": [
                                {"formatted_address": "Paris, France",
                                 "name": "Paris"}],
                            "status": "OK"}
        elif result_type == 'title':
            self.results = {"query": {"search": [{"title": "Paris"}],
                                      "searchinfo": {"totalhits": 1}}}
        elif result_type == 'info':
            self.results = {"query": {"pages": [{"extract": "About Paris"}]}}

    def json(self):
        return self.results


def test_answer(monkeypatch):
    """Tests the dictionnary, which contains google and media wiki
       apis responses, to send to ajax (using mocks)"""

    embed_url = "https://www.google.com/maps/embed/v1/place?q=paris&key="
    loc_results = {"name": "Paris",
                   "address": "Paris, France",
                   "source": embed_url}

    title_result = 'Paris'
    info_result = 'About Paris'
    answer_result = loc_results.copy()
    answer_result['info'] = info_result

    def mock_get_loc(*args, **kwargs):
        return MockResponse('loc')

    def mock_get_title(*args, **kwargs):
        return MockResponse('title')

    def mock_get_info(*args, **kwargs):
        return MockResponse('info')

    monkeypatch.setattr(requests, 'get', mock_get_loc)
    fake_loc = Seeker.get_loc("paris", "")
    assert fake_loc == loc_results
    monkeypatch.setattr(requests, 'get', mock_get_title)
    fake_title = Seeker.get_title("paris")
    assert fake_title == title_result
    monkeypatch.setattr(requests, 'get', mock_get_info)
    fake_info = Seeker.get_info("Paris", "1")
    assert fake_info == info_result
    fake_loc['info'] = fake_info
    assert fake_loc == answer_result
