from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    locator_enter_email = (By.NAME, "email")
    locator_enter_password = (By.NAME, "password")
    locator_button_submit = (By.XPATH, "//button[@type='submit' and contains(@class, 'button--orange')]")

    def enter_email(self, email: str):
        self.safe_send_keys(self.locator_enter_email, email)

    def enter_password(self, password: str):
        self.safe_send_keys(self.locator_enter_password, password)

    def click_submit_button(self):
        self.safe_click(self.locator_button_submit)




