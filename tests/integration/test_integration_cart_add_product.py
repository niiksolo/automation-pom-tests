import pytest
import requests
import allure
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.base_page import BasePage
from pages.login_page import LoginPage
import os
from dotenv import load_dotenv
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()
email = os.getenv("USER_EMAIL")
password = os.getenv("USER_PASSWORD")

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

        response = session.get("https://api.kasta.ua/api/v2/basket")
        assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"

        total_items = sum(
            item.get("quantity", 0)
            for block in response.json().get("items", [])
            for item in block.get("items", [])
        )
        assert total_items > 0, "Корзина пуста, товар не добавился через UI"
