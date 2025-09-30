from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class CartPage(BasePage):
    locator_delete_button = (By.CSS_SELECTOR, "div.ic.bin[role='button']")
    locator_empty_cart = (By.XPATH, "//div[text()='Товар видалено з кошику']")
    locator_cart_counter = (By.XPATH, "//div[contains(@class, 't-16 lh-22 expand')]")
    overlay_locator = (By.CSS_SELECTOR, "div.SbBg.cover")
    close_cart_button_locator = (By.CSS_SELECTOR, "button.close-cart")

    def wait_overlay_disappear(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(self.overlay_locator)
            )
        except TimeoutException:
            pass

    def close_cart(self):
        try:
            self.safe_click(self.close_cart_button_locator)
            self.wait_overlay_disappear()
        except:
            pass

    def get_cart_count(self) -> int:
        try:
            counter = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.locator_cart_counter)
            )
            import re
            match = re.search(r"\d+", counter.text)
            return int(match.group()) if match else 0
        except TimeoutException:
            return 0

    def delete_one_product(self):
        """Удаляем один товар из корзины стабильно"""
        try:
            self.safe_click(self.locator_delete_button)
        except TimeoutException:
            return


        self.wait_overlay_disappear()
        try:
            WebDriverWait(self.driver, 15).until(
                EC.invisibility_of_element_located(self.locator_delete_button)
            )
        except TimeoutException:
            pass  # если не исчезла — продолжаем

    def is_cart_empty(self) -> bool:
        """Проверка, что корзина пуста"""
        empty_text = len(self.driver.find_elements(*self.locator_empty_cart)) > 0
        no_delete_buttons = len(self.driver.find_elements(*self.locator_delete_button)) == 0
        return empty_text or no_delete_buttons

    def wait_cart_count(self, expected_count: int, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.locator_cart_counter, str(expected_count))
        )


