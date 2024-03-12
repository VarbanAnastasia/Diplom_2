import allure
import requests

from constants.Constants import Constants
from constants.Payload import IngredientsPayload


@allure.epic("Создание заказа")
class TestCreateOrder:
    @allure.title("Тест на успешное создание заказа без авторизации с ингредиентами")
    def test_successful_order_creation_without_authentication_with_ingredients(self):
        response = requests.request("POST", Constants.CREATE_ORDER, headers=Constants.headers,
                                 json=IngredientsPayload.data_ingredient)
        assert response.json()['success'] == True
        assert response.json()['name'] == "Бессмертный флюоресцентный бургер"

    @allure.title("Тест на создание заказа без авторизации без ингредиентов и проверку статуса")
    def test_order_creation_without_authentication_without_ingredients(self):
        response = requests.request("POST",Constants.CREATE_ORDER, headers=Constants.headers,
                                 json=IngredientsPayload.data_not_ingredient)
        assert response.status_code == 400
        assert response.text == '{"success":false,"message":"Ingredient ids must be provided"}'

    @allure.title("Тест на создание заказа без авторизации с неверным хешем ингредиентов и проверку статуса")
    def test_order_creation_without_authentication_with_invalid_ingredients(self):
        response = requests.request("POST",Constants.CREATE_ORDER, headers=Constants.headers,
                                 json=IngredientsPayload.data_bad_ingredient)
        assert response.status_code == 400
        assert response.text == '{"success":false,"message":"One or more ids provided are incorrect"}'
