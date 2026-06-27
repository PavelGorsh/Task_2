## Задание 2: API

### Автотесты для проверки API программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы API-тесты, покрывающие ручки '/api/auth/register', '/api/auth/login', '/api/auth/user', '/api/orders', '/api/ingredients'

Создан allure-отчёт

### Структура проекта

- `methods` - пакет, содержащий методы ручек API для Stellar Burgers
- `tests` - пакет, содержащий тесты, разделенные по классам. Например, `test_create_user.py`, `test_login_user.py` и т.д.

### Основа для написания автотестов

Фреймворк pytest

### Основа для автоматизации действий с API

Фреймворк requests

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов**

>  `$ pytest -v`

**Формирование allure-отчёта**

>  `$ pytest tests/ --alluredir=allure_results`

**Формирование allure-отчёта в формате веб-страницы**

>  `$ allure serve allure_results`

### Документация

URL Stellar Burgers: https://qa-stellarburgers.education-services.ru/

Документация к API Stellar Burgers: https://code.s3.yandex.net/qa-automation-engineer/python-full/diploma/api-Stelar_Burger_10.25.pdf?etag=3584917d935c90b69cb3ffaff58d4f34
