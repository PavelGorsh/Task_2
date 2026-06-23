import pytest
from methods.user_methods import UserMethods
from methods.order_methods import OrderMethods

@pytest.fixture()
def user():
    user_methods = UserMethods()
    user_data = user_methods.generate_new_user_data()
    response_user_data, response_status_code = user_methods.create_user(user_data[0], user_data[1], user_data[2]) # email, password, name
    token = response_user_data.get('accessToken') # токен авторизации

    # объект UserMethods, данные (email, password, name), ответ после создания пользователя, код ответа, токен
    yield user_methods, user_data, response_user_data, response_status_code, token
    user_methods.delete_user(token) # удаление пользователя по токену

@pytest.fixture()
def user_create_false(): # для несозданного пользователя не требуется удаление
    user_methods = UserMethods()
    user_data = user_methods.generate_new_user_data()
    return user_methods, user_data

@pytest.fixture()
def order():
    order_methods = OrderMethods()
    return order_methods
