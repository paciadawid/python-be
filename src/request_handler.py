import requests


class RequestsHandler:

    def __init__(self, token):
        self.base_url = "https://gorest.co.in/public/v2"
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {token}"
        }

    def post_request(self, endpoint, body=None):
        res = requests.post(self.base_url + endpoint, headers=self.headers, json=body)
        return res.status_code, res.json()

    def get_request(self, endpoint, params=None):
        res = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        return res.status_code, res.json()

    def delete_request(self, endpoint):
        res = requests.delete(self.base_url + endpoint, headers=self.headers)
        return res.status_code

    def put_request(self, endpoint, body=None):
        res = requests.put(self.base_url + endpoint, headers=self.headers, json=body)
        return res.status_code, res.json()
