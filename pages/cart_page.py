from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage(BasePage):
    locator_cart_count_one_product = (By.XPATH, "//span[@class='t-center t-14 lh-20']")
    locator_delete_one_product = (By.XPATH, "//div[contains(@ts-target, '#cartContent')] [1]")
    locator_close_cart = (By.XPATH, "//ic[contains(@class, 'popup-close absolute left-0 h-100')]")
    locator_cart_counter = (By.XPATH, "//div[contains(@class, 't-16 lh-22 expand')]")
    locator_cart_is_empty = (By.XPATH, "//div[text()='Товар видалено з кошику']")

    def get_cart_count_one_product(self):
        """Проверяем что в корзине добавился товар и возвращаем текст"""
        element = self.is_element_visible(self.locator_cart_count_one_product)
        return element.text

    def close_cart(self):
        """Закрытие корзины"""
        self.click_clickable_element(self.locator_close_cart)

    def delete_one_product(self):
        """Удалить один товар из корзины"""
        self.safe_action(lambda: self.click_clickable_element(self.locator_delete_one_product))

    def check_count_cart_several_product(self):
        """Посмотреть сколько товаров всего в корзине"""
        element = self.is_element_visible(self.locator_cart_counter)
        return element.text

    def wait_cart_counter(self, expected_count: str, timeout=10):
        """Ждём пока счётчик корзины покажет нужное количество товаров"""
        self.wait_text_in_element(self.locator_cart_counter,expected_count,timeout=10)
        return self.driver.find_element(*self.locator_cart_counter).text

    def is_cart_empty(self, timeout=5) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(self.locator_cart_is_empty)
            )
            return False
        except:
            return True

