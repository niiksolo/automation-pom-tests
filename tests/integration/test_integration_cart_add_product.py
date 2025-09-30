import pytest
import requests
import allure
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.base_page import BasePage
from pages.login_page import LoginPage
import os
from dotenv import load_dotenv
import time

load_dotenv()
email = os.getenv("SITE_LOGIN")
password = os.getenv("SITE_PASSWORD")

@pytest.mark.skipif(True, reason="тест локально работает в CICD никак")
@pytest.mark.integration
@allure.feature("Корзина")
@allure.story("UI → API проверка")
@allure.title("Добавление товара через UI и проверка корзины через API")
def test_add_product_ui_api(browser):
    base = BasePage(browser)
    home = HomePage(browser)
    login = LoginPage(browser)
    product = ProductPage(browser)

    with allure.step("Авторизация через UI"):
        base.login(login, home, email, password)
        home.wait_until_loaded()

    with allure.step('Ищем товар "носки" и добавляем в корзину'):
        home.search_by_button("носки")
        product.add_product_to_cart()

    with allure.step("Проверка корзины через API"):
        session = requests.Session()
        for c in browser.get_cookies():
            session.cookies.set(c['name'], c['value'], domain=c.get('domain'))

        max_attempts = 15
        for attempt in range(max_attempts):
            response = session.get("https://api.kasta.ua/api/v2/basket")
            assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"

            total_items = sum(
                item.get("quantity", 0)
                for block in response.json().get("items", [])
                for item in block.get("items", [])
            )

            if total_items > 0:
                break  # товар добавлен, продолжаем тест
            else:
                allure.step(f"Попытка {attempt + 1}/{max_attempts}: корзина пуста, ждём 1 сек.")
                time.sleep(1)
        else:
            # Если по истечении всех попыток корзина пуста — падаем
            pytest.fail(f"Корзина пуста после {max_attempts} попыток, товар не добавился через UI")
