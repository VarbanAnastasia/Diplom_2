import requests

from constants.Payload import Payload
from constants.Urls import Urls

url = Urls.CREATE_USER


class TestCreateUser:

    def test_create_user_200(self):
        payload = Payload.create_user_200_payload
        response = requests.request("POST", url=Urls.CREATE_USER, headers=Payload.headers_unique, data=payload)

        assert response.status_code == 200
        assert response.json()["success"] is True

    def test_create_user_one_missing(self):
        payload = Payload.create_user_one_missing
        response = requests.request("POST", url=Urls.CREATE_USER, headers=Payload.headers_unique, data=payload)

        assert response.status_code == 403
        assert response.json()["message"] == "Email, password and name are required fields"

    def test_create_user_existed(self):
        payload = Payload.create_user_existed
        response = requests.request("POST", url=Urls.CREATE_USER, headers=Payload.headers_unique, data=payload)

        assert response.status_code == 403
        assert response.json()["message"] == "User already exists"





