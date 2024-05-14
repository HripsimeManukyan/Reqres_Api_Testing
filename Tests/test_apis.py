from Api.reqres import Api
import pytest


class TestApi:
    @pytest.fixture
    def api(self):
        return Api()

    @pytest.fixture
    def valid_user_data(self):
        return {
            "name": "John Smith",
            "job": "QA Engineer"
        }

    @pytest.fixture
    def payload(self):
        return {
            "name": "Ann Brown"
        }

    @pytest.mark.parametrize("endpoint", ["users", "users/2", "invalid_endpoint"])
    def test_get_request(self, api, endpoint):
        response = api.get_request(endpoint)
        assert response.status_code != 404

    def test_create_user(self, api, valid_user_data):
        response = api.create_valid_user(valid_user_data)
        assert response.status_code == 201
        data = response.json()
        # print(data)
        assert "id" in data

    def test_update_specific_data(self, api, payload):
        response = api.updated_data(payload)
        assert response.status_code == 200
        assert response.json()["name"] == "Ann Brown"
        # print(response.text)
