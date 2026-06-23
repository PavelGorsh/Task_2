import allure
import requests
import urls
import json
import random
import string


class UserMethods:

    # Запрос - Создание пользователя
    def send_request_create(self, payload):
        return requests.post(f'{urls.BASE_URL}{urls.CREATE_USER_URL}', data=payload)
    
    # Запрос - Логин пользователя в системе
    def send_request_login(self, payload):
        return requests.post(f'{urls.BASE_URL}{urls.LOGIN_USER_URL}', data=payload)
    
    # Запрос - Изменение информации о пользователе
    def send_request_change(self, payload, token):
        return requests.patch(f'{urls.BASE_URL}{urls.USER_DATA_URL}', headers={'Authorization': token}, data=payload)

    @allure.step("Создать пользователя")
    def create_user(self, email = None, password = None, name = None):
        # собираем тело запроса
        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        # отправляем запрос на регистрацию пользователя и сохраняем ответ в переменную response
        response = self.send_request_create(payload)

        try:
            return response.json(), response.status_code
        except json.decoder.JSONDecodeError:
            return response.text, response.status_code

    @allure.step("Залогинить пользователя")
    def login_user(self, email = None, password = None):

        # собираем тело запроса
        payload_login = {
            "email": email,
            "password": password
        }

        # отправляем запрос на логин пользователя и сохраняем ответ в переменную response
        response = self.send_request_login(payload_login)

        try:
            return response.json(), response.status_code
        except json.decoder.JSONDecodeError:
            return response.text, response.status_code

    @allure.step("Изменить информацию о пользователе")    
    def change_user_data(self, payload_change = None, token = None):

        # отправляем запрос на логин пользователя и сохраняем ответ в переменную response
        response = self.send_request_change(payload_change, token)

        try:
            return response.json(), response.status_code
        except json.decoder.JSONDecodeError:
            return response.text, response.status_code

    
    def delete_user(self, token):
        # отправляем запрос на удаление пользователя
        requests.delete(f'{urls.BASE_URL}{urls.USER_DATA_URL}', headers={'Authorization': token})


    # метод для создания данных регистрации нового пользователя возвращает список из почты, пароля
    @staticmethod
    def generate_new_user_data():
        # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        # создаём список, чтобы метод мог его вернуть
        login_pass = []

        # генерируем логин, пароль и имя пользователя
        email = generate_random_string(10) + "@yandex.ru"
        password = generate_random_string(10)
        name = generate_random_string(10)

        # добавляем в список логин, пароль и имя пользователя 
        login_pass.append(email)
        login_pass.append(password)
        login_pass.append(name)

        # возвращаем список
        return login_pass
