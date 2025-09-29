import pytest
import allure
from pages.home_page import HomePage
from selenium.webdriver.common.by import By

@pytest.mark.regression
@allure.feature("Поиск")
@allure.story("Негативный сценарий: пустой поиск")
def test_empty_search_validation_message(browser):
    home = HomePage(browser)

    with allure.step("Открываем главную страницу"):
        home.open_main_page()

    with allure.step("Нажимаем кнопку поиска с пустым полем"):
        search_input = browser.find_element(By.XPATH, "//input[@type='search']")
        search_button = browser.find_element(By.XPATH, "//button[@type='submit']")
        search_button.click()

    with allure.step("Проверяем встроенное сообщение браузера о пустом поле"):
        validation_msg = search_input.get_attribute("validationMessage")
        assert validation_msg == "Заполните это поле.", \
            f'Ожидали "Заполните это поле.", но получили "{validation_msg}"'