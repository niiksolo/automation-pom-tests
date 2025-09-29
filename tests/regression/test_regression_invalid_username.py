import pytest
import allure
from pages.home_page import HomePage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

invalid_data = [
    ('', "Обов'язкове поле"),
    (123455678, 'Введiть коректні email чи телефон'),
    ('!@#$%$$%#', 'Введiть коректні email чи телефон'),
    ("' OR '1'='1", 'Введiть коректні email чи телефон')
]

@pytest.mark.regression
@pytest.mark.parametrize("username, expected_error", invalid_data)
@allure.feature("Авторизация")
@allure.story("Негативные сценарии ввода логина")

def test_invalid_login(browser,username, expected_error):
    home = HomePage(browser)
    login = LoginPage(browser)

    with allure.step("Открываем главную страницу"):
        home.open_main_page()

    with allure.step("Открываем профиль"):
        home.click_profile_on_main_page()

    with allure.step(f"Вводим некорректный логин: {username}"):
        login.enter_email(username)
        login.click_submit_button()

    with allure.step('Проверяем отображение ошибки'):
        locator = (By.XPATH, "//span[@class='t-12 t-red t-right']")
        element = login.is_element_visible(locator)
        assert expected_error in element.text
