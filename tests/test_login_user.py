import allure
import requests

from constants.payload import PayloadLoginUser
from constants.constants import Constants


@allure.epic("Авторизация пользователя")
class TestLoginUser:

    @allure.title("Авторизация пользователя")
    def test_login_user_200(self):
        response = requests.request("POST", Constants.LOG_IN_USER, headers=Constants.headers,
                                    data=PayloadLoginUser.login_user_existed)

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Авторизация пользователя с неверными данными")
    def test_login_user_401(self):
        response = requests.request("POST", Constants.LOG_IN_USER, headers=Constants.headers,
                                    data=PayloadLoginUser.login_wrong_data)

        assert response.status_code == 401
        assert response.json()["message"] == "email or password are incorrect"
