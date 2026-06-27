import allure
import data


class TestOrders:

    @allure.title('Проверка создания заказа с авторизацией')
    def test_create_order_auth_true(self, user, order):
        #user[0] - user_methods
        #user[1] - user_data (user[1][0] - email, user[1][1] - password, user[1][2] - name)
        #user[2] - response_user_data (после создания пользователя)
        #user[3] - response_status_code (после создания пользователя)
        #user[4] - token (токен авторизации созданного пользователя)

        # Обязательные игредиенты 
        # Флюоресцентная булка R2-D3 response_ingredients_data.get('data')[0], 
        # Краторная булка N-200i response_ingredients_data.get('data')[8]
        # Общее количество различных ингредиентов 14
        response_ingredients_data, _ = order.get_ingredients()
        ingredients_hash = [data.fluor_bun_hash, response_ingredients_data.get('data')[1].get('_id')]

        response_order_data, response_status_code = order.create_order(ingredients_hash, user[4])

        # Требуется несколько проверок, в том числе owner name и id, чтобы различить ответы с авторизацией и без
        assert (not isinstance(response_order_data, str) and 200 == response_status_code and
                response_order_data.get('order').get("number") and
                response_order_data.get('success') and
                response_order_data.get('order').get("owner").get('name') == user[1][2],
                response_order_data.get('order').get("_id")), (
                f'status_code: {response_status_code}, message: {response_order_data}')
        
    @allure.title('Проверка создания заказа с невалидным хэшем ингредиента с авторизацией')
    def test_create_order_auth_true_ids_false(self, user, order):
        #user[0] - user_methods
        #user[1] - user_data (user[1][0] - email, user[1][1] - password, user[1][2] - name)
        #user[2] - response_user_data (после создания пользователя)
        #user[3] - response_status_code (после создания пользователя)
        #user[4] - token (токен авторизации созданного пользователя)

        # Обязательные игредиенты 
        # Флюоресцентная булка R2-D3 response_ingredients_data.get('data')[0], 
        # Краторная булка N-200i response_ingredients_data.get('data')[8]
        # Общее количество различных ингредиентов 14
        response_ingredients_data, _ = order.get_ingredients()
        ingredients_hash = [data.fluor_bun_hash+"mistake", response_ingredients_data.get('data')[1].get('_id')]

        response_order_data, response_status_code = order.create_order(ingredients_hash, user[4])

        assert (500 == response_status_code), (
                f'status_code: {response_status_code}, message: {response_order_data}')
        
    @allure.title('Проверка создания заказа с отсутствующими ингредиентами с авторизацией')
    def test_create_order_auth_true_ingredients_false(self, user, order):
        #user[0] - user_methods
        #user[1] - user_data (user[1][0] - email, user[1][1] - password, user[1][2] - name)
        #user[2] - response_user_data (после создания пользователя)
        #user[3] - response_status_code (после создания пользователя)
        #user[4] - token (токен авторизации созданного пользователя)

        # Обязательные игредиенты 
        # Флюоресцентная булка R2-D3 response_ingredients_data.get('data')[0], 
        # Краторная булка N-200i response_ingredients_data.get('data')[8]
        # Общее количество различных ингредиентов 14
        
        ingredients_hash = [None, None]

        response_order_data, response_status_code = order.create_order(ingredients_hash, user[4])

        assert (not isinstance(response_order_data, str) and 400 == response_status_code and
                response_order_data.get('message') == "Ingredient ids must be provided" and
                not response_order_data.get('success')), (
                f'status_code: {response_status_code}, message: {response_order_data}')
        
    @allure.title('Проверка создания заказа без авторизации')
    def test_create_order_auth_false(self, order):
        #user[0] - user_methods
        #user[1] - user_data (user[1][0] - email, user[1][1] - password, user[1][2] - name)
        #user[2] - response_user_data (после создания пользователя)
        #user[3] - response_status_code (после создания пользователя)
        #user[4] - token (токен авторизации созданного пользователя)

        # Обязательные игредиенты 
        # Флюоресцентная булка R2-D3 response_ingredients_data.get('data')[0], 
        # Краторная булка N-200i response_ingredients_data.get('data')[8]
        # Общее количество различных ингредиентов 14
        response_ingredients_data, _ = order.get_ingredients()
        ingredients_hash = [data.fluor_bun_hash, response_ingredients_data.get('data')[1].get('_id')]

        response_order_data, response_status_code = order.create_order(ingredients_hash, None)

        # Требуется несколько проверок, в том числе owner name и id, чтобы различить ответы с авторизацией и без
        assert (not isinstance(response_order_data, str) and 200 == response_status_code and
                response_order_data.get('order').get("number") and
                response_order_data.get('success') and
                response_order_data.get('order').get("owner") == None and
                response_order_data.get('order').get("_id") == None), (
                f'status_code: {response_status_code}, message: {response_order_data}')
        
    @allure.title('Проверка получения заказов конкретного пользователя с авторизацией')
    def test_get_orders_by_user_auth_true(self, user, order):
        #user[0] - user_methods
        #user[1] - user_data (user[1][0] - email, user[1][1] - password, user[1][2] - name)
        #user[2] - response_user_data (после создания пользователя)
        #user[3] - response_status_code (после создания пользователя)
        #user[4] - token (токен авторизации созданного пользователя)

        # Обязательные игредиенты 
        # Флюоресцентная булка R2-D3 response_ingredients_data.get('data')[0], 
        # Краторная булка N-200i response_ingredients_data.get('data')[8]
        # Общее количество различных ингредиентов 14
        response_ingredients_data, _ = order.get_ingredients()

        orders_quantity = 0

        ingredients_hash = [data.fluor_bun_hash, response_ingredients_data.get('data')[1].get('_id')]
        _, _ = order.create_order(ingredients_hash, user[4])
        orders_quantity += 1

        ingredients_hash = [data.krator_bun_hash, response_ingredients_data.get('data')[3].get('_id'), response_ingredients_data.get('data')[5].get('_id')]
        _, _ = order.create_order(ingredients_hash, user[4])
        orders_quantity += 1

        ingredients_hash = [data.krator_bun_hash, response_ingredients_data.get('data')[6].get('_id'), response_ingredients_data.get('data')[12].get('_id')]
        _, _ = order.create_order(ingredients_hash, user[4])
        orders_quantity += 1

        response_order_data, response_status_code = order.get_orders_by_user(user[4])

        assert (not isinstance(response_order_data, str) and 200 == response_status_code and
                response_order_data.get('success') and
                len(response_order_data.get('orders')) == orders_quantity), (
                f'status_code: {response_status_code}, message: {response_order_data}')
        
    @allure.title('Проверка получения заказов конкретного пользователя без авторизации')
    def test_get_orders_by_user_auth_false(self, user, order):
        #user[0] - user_methods
        #user[1] - user_data (user[1][0] - email, user[1][1] - password, user[1][2] - name)
        #user[2] - response_user_data (после создания пользователя)
        #user[3] - response_status_code (после создания пользователя)
        #user[4] - token (токен авторизации созданного пользователя)

        # Обязательные игредиенты 
        # Флюоресцентная булка R2-D3 response_ingredients_data.get('data')[0], 
        # Краторная булка N-200i response_ingredients_data.get('data')[8]
        # Общее количество различных ингредиентов 14
        response_ingredients_data, _ = order.get_ingredients()

        orders_quantity = 0

        ingredients_hash = [data.fluor_bun_hash, response_ingredients_data.get('data')[1].get('_id')]
        _, _ = order.create_order(ingredients_hash, user[4])
        orders_quantity += 1

        ingredients_hash = [data.krator_bun_hash, response_ingredients_data.get('data')[3].get('_id'), response_ingredients_data.get('data')[5].get('_id')]
        _, _ = order.create_order(ingredients_hash, user[4])
        orders_quantity += 1

        ingredients_hash = [data.krator_bun_hash, response_ingredients_data.get('data')[6].get('_id'), response_ingredients_data.get('data')[12].get('_id')]
        _, _ = order.create_order(ingredients_hash, user[4])
        orders_quantity += 1

        response_order_data, response_status_code = order.get_orders_by_user(None)

        assert (not isinstance(response_order_data, str) and 401 == response_status_code and
                not response_order_data.get('success') and
                response_order_data.get('message') == "You should be authorised"), (
                f'status_code: {response_status_code}, message: {response_order_data}')