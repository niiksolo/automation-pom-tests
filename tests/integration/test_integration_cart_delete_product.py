import pytest
import requests
import allure
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
import os
from dotenv import load_dotenv

load_dotenv()
email = os.getenv("SITE_LOGIN")
password = os.getenv("SITE_PASSWORD")

@pytest.mark.integration
@allure.feature("Корзина")
@allure.story("UI ↔ API интеграция")
@allure.title("Добавление товара через UI, проверка через API, удаление через UI и проверка корзины")

def test_add_remove_product_ui_api(browser):
    base = BasePage(browser)
    home = HomePage(browser)
    login = LoginPage(browser)
    product = ProductPage(browser)
    cart = CartPage(browser)

    with allure.step("Авторизация через UI"):
        base.login(login, home, email, password)
        home.wait_until_loaded()

    with allure.step('Ищем товар "шарф" и добавляем его в корзину'):
        home.search_by_button("шарф")
        product.add_product_to_cart()

    with allure.step("Проверка, что корзина через API содержит товар"):
        session = requests.Session()
        for c in browser.get_cookies():
            session.cookies.set(c['name'], c['value'], domain=c.get('domain'))

        response = session.get("https://api.kasta.ua/api/v2/basket")
        assert response.status_code == 200
        items = response.json().get("items", [])
        assert any(block.get("items") for block in items), "Корзина пуста после добавления товара через UI"

    with allure.step("Удаляем товар через UI"):
        cart.delete_one_product()
        assert cart.is_cart_empty(), "Корзина не пуста после удаления товара"