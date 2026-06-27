import allure
import requests
import urls
import json


class OrderMethods:

    # Запрос - Создание заказа
    def send_request_create_order(self, payload, token):
        return requests.post(f'{urls.BASE_URL}{urls.ORDERS_URL}', headers={'Authorization': token}, data=payload)
    
    # Запрос - Получение списка всех заказов
    def send_request_get_ingredients(self):
        return requests.get(f'{urls.BASE_URL}{urls.GET_INGREDIENTS_URL}')
    
    # Запрос - Получение списка всех заказов ВОЗМОЖНО УДАЛЕНИЕ
    def send_request_get_orders(self):
        return requests.get(f'{urls.BASE_URL}{urls.ORDERS_URL}')
    
    # Запрос - Получение списка всех заказов конкретного пользователя
    def send_request_get_orders_by_user(self, token):
        return requests.get(f'{urls.BASE_URL}{urls.ORDERS_URL}', headers={'Authorization': token})

    @allure.step("Создать заказ")
    def create_order(self, ingredients_hash = None, token = None):

        # собираем тело запроса
        payload = {
            "ingredients": ingredients_hash,
        }

        # отправляем запрос на создание заказа и сохраняем ответ в переменную response
        response = self.send_request_create_order(payload, token)

        try:
            return response.json(), response.status_code
        except json.decoder.JSONDecodeError:
            return response.text, response.status_code
    
    @allure.step("Получить данные об ингредиентах")
    def get_ingredients(self):

        # отправляем запрос на получение ингредиентов и сохраняем ответ в переменную response
        response = self.send_request_get_ingredients()

        try:
            return response.json(), response.status_code
        except json.decoder.JSONDecodeError:
            return response.text, response.status_code

    @allure.step("Получить все заказы") # ВОЗМОЖНО УДАЛЕНИЕ
    def get_orders(self):

        # отправляем запрос на получение заказов и сохраняем ответ в переменную response
        response = self.send_request_get_orders()

        try:
            return response.json(), response.status_code
        except json.decoder.JSONDecodeError:
            return response.text, response.status_code
        
    @allure.step("Получить все заказы конкретного пользователя")
    def get_orders_by_user(self, token):

        # отправляем запрос на получение заказов пользователя и сохраняем ответ в переменную response
        response = self.send_request_get_orders_by_user(token)

        try:
            return response.json(), response.status_code
        except json.decoder.JSONDecodeError:
            return response.text, response.status_code
