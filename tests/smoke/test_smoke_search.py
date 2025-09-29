import pytest
import allure
from pages.home_page import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.smoke
@allure.feature("Поиск")
@allure.story("Поиск товара")
@allure.title("Поиск товара и проверка что нужный товар найден")

def test_search(browser):
    home = HomePage(browser)


    with allure.step("Открываем главную страницу"):
        home.open_main_page()

    with allure.step('Вводим текст в строку поиска и нажимаем кнопку поиска'):
        home.search_by_button("кепка")

    with allure.step("Проверяем, что найден хотя бы один товар с текстом 'кепка'"):
        locator = (By.XPATH, "//header[contains(@class, 'p__info_name') and contains(text(), 'кепка')]")
        elements = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located(locator))
        assert len(elements) > 0, "Товар 'кепка' не найден"