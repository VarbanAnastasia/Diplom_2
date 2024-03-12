import allure
import requests
from constants.Constants import Constants
from constants.Payload import PayloadChangeData


@allure.epic("Получение заказов пользователя")
class TestGetOrderUser:
    @allure.title("Получение авторизационного токена и сохранение в переменную")
    def get_authentication_token(self):
        token = requests.request("POST", Constants.LOG_IN_USER, headers=Constants.headers,
                              data=PayloadChangeData.user)
        new_token = token.json()['accessToken']
        return new_token

    @allure.title("Получение заказов авторизованного пользователя")
    def test_get_orders_for_authenticated_user(self):
        new_token = self.get_authentication_token()
        response = requests.request("GET", Constants.ORDER,
                                headers={'Authorization': new_token}, data=PayloadChangeData.user_changed_data)
        body = response
        assert response.status_code == 200 and body.json()['success'] == True

    @allure.title("Получение заказов неавторизованного пользователя")
    def test_get_orders_for_unauthenticated_user(self):
        response = requests.request("GET", Constants.ORDER, headers=Constants.headers)
        body = response
        assert response.status_code == 401 and body.json()['success'] == False
