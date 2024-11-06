import allure


@allure.feature("Авторизация курьера")
class TestLoginCourier:

    @allure.story("Успешная авторизация курьера")
    def test_login_courier_success(self, courier, courier_methods, unique_courier_data):
        status_code, response_data = courier_methods.login_courier({
            "login": unique_courier_data["login"],
            "password": unique_courier_data["password"]
        })
        assert status_code == 200 and "id" in response_data and response_data["id"] > 0, \
            f"Ожидались статус 200 и поле 'id' > 0, а получили {status_code} и {response_data}"

    @allure.story("Проверка ответа успешной авторизации курьера")
    def test_login_courier_success_check_response(self, courier, courier_methods, unique_courier_data):
        status_code, response_data = courier_methods.login_courier({
            "login": unique_courier_data["login"],
            "password": unique_courier_data["password"]
        })
        assert "id" in response_data and response_data["id"] > 0, \
            f"Ожидалось, что 'id' > 0, но получили {response_data}"

    @allure.story("Ошибка при авторизации без обязательного поля")
    def test_login_courier_without_required_field_error(self, courier, courier_methods, unique_courier_data):
        status_code, response_context = courier_methods.login_courier({
            "password": unique_courier_data["password"]
        })
        assert status_code == 400 and response_context == {"code": 400, "message": "Недостаточно данных для входа"}, \
            f"Ожидались статус 400 и сообщение об ошибке, а получили {status_code} и {response_context}"

    @allure.story("Ошибка при авторизации несуществующего курьера")
    def test_login_with_non_existing_courier_error(self, courier_methods, unique_courier_data):
        status_code, response_context = courier_methods.login_courier({
            "login": unique_courier_data["login"],
            "password": unique_courier_data["password"]
        })
        assert status_code == 404 and response_context == {"code": 404, "message": "Учетная запись не найдена"}, \
            f"Ожидались статус 404 и сообщение 'Курьер не найден', а получили {status_code} и {response_context}"

    @allure.story("Ошибка при авторизации с неверным логином")
    def test_login_with_invalid_login_error(self, courier, courier_methods, unique_courier_data):
        status_code, response_context = courier_methods.login_courier({
            "login": "wrong_login",
            "password": unique_courier_data["password"]
        })
        assert status_code == 404 and response_context == {"code": 404, "message": "Учетная запись не найдена"}, \
            f"Ожидались статус 404 и сообщение 'Курьер не найден', а получили {status_code} и {response_context}"

    @allure.story("Ошибка при авторизации с неверным паролем")
    def test_login_with_invalid_password_error(self, courier, courier_methods, unique_courier_data):
        status_code, response_context = courier_methods.login_courier({
            "login": unique_courier_data["login"],
            "password": "wrong_password"
        })
        assert status_code == 404 and response_context == {"code": 404, "message": "Учетная запись не найдена"}, \
            f"Ожидались статус 404 и сообщение 'Курьер не найден', а получили {status_code} и {response_context}"
