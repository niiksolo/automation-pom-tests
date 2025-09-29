import pytest
from pages.home_page import HomePage
from pages.base_page import BasePage
from pages.login_page import LoginPage
import os
import allure
from dotenv import load_dotenv
from selenium.webdriver.common.by import By


load_dotenv()
email = os.getenv("SITE_LOGIN")
password = os.getenv("SITE_PASSWORD")

@pytest.mark.smoke
@allure.feature("Авторизация")
@allure.story("Вход в аккаунт")
@allure.title("Проверка успешного входа в профиль через поп-ап")

def test_successful_login(browser):
    login = LoginPage(browser)
    home = HomePage(browser)

    with allure.step("Открываем главную страницу"):
        home.open_main_page()

    with allure.step("Открываем профиль"):
        home.click_profile_on_main_page()

    with allure.step('Вводим E-mail'):
        login.enter_email(email)
    with allure.step('Нажимаем кнопку "Войти"'):
        login.click_submit_button()

    with allure.step('Вводим пароль'):
        login.enter_password(password)
    with allure.step('Нажимаем кнопку "Войти"'):
        login.click_submit_button()

    with allure.step("Проверяем, что вход успешен"):
        locator = (By.XPATH, "//span[text()='Приємних покупок!']")
        success_message = home.is_element_visible(locator)
        assert success_message.is_displayed(), "Вход не разрешен"




