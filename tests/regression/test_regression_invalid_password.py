import pytest
import allure
from pages.home_page import HomePage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

invalid_data = [
    ('', ["Введіть", "пароль"]),
    (123455678, ["Введіть", "пароль"]),
    ('!@#$%$$%#', ["Введіть", "пароль"]),
    ("'OR '1'='1", ["пароль", "Невірно"])
]

@pytest.mark.regression
@pytest.mark.parametrize("password, expected_keywords", invalid_data)
@allure.feature("Авторизация")
@allure.story("Негативные сценарии ввода пароля")

def test_invalid_login(browser, password, expected_keywords):
    home = HomePage(browser)
    login = LoginPage(browser)

    with allure.step("Открываем главную страницу"):
        home.open_main_page()

    with allure.step("Открываем профиль"):
        home.click_profile_on_main_page()

    with allure.step("Вводим логин"):
        login.enter_email('my@email.com')
        login.click_submit_button()

    with allure.step(f"Вводим некорректный пароль: {password}"):
        login.enter_password(password)
        login.click_submit_button()

    with allure.step("Проверяем отображение ошибки"):
        locator = (By.XPATH, "//div[@class='auth_title']")
        error_text = login.get_text_when_present(locator)

        assert any(keyword in error_text for keyword in expected_keywords), \
            f'Ожидали хотя бы одно из ключевых слов {expected_keywords}, но получили "{error_text}"'
