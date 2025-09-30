from pages.base_page import BasePage
from configs.config import BASE_URL
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
    locator_catalog = (By.XPATH, '//span[@class="menu__label"]')
    locator_catalog_odezhda = (By.XPATH, '(//a[@class="menu-vertical__link"])[1]')
    locator_profile = (By.ID, 'hUser')
    locator_search = (By.XPATH, "//input[@type='search']")
    locator_search_button = (By.XPATH, "//button[@type='submit']")

    def open_main_page(self):
        self.open_url(BASE_URL)

    def open_catalog(self):
        self.safe_click(self.locator_catalog)

    def click_odezhda_in_catalog(self):
        self.safe_click(self.locator_catalog_odezhda)

    def click_profile_on_main_page(self):
        self.safe_click(self.locator_profile)

    def search_by_button(self, text: str):
        self.safe_send_keys(self.locator_search, text)
        self.safe_click(self.locator_search_button)
        self.wait_until_loaded()

    def wait_until_loaded(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(self.locator_search)
        )


