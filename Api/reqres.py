import requests


class Api:
    base_url = "https://reqres.in/api/"

    def get_request(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url)
        return response

    def create_valid_user(self, valid_user_data):
        response = requests.post(f"{self.base_url}" + "users", json=valid_user_data)
        return response

    def updated_data(self, payload):
        response = requests.patch(f"{self.base_url}"+"users/2", data=payload)
        return response
