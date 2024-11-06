import requests
import allure
from data import BASE_URL, ORDERS_URL


class OrderMethods:

    @allure.step("Создание заказа с данными: {payload}")
    def create_order(self, payload):
        response=requests.post(f'{BASE_URL}{ORDERS_URL}', json=payload)
        return response.status_code, response.json()

    @allure.step("Получение списка заказов")
    def get_orders(self):
        response=requests.get(f'{BASE_URL}{ORDERS_URL}?limit=10&page=0')
        return response.status_code, response.json()
