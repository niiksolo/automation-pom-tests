from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.product_page import ProductPage
from pages.home_page import HomePage
import pytest
import allure


@pytest.mark.smoke
@allure.feature("Корзина")
@allure.story("Добавление товара")
@allure.title("Добавление товара в корзину и проверка что товар добавлен")

def test_add_to_cart(browser):
    home = HomePage(browser)
    product = ProductPage(browser)
    cart = CartPage(browser)

    with allure.step("Открываем главную страницу"):
        home.open_main_page()

    with allure.step('Вводим текст в строку поиска и нажимаем кнопку поиска'):
        home.search_by_button("кепка")

    with allure.step('Добавляем в корзину товар'):
        product.add_product_to_cart()

    with allure.step('Проверяем что в корзине добавился товар'):
        count = cart.get_cart_count()

    with allure.step('Проверяем что в корзине 1 товар'):
        assert count == 1, f"Ожидали 1 товар, но в корзине {count}"



