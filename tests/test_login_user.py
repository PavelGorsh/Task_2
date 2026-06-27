import allure


class TestLoginUser:

    @allure.title('Проверка логина пользователя с правильными данными')
    def test_login_user_true(self, user):
        #user[0] - user_methods
        #user[1] - user_data (user[1][0] - email, user[1][1] - password, user[1][2] - name)
        #user[2] - response_user_data (после создания пользователя)
        #user[3] - response_status_code (после создания пользователя)
        #user[4] - token (токен авторизации созданного пользователя)

        response_user_data, response_status_code = user[0].login_user(user[1][0], user[1][1])

        assert (not isinstance(response_user_data, str) and 200 == response_status_code and 
                response_user_data.get('success')), (
                f'status_code: {response_status_code}, message: {response_user_data}')

    @allure.title('Проверка логина пользователя без заполнения обязательного поля «почта»')
    def test_login_user_without_email_false(self, user):
        #user[0] - user_methods
        #user[1] - user_data (user[1][0] - email, user[1][1] - password, user[1][2] - name)
        #user[2] - response_user_data (после создания пользователя)
        #user[3] - response_status_code (после создания пользователя)
        #user[4] - token (токен авторизации созданного пользователя)

        response_user_data, response_status_code = user[0].login_user(None, user[1][1])

        assert (not isinstance(response_user_data, str) and 401 == response_status_code and 
                "email or password are incorrect" == response_user_data.get('message')), (
                f'status_code: {response_status_code}, message: {response_user_data}')

    @allure.title('Проверка логина пользователя без заполнения обязательного поля «пароль»')
    def test_login_user_without_password_false(self, user):
        #user[0] - user_methods
        #user[1] - user_data (user[1][0] - email, user[1][1] - password, user[1][2] - name)
        #user[2] - response_user_data (после создания пользователя)
        #user[3] - response_status_code (после создания пользователя)
        #user[4] - token (токен авторизации созданного пользователя)

        response_user_data, response_status_code = user[0].login_user(user[1][0], None)

        assert (not isinstance(response_user_data, str) and 401 == response_status_code and 
                "email or password are incorrect" == response_user_data.get('message')), (
                f'status_code: {response_status_code}, message: {response_user_data}')

    @allure.title('Проверка логина пользователя с несуществующей парой почта-пароль')
    def test_login_user_with_unexisting_user_false(self, user):
        #user[0] - user_methods
        #user[1] - user_data (user[1][0] - email, user[1][1] - password, user[1][2] - name)
        #user[2] - response_user_data (после создания пользователя)
        #user[3] - response_status_code (после создания пользователя)
        #user[4] - token (токен авторизации созданного пользователя)

        user_data = user[0].generate_new_user_data() # Создаем другую пару почта-пароль для логина
        response_user_data, response_status_code = user[0].login_user(user_data[0], user_data[1])

        assert (not isinstance(response_user_data, str) and 401 == response_status_code and 
                "email or password are incorrect" == response_user_data.get('message')), (
                f'status_code: {response_status_code}, message: {response_user_data}')

    @allure.title('Проверка логина пользователя с ошибкой в поле «почта»')
    def test_login_user_with_uncorrect_email_false(self, user):
        #user[0] - user_methods
        #user[1] - user_data (user[1][0] - email, user[1][1] - password, user[1][2] - name)
        #user[2] - response_user_data (после создания пользователя)
        #user[3] - response_status_code (после создания пользователя)
        #user[4] - token (токен авторизации созданного пользователя)

        response_user_data, response_status_code = user[0].login_user(f'{user[1][0]}mistake', user[1][1])

        assert (not isinstance(response_user_data, str) and 401 == response_status_code and 
                "email or password are incorrect" == response_user_data.get('message')), (
                f'status_code: {response_status_code}, message: {response_user_data}')

    @allure.title('Проверка логина пользователя с ошибкой в поле «пароль»')
    def test_login_user_with_uncorrect_password_false(self, user):
        #user[0] - user_methods
        #user[1] - user_data (user[1][0] - email, user[1][1] - password, user[1][2] - name)
        #user[2] - response_user_data (после создания пользователя)
        #user[3] - response_status_code (после создания пользователя)
        #user[4] - token (токен авторизации созданного пользователя)

        response_user_data, response_status_code = user[0].login_user(user[1][0], f'{user[1][1]}mistake')

        assert (not isinstance(response_user_data, str) and 401 == response_status_code and 
                "email or password are incorrect" == response_user_data.get('message')), (
                f'status_code: {response_status_code}, message: {response_user_data}')
