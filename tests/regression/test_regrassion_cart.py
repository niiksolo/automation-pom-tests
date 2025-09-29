from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.product_page import ProductPage
from pages.home_page import HomePage
import pytest
import allure

@pytest.mark.regression
@allure.feature("Корзина")
@allure.story("Добавление и удаление товаров")
@allure.title("Добавление нескольких товаров и удаление одного из них")

def test_add_two_products_and_delete_one(browser):
    home = HomePage(browser)
    cart = CartPage(browser)
    product = ProductPage(browser)

    with allure.step("Открываем главную страницу"):
        home.open_main_page()

    with allure.step('Вводим текст "корм" в строку поиска: и нажимаем кнопку поиска'):
        home.search_by_button("корм")

    with allure.step('Добавляем первый товар в корзину и закрываем ее'):
        product.add_product_to_cart()
        cart.close_cart()

    with allure.step('Добавляем второй товар в корзину и закрываем ее'):
        product.add_second_product_to_cart()

    with allure.step('Проверяем что товаров в корзине два'):
        text = cart.wait_cart_counter('2')
        assert '2' in text, f"Ожидали товаров '2' но получили '{text}'"

    with allure.step('Удаляем один товар с корзины и проверяем что товар остался один'):
        cart.delete_one_product()
        text = cart.wait_cart_counter('1')
        assert '1' in text, f"Ожидали товаров '1' но получили '{text}'"
