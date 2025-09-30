import pytest
import allure
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

@pytest.mark.skipif(reason="Нестабильный тест из-за динамической анимации корзины (overlay), клики на второй товар часто перехватываются элементом")
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

    with allure.step('Ищем товар "корм" и добавляем первый товар в корзину'):
        home.search_by_button("корм")
        product.add_product_to_cart()
        cart.wait_overlay_disappear()
        cart.close_cart()
        cart.wait_overlay_disappear()

    with allure.step('Добавляем второй товар в корзину'):
        product.add_second_product_to_cart()
        cart.wait_overlay_disappear()

    with allure.step('Проверяем что товаров в корзине два'):
        count = cart.get_cart_count()
        assert count == 2, f"Ожидали товаров '2', но получили '{count}'"

    with allure.step('Удаляем один товар и проверяем, что остался один'):
        cart.delete_one_product()
        cart.wait_overlay_disappear()
        count = cart.get_cart_count()
        assert count == 1, f"Ожидали товаров '1', но получили '{count}'"