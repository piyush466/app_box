import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.base_page import Base
from pages.home_page import All_pages
from pages.login_page import Login

@pytest.fixture
def setup(request):
    option = Options()
    option.add_argument("--incognito")
    option.add_argument("--headless")
    driver = webdriver.Chrome(options=option)
    driver.get("https://account.box.com/login")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.login = Login(driver)
    request.cls.base = Base(driver)
    request.cls.all_page = All_pages(driver)
    yield driver
    driver.quit()