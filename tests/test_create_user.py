import requests

from constants.Payload import PayloadCreateUser
from constants.Urls import Urls

url = Urls.CREATE_USER


class TestCreateUser:

    def test_create_user_200(self):
        payload = PayloadCreateUser.create_user_200_payload
        response = requests.request("POST", url, headers=PayloadCreateUser.headers_unique, data=payload)

        assert response.status_code == 200
        assert response.json()["success"] is True

    def test_create_user_one_missing(self):
        payload = PayloadCreateUser.create_user_one_missing
        response = requests.request("POST", url=Urls.CREATE_USER, headers=PayloadCreateUser.headers_unique, data=payload)

        assert response.status_code == 403
        assert response.json()["message"] == "Email, password and name are required fields"

    def test_create_user_existed(self):
        payload = PayloadCreateUser.create_user_existed
        response = requests.request("POST", url=Urls.CREATE_USER, headers=PayloadCreateUser.headers_unique, data=payload)

        assert response.status_code == 403
        assert response.json()["message"] == "User already exists"





