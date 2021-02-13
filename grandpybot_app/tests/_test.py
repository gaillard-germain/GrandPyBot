from grandpybot_app import get_place_info
import requests



class MockResponse:
    @staticmethod
    def json():
        results = {"candidates": [{"formatted_address": "Paris, France",
                                   "name": "Paris"}]}
        return results

def test_get_place_info(monkeypatch):
    results = {"question": "paris",
               "name": "Paris",
               "address": "Paris, France",
               "source": "https://www.google.com/maps/embed/v1/place?q=paris&key="}

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, 'get', mock_get)

    assert get_place_info("paris", "") == results
