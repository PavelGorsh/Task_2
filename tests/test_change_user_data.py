import allure
import pytest
import data


class TestChangeUser:

    @allure.title('Проверка изменения данных пользователя c авторизацией (почта, имя)')
    @pytest.mark.parametrize('field', data.fields_keys_email_name) # перебор ключей payload
    def test_change_user_email_name_auth_true(self, user, field):
        #user[0] - user_methods
        #user[1] - user_data (user[1][0] - email, user[1][1] - password, user[1][2] - name)
        #user[2] - response_user_data (после создания пользователя)
        #user[3] - response_status_code (после создания пользователя)
        #user[4] - token (токен авторизации созданного пользователя)

        gen_data = user[0].generate_new_user_data() # генерация набора данных на замену
        fields_payload = {"email": gen_data[0], "password": gen_data[1], "name": gen_data[2]}

        payload_change = {field: fields_payload.get(field)} # выбор одной пары ключ-значения для payload
        response_user_data, response_status_code = user[0].change_user_data(payload_change, user[4])

        assert (not isinstance(response_user_data, str) and 200 == response_status_code and 
                response_user_data.get('success') and
                response_user_data.get('user').get(field) == fields_payload.get(field)), (
                f'status_code: {response_status_code}, message: {response_user_data}')
    
    # Пароль проверяется отдельно, потому что нет возврата его значения, assert другой
    @allure.title('Проверка изменения данных пользователя c авторизацией (пароль)')
    def test_change_user_password_auth_true(self, user):
        #user[0] - user_methods
        #user[1] - user_data (user[1][0] - email, user[1][1] - password, user[1][2] - name)
        #user[2] - response_user_data (после создания пользователя)
        #user[3] - response_status_code (после создания пользователя)
        #user[4] - token (токен авторизации созданного пользователя)

        gen_data = user[0].generate_new_user_data() # генерация набора данных на замену
        fields_payload = {"email": gen_data[0], "password": gen_data[1], "name": gen_data[2]}

        payload_change = {"password": fields_payload.get("password")} # выбор одной пары ключ-значения для payload
        response_user_data, response_status_code = user[0].change_user_data(payload_change, user[4])

        assert (not isinstance(response_user_data, str) and 200 == response_status_code and 
                response_user_data.get('success')), (
                f'status_code: {response_status_code}, message: {response_user_data}')
        
    @allure.title('Проверка изменения данных пользователя без авторизации (почта, имя, пароль)')
    @pytest.mark.parametrize('field', data.fields_keys_full) # перебор ключей payload
    def test_change_user_data_no_auth_false(self, user, field):
        #user[0] - user_methods
        #user[1] - user_data (user[1][0] - email, user[1][1] - password, user[1][2] - name)
        #user[2] - response_user_data (после создания пользователя)
        #user[3] - response_status_code (после создания пользователя)
        #user[4] - token (токен авторизации созданного пользователя)

        gen_data = user[0].generate_new_user_data() # генерация набора данных на замену
        fields_payload = {"email": gen_data[0], "password": gen_data[1], "name": gen_data[2]}

        payload_change = {field: fields_payload.get(field)} # выбор одной пары ключ-значения для payload
        response_user_data, response_status_code = user[0].change_user_data(payload_change, None)

        assert (not isinstance(response_user_data, str) and 401 == response_status_code and 
                not response_user_data.get('success') and
                "You should be authorised" == response_user_data.get('message')), (
                f'status_code: {response_status_code}, message: {response_user_data}')
