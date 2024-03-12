import allure
import requests

from constants.payload import PayloadCreateUser
from constants.constants import Constants


@allure.epic("Создание пользователя")
class TestCreateUser:
    @allure.title("Создание пользователя")
    def test_create_user_200(self):
        payload = PayloadCreateUser.create_user_200_payload
        response = requests.request("POST", url=Constants.CREATE_USER, headers=Constants.headers, data=payload)

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание пользователя с одним отсутствующим полем")
    def test_create_user_one_missing(self):
        payload = PayloadCreateUser.create_user_one_missing
        response = requests.request("POST", url=Constants.CREATE_USER, headers=Constants.headers, data=payload)

        assert response.status_code == 403
        assert response.json()["message"] == "Email, password and name are required fields"

    @allure.title("Создание пользователя уже существующего")
    def test_create_user_existed(self):
        payload = PayloadCreateUser.create_user_existed
        response = requests.request("POST", url=Constants.CREATE_USER, headers=Constants.headers, data=payload)

        assert response.status_code == 403
        assert response.json()["message"] == "User already exists"





