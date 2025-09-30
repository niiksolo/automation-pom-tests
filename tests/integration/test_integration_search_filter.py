import pytest
import requests
import allure
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.base_page import BasePage
from pages.login_page import LoginPage
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()
email = os.getenv('SITE_LOGIN')
password = os.getenv('SITE_PASSWORD')

skip_on_ci = os.getenv("CI") == "true"

@pytest.mark.skipif(True, reason="Тест нестабильный в CI")
@pytest.mark.integration
@allure.feature("Поиск")
@allure.story("UI → API проверка поиска")
@allure.title("Поиск товара, применение фильтра и проверка HTML ответа")
def test_search_filter_ui_api(browser):
    base = BasePage(browser)
    home = HomePage(browser)
    login = LoginPage(browser)
    product = ProductPage(browser)

    with allure.step("Авторизация через UI"):
        base.login(login, home, email, password)
        home.wait_until_loaded()

    with allure.step('Вводим текст в строку поиска и нажимаем кнопку поиска'):
        home.search_by_button("юбка")
        product.select_sale_product()

    with allure.step("Проверка фильтра через HTML ответа"):
        session = requests.Session()
        for c in browser.get_cookies():
            session.cookies.set(c['name'], c['value'], domain=c.get('domain'))


        response = session.get('https://kasta.ua/uk/search/?q=%D1%8E%D0%B1%D0%BA%D0%B0&affiliation=divchatkam')
        assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"

        soup = BeautifulSoup(response.text, 'html.parser')
        active_filter = soup.select_one("label input[name='affiliation'][value='divchatkam'][checked]")
        assert active_filter is not None, "Фильтр 'Дивчаткам' не активен или не найден"
