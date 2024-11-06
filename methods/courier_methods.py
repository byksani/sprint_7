import requests
import allure
from data import BASE_URL, COURIERS_URL


class CourierMethods:

    @allure.step("Создание курьера с данными: {payload}")
    def create_courier(self, payload):
        response=requests.post(f'{BASE_URL}{COURIERS_URL}', json=payload)
        return response.status_code, response.json()

    @allure.step("Авторизация курьера с данными: {payload}")
    def login_courier(self, payload):
        response = requests.post(f"{BASE_URL}{COURIERS_URL}/login", json=payload)
        return response.status_code, response.json()

    @allure.step("Удаление курьера по ID: {id}")
    def delete_courier(self, id):
        response = requests.delete(f"{BASE_URL}{COURIERS_URL}/{id}")
        return response.status_code, response.json()