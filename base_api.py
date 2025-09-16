import requests
import allure


class BaseAPI:
    def __init__(self, base_url="https://api.kinopoisk.dev", api_key="CH5EBJX-8BR4F9T-NAEDG5V-YVWHHTA"):
        self.base_url = base_url
        self.api_key = api_key
        self.headers = {
            "accept": "application/json",
            "X-API-KEY": self.api_key
        }

    def _get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response
