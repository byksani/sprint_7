import pytest
import allure


@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.story("Успешное создание заказа с различными параметрами цвета")
    @pytest.mark.parametrize("colors", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    def test_create_order_with_colors_success(self, order_methods, colors):
        payload = {
            "firstName": "Иван",
            "lastName": "Иванов",
            "address": "Москва, ул. Пушкина, дом 10",
            "metroStation": 4,
            "phone": "+7 800 555 35 35",
            "rentTime": 5,
            "deliveryDate": "2023-10-10",
            "comment": "Позвоните за час до приезда",
            "color": colors
        }

        status_code, response_context = order_methods.create_order(payload)

        assert status_code == 201 and "track" in response_context, \
            f"Ожидались статус 201 и что тело ответа содержит 'track', а получили {status_code} и {response_context}"
