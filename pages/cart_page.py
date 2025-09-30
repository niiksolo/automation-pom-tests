from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class CartPage(BasePage):
    # Локаторы
    locator_delete_button = (By.CSS_SELECTOR, "div.ic.bin[role='button']")  # кнопка удаления товара
    locator_empty_cart = (By.XPATH, "//div[text()='Товар видалено з кошику']")  # надпись о пустой корзине
    locator_cart_counter = (By.XPATH, "//div[contains(@class, 't-16 lh-22 expand')]")  # счётчик товаров

    def delete_one_product(self):
        """
        Удаляем один товар из корзины и ждём, пока корзина обновится:
        либо появится надпись о пустой корзине,
        либо исчезнет кнопка удаления.
        """
        # Ждём пока кнопка удаления станет кликабельной
        delete_btn = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.locator_delete_button)
        )
        delete_btn.click()

        # Ждём, пока корзина обновится
        WebDriverWait(self.driver, 15).until(
            lambda d: len(d.find_elements(*self.locator_empty_cart)) > 0
                      or len(d.find_elements(*self.locator_delete_button)) == 0
        )

    def is_cart_empty(self) -> bool:
        """Проверяем, что корзина пуста"""
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.locator_empty_cart)
            )
            return True
        except TimeoutException:
            return False

    def get_cart_count(self) -> int:
        """Возвращаем количество товаров в корзине"""
        try:
            counter = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.locator_cart_counter)
            )
            return int(counter.text)
        except TimeoutException:
            return 0



