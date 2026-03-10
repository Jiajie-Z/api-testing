import requests
from utils.config import API_KEY


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {"x-api-key": API_KEY} if API_KEY else {}

    def get(self, endpoint, params=None):
        return requests.get(
            f"{self.base_url}{endpoint}",
            params=params,
            headers=self.headers
        )

    def post(self, endpoint, json=None):
        return requests.post(
            f"{self.base_url}{endpoint}",
            json=json,
            headers=self.headers
        )

    def put(self, endpoint, json=None):
        return requests.put(
            f"{self.base_url}{endpoint}",
            json=json,
            headers=self.headers
        )

    def delete(self, endpoint):
        return requests.delete(
            f"{self.base_url}{endpoint}",
            headers=self.headers
        )