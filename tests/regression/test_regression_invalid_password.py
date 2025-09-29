import pytest
import allure
from pages.home_page import HomePage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

invalid_data = [
    ('', ["Обов'язкове", "Введіть", "пароль", "Невірно"]),
    (123455678, ["Обов'язкове", "Введіть", "пароль", "Невірно"]),
    ('!@#$%$$%#', ["Обов'язкове", "Введіть", "пароль", "Невірно"]),
    ("'OR '1'='1", ["Обов'язкове", "Введіть", "пароль", "Невірно"])
]
@pytest.mark.skip(reason="Сложно ловить ошибки пароля, временно пропускаем")
@pytest.mark.regression
@pytest.mark.parametrize("password, expected_error", invalid_data)
@allure.feature("Авторизация")
@allure.story("Негативные сценарии ввода пароля")

def test_invalid_login(browser,password, expected_error):
    home = HomePage(browser)
    login = LoginPage(browser)

    with allure.step("Открываем главную страницу"):
        home.open_main_page()

    with allure.step("Открываем профиль"):
        home.click_profile_on_main_page()

    with allure.step(f"Вводим логин"):
        login.enter_email('my@email.com')
        login.click_submit_button()

    with allure.step(f"Вводим некорректный пароль: {password}"):
        login.enter_password(password)
        login.click_submit_button()

    with allure.step("Проверяем отображение ошибки"):
        locator = (By.XPATH, "//div[@class='auth_title']")
        error_text = login.get_text_when_present(locator)
        expected_keywords = ["Обов'язкове", "Введіть", "пароль", "Невірно"]
        assert all(keyword in error_text for keyword in expected_keywords), \
            f'Ожидали все ключевые слова {expected_keywords}, но получили "{error_text}"'
