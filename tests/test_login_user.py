import requests

from constants.Payload import PayloadLoginUser
from constants.Urls import Urls

url = Urls.LOG_IN_USER


class TestLoginUser:

    def test_login_user_200(self):

        response = requests.request("POST", url, headers=PayloadLoginUser.headers,
                                    data=PayloadLoginUser.login_user_existed)

        assert response.status_code == 200
        assert response.json()["success"] is True

    def test_login_user_401(self):

        response = requests.request("POST", url, headers=PayloadLoginUser.headers,
                                    data=PayloadLoginUser.login_wrong_data)

        assert response.status_code == 401
        assert response.json()["message"] == "email or password are incorrect"

