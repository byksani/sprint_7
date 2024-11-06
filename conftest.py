import pytest
import random
import string
from methods.courier_methods import CourierMethods
from methods.orders_methods import OrderMethods


@pytest.fixture()
def courier_methods():
    return CourierMethods()

@pytest.fixture()
def order_methods():
    return OrderMethods()

@pytest.fixture()
def courier(courier_methods, unique_courier_data):
    courier_methods.create_courier(unique_courier_data)
    status_code, response_context = courier_methods.login_courier({
        "login": unique_courier_data["login"],
        "password": unique_courier_data["password"]
    })
    courier_id = response_context["id"]

    yield courier_id

    courier_methods.delete_courier(courier_id)

@pytest.fixture()
def created_courier(courier_methods, unique_courier_data):
    status_code, response_context = courier_methods.create_courier(unique_courier_data)

    yield status_code, response_context

    status_code, response_context = courier_methods.login_courier({
        "login": unique_courier_data["login"],
        "password": unique_courier_data["password"]
    })
    courier_id = response_context["id"]
    courier_methods.delete_courier(courier_id)

@pytest.fixture()
def courier_without_name(courier_methods, unique_courier_data):
    payload = {
        "login": unique_courier_data["login"],
        "password": unique_courier_data["password"]
    }
    status_code, response_context = courier_methods.create_courier(payload)

    yield status_code, response_context

    status_code, login_response = courier_methods.login_courier(payload)
    courier_id = login_response.get("id")
    courier_methods.delete_courier(courier_id)

def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

@pytest.fixture()
def unique_courier_data():

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    return payload
