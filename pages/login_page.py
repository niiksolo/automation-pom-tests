from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import pytest

class LoginPage(BasePage):
    locator_enter_email = (By.XPATH, "//input[@name='email']")
    locator_enter_password = (By.XPATH, "//input[@name='password']")
    locator_button_submit = (By.XPATH, "//button[@type='submit' and contains(@class, 'button--orange')]")

    def enter_email(self, email: str):
        """Вводим email в поле авторизации"""
        self.send_keys_to_element(self.locator_enter_email, email)

    def enter_password(self, password: str):
        """Вводим пароль в поле авторизации"""
        self.send_keys_to_element(self.locator_enter_password, password)

    def click_submit_button(self):
        """Нажимаем кнопку 'Войти' при авторизации"""
        self.click_clickable_element(self.locator_button_submit)




