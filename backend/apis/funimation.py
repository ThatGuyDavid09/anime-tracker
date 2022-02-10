import requests
from pprint import pprint

LOGIN_ENDPOINT = "https://prod-api-funimationnow.dadcdigital.com/api/auth/login/"
SEARCH_ENDPOINT = "https://search.prd.funimationsvc.com/v1/search"

class Funimation:
    def __init__(self, username, password):
        data = {"username": username, "password": password}
        r = requests.post(LOGIN_ENDPOINT, data=data)
        print(r.status_code)
        pprint(r.text)
        self.r = r
        self.token = r.json()["token"]

    def search(self, show_name):
        headers = {"Authorization": "Token " + self.token}
        params = {
            "index": "search-shows",
            "region": "US",
            "lang": "en-US",
            "q": show_name,
            "offset": 0,
            "limit": "3"
        }
        r = requests.get(SEARCH_ENDPOINT, headers=headers, params=params)
        return r
