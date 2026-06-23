# Проект автоматизации тестирования API сервиса Stellar Burger
1. Основа для написания автотестов — фреймворк pytest.
2. Основа для автоматизации действий с API — фреймворк requests
3. Установить зависимости — pip install -r requirements.txt.
4. Команда для запуска — pytest -v.
5. Команда для формирования allure-отчёта — pytest tests/ --alluredir=allure_results (в проекте автоматически появится папка allure_results и неё попадут отчёты в формате JSON — по одному на каждый тест)
6. Команда для формирования отчёта в формате веб-страницы — allure serve allure_results (здесь allure_results указывает на папку с отчётами, из которой нужно взять JSON-файлы)
7. URL Stellar Burger: https://qa-stellarburgers.education-services.ru/
8. Документация к API Stellar Burger: https://code.s3.yandex.net/qa-automation-engineer/python-full/diploma/api-Stelar_Burger_10.25.pdf?etag=3584917d935c90b69cb3ffaff58d4f34
