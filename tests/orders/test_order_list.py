import allure


@allure.feature("Получение списка заказов")
class TestGetOrders:

    @allure.story("Успешное получение списка заказов")
    def test_get_orders_list_success(self, order_methods):
        status_code, response_context = order_methods.get_orders()

        assert status_code == 200 and isinstance(response_context.get("orders"), list), \
            f"Ожидались статус 200 и список заказов, а получили {status_code} и {response_context}"
