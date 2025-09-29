from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    locator_add_product_to_cart_1 = (By.XPATH, "(//button[@type='submit']) [2]")
    locator_add_product_to_cart_2 = (By.XPATH, "(//button[@type='submit']) [3]")
    locator_sale_product = (By.XPATH, "//label[@data-value-id='divchatkam']")


    def add_product_to_cart(self):
        """Добавляем первый товар по списку в корзину"""
        self.click_clickable_element(self.locator_add_product_to_cart_1)

    def add_second_product_to_cart(self):
        """Добавляем второй товар по списку в корзину"""
        self.click_clickable_element(self.locator_add_product_to_cart_2)

    def select_sale_product(self):
        """Фильтруем товары по акции"""
        self.click_clickable_element(self.locator_sale_product)

