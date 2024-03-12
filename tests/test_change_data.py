import allure
import pytest
import requests


from constants.payload import PayloadChangeData
from constants.constants import Constants


@allure.epic("Обновление данных пользователя")
class TestUpdateDataUser:

    def get_authentication_token(self):
        token = requests.request("POST", url=Constants.LOG_IN_USER, headers=Constants.headers,
                                 data=PayloadChangeData.user)
        new_token = token.json()['accessToken']
        return new_token

    @allure.title("Обновление данных пользователя")
    def test_update_data_user_200(self):
        new_token = self.get_authentication_token()
        payload = PayloadChangeData.user_changed_data
        response = requests.request("PATCH", url=Constants.CHANGE_DATA,
                                    headers={'Authorization': new_token}, data=payload)

        assert response.status_code == 200
        assert response.json()["user"]["name"] == "Nastya"

    @pytest.mark.parametrize(("data", "status_code"), [
        (
                pytest.param(PayloadChangeData.data_double, 400)
        )
    ])
    @allure.title("Обновление данных пользователя с неверными данными")
    def test_create_user_fail(self, data, status_code):
        response = requests.request("PATCH", url=Constants.CHANGE_DATA, headers=Constants.headers,
                                    data=PayloadChangeData.data_double, json=data)
        assert response.status_code == status_code
