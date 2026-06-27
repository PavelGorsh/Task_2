import allure


class TestCreateUser:

    @allure.title('Проверка создания пользователя с правильными данными')
    def test_create_user_true(self, user):
        #user[0] - user_methods
        #user[1] - user_data (user[1][0] - email, user[1][1] - password, user[1][2] - name)
        #user[2] - response_user_data (после создания пользователя)
        #user[3] - response_status_code (после создания пользователя)
        #user[4] - token (токен авторизации созданного пользователя)
        
        response_user_data = user[2]
        response_status_code = user[3]

        assert (not isinstance(response_user_data, str) and 200 == response_status_code and 
                response_user_data.get('success')), (
                f'status_code: {response_status_code}, message: {response_user_data}')

    @allure.title('Проверка создания двух одинаковых пользователей')
    def test_create_two_equal_users_false(self, user):
        #user[0] - user_methods
        #user[1] - user_data (user[1][0] - email, user[1][1] - password, user[1][2] - name)
        #user[2] - response_user_data (после создания пользователя)
        #user[3] - response_status_code (после создания пользователя)
        #user[4] - token (токен авторизации созданного пользователя)

        #Создание еще одного пользователя с теми же данными
        response_user_data, response_status_code = user[0].create_user(user[1][0], user[1][1], user[1][2])   

        assert (not isinstance(response_user_data, str) and 403 == response_status_code and 
                "User already exists" == response_user_data.get('message') and 
                not response_user_data.get('success')), (
                f'status_code: {response_status_code}, message: {response_user_data}')

    @allure.title('Проверка создания пользователя без заполнения обязательного поля «почта»')
    def test_create_user_without_email_false(self, user_create_false):
        #user[0] - user_methods
        #user[1] - user_data (user[1][0] - email, user[1][1] - password, user[1][2] - name)

        response_user_data, response_status_code = user_create_false[0].create_user(None, user_create_false[1][1], user_create_false[1][2])

        assert (not isinstance(response_user_data, str) and 403 == response_status_code and 
                "Email, password and name are required fields" == response_user_data.get('message') and
                not response_user_data.get('success')), (
                f'status_code: {response_status_code}, message: {response_user_data}')
        

    @allure.title('Проверка создания пользователя без заполнения обязательного поля «пароль»')
    def test_create_user_without_password_false(self, user_create_false):
        #user[0] - user_methods
        #user[1] - user_data (user[1][0] - email, user[1][1] - password, user[1][2] - name)

        response_user_data, response_status_code = user_create_false[0].create_user(user_create_false[1][0], None, user_create_false[1][2])

        assert (not isinstance(response_user_data, str) and 403 == response_status_code and 
                "Email, password and name are required fields" == response_user_data.get('message') and
                not response_user_data.get('success')), (
                f'status_code: {response_status_code}, message: {response_user_data}')
        
    @allure.title('Проверка создания пользователя без заполнения обязательного поля «имя»')
    def test_create_user_without_name_false(self, user_create_false):
        #user[0] - user_methods
        #user[1] - user_data (user[1][0] - email, user[1][1] - password, user[1][2] - name)

        response_user_data, response_status_code = user_create_false[0].create_user(user_create_false[1][0], user_create_false[1][1], None)

        assert (not isinstance(response_user_data, str) and 403 == response_status_code and 
                "Email, password and name are required fields" == response_user_data.get('message') and
                not response_user_data.get('success')), (
                f'status_code: {response_status_code}, message: {response_user_data}')
