from pages.base_page import BasePage
from configs.config import BASE_URL
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
    locator_catalog = (By.XPATH, '//span[@class="menu__label"]')
    locator_catalog_odezhda = (By.XPATH, '(//a[@class="menu-vertical__link"])[1]')
    locator_profile = (By.XPATH, "//div[@id='hUser']")
    locator_search = (By.XPATH, "//input[@type='search']")
    locator_search_button = (By.XPATH, "//button[@type='submit']")


    def open_main_page(self):
        """Открываем главную страницу сайта"""
        self.open_url(BASE_URL)

    def open_catalog(self):
        """Открываем каталог"""
        self.click_clickable_element(self.locator_catalog)

    def click_odezhda_in_catalog(self):
        """Нажимаем категорию 'Одежда'"""
        self.click_clickable_element(self.locator_catalog_odezhda)

    def click_profile_on_main_page(self):
        """Нажимаем на иконку 'Профиль'"""
        self.click_clickable_element(self.locator_profile)

    def search_by_button(self, text: str):
        """ ВВодим текст в поиск и нажимаем кнопку поиска """
        self.send_keys_to_element(self.locator_search, text)
        self.click_clickable_element(self.locator_search_button)

    def wait_until_loaded(self):
        self.wait.until(EC.visibility_of_element_located(self.locator_search))


