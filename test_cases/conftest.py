import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.base_page import Base
from pages.home_page import All_pages
from pages.login_page import Login


def pytest_addoption(parser):
    parser.addoption("--browser", action='store', default='chrome')

@pytest.fixture
def setup(request):
    browser = request.config.getoption('--browser')
    option = Options()
    option.add_argument("--incognito")
    # option.add_argument("--headless")
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        driver = webdriver.Chrome()

    driver.get("https://account.box.com/login")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.login = Login(driver)
    request.cls.base = Base(driver)
    request.cls.all_page = All_pages(driver)
    yield driver
    driver.quit()
    print("test")