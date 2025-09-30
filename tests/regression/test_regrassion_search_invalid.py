import pytest
import allure
from pages.home_page import HomePage
from selenium.webdriver.common.by import By

invalid_data = [
    ("гадюкагабонская"),
    (123123123123),
    ('!@#$%$$%#')
]

@pytest.mark.regression
@pytest.mark.parametrize("product", invalid_data)
@allure.feature("Поиск")
@allure.story("Негативные проверки")
@allure.title("Негативные проверки поиска товаров")

def test_search_invalid(browser, product):
    home = HomePage(browser)

    with allure.step("Открываем главную страницу"):
        home.open_main_page()

    with allure.step(f'Вводим текст в строку поиска: "{product}" и нажимаем кнопку поиска'):
        home.search_by_button(product)

    with allure.step("Проверяем сообщение о том, что ничего не найдено"):
        locator = (By.XPATH, "//span[contains(@class,'empty-search__title')]")
        message_element = home.is_element_visible(locator)
        actual_message = message_element.text.strip()
        assert "ничего не найдено" in actual_message, \
            f'Ожидали сообщение про "ничего не найдено", но получили "{actual_message}"'