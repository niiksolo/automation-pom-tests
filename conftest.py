import pytest
from selenium import webdriver
import allure

@pytest.fixture()
def browser(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)

    yield driver

    if request.node.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(),
                      name="screenshot_on_failure",
                      attachment_type=allure.attachment_type.PNG)
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)