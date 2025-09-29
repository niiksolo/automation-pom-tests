import pytest
import allure
from pages.home_page import HomePage

@pytest.mark.smoke
@allure.feature("Каталог")
@allure.story("Одежда")
@allure.title("Проверка открытия категории 'Одежда' из каталога")

def test_open_catalog_odezhda(browser):
    home = HomePage(browser)

    with allure.step("Открываем главную страницу"):
        home.open_main_page()

    with allure.step("Открываем каталог"):
        home.open_catalog()

    with allure.step("Кликаем по категории 'Одежда'"):
        home.click_odezhda_in_catalog()

    with allure.step("Проверяем, что перешли на нужную страницу"):
        assert "odezhda" in browser.current_url.lower(), \
            f"Ожидали 'odezhda' в URL, получили: {browser.current_url}"
