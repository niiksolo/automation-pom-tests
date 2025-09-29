from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open_url(self, url):
        self.driver.get(url)

    def send_keys_to_element(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def click_clickable_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def is_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_text_in_element(self, locator, text, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))

    def login(self, login_page, home_page, email, password):
        home_page.open_main_page()
        home_page.click_profile_on_main_page()
        login_page.enter_email(email)
        login_page.click_submit_button()
        login_page.enter_password(password)
        login_page.click_submit_button()










    def get_text_when_present(self, locator, timeout=10):
        for _ in range(3):
            try:
                element = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located(locator)
                )
                text = element.text.strip()
                if text:
                    return text
            except:
                continue
        raise Exception(f"Не удалось получить текст для элемента {locator}")