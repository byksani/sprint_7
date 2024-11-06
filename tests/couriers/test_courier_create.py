import allure


@allure.feature("Курьер")
class TestCreateCourier:

    @allure.story("Успешное создание курьера")
    def test_create_courier_success(self, courier_methods, created_courier):
        status_code, response_context = created_courier
        assert status_code == 201 and response_context == {"ok": True}, \
            f"Ожидались статус 201 и ответ {{'ok': True}}, а получили {status_code} и {response_context}"

    @allure.story("Создание курьера без указания имени")
    def test_create_courier_without_name_success(self, courier_without_name, courier_methods, unique_courier_data):
        status_code, response_context = courier_without_name
        assert status_code == 201 and response_context == {"ok": True}, \
            f"Ожидались статус 201 и ответ {{'ok': True}}, а получили {status_code} и {response_context}"

    @allure.story("Попытка создания курьера без логина")
    def test_create_courier_without_login_error(self, courier_methods, unique_courier_data):
        status_code, response_context = courier_methods.create_courier({
            "firstName": unique_courier_data["firstName"],
            "password": unique_courier_data["password"]
        })
        assert status_code == 400 and response_context == {"code": 400, "message": "Недостаточно данных для создания учетной записи"}, \
            f"Ожидались статус 400 и сообщение об ошибке, а получили {status_code} и {response_context}"

    @allure.story("Попытка создания курьера без пароля")
    def test_create_courier_without_password_error(self, courier_methods, unique_courier_data):
        status_code, response_context = courier_methods.create_courier({
            "firstName": unique_courier_data["firstName"],
            "login": unique_courier_data["login"]
        })
        assert status_code == 400 and response_context == {"code": 400, "message": "Недостаточно данных для создания учетной записи"}, \
            f"Ожидались статус 400 и сообщение об ошибке, а получили {status_code} и {response_context}"

    @allure.story("Попытка создания дубликата курьера")
    def test_create_duplicate_courier_error(self, created_courier, courier_methods, unique_courier_data):
        status_code, response_context = courier_methods.create_courier(unique_courier_data)
        assert status_code == 409 and response_context == {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}, \
            f"Ожидались статус 409 и сообщение о дублировании, а получили {status_code} и {response_context}"
