import pytest
from selenium import webdriver

from pages.base_page import Base
from pages.home_page import All_pages
from pages.login_page import Login


@pytest.fixture
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://account.box.com/login")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.login = Login(driver)
    request.cls.base = Base(driver)
    request.cls.all_page = All_pages(driver)
    return driver