import time

from selenium import webdriver

from pages.base_page import Base
from pages.login_page import Login


class Test_Login:

    def test_01_verify_login_with_valid_creds(self,setup):
        self.driver= setup
        self.login = Login(self.driver)
        self.base = Base(self.driver)
        self.login.do_login("piyush.alphabin@gmail.com", "Piyush@123")
        time.sleep(2)
        expected_result = "All Files | Powered by Box"
        assert self.base.get_title() == expected_result


    def test_02_verify_login_with_invalid_creds(self,setup):
        self.driver = setup
        self.login = Login(self.driver)
        self.base = Base(self.driver)
        self.login.do_login("piyush.alphabin12@gmail.com", "Piyush")
        expected_result = "Invalid login credentials"
        assert self.base.get_text(self.login.invalid_creds) == expected_result

    def test_03_verify_login_with_invalid_email(self,setup):
        self.driver = setup
        self.login = Login(self.driver)
        self.base = Base(self.driver)
        self.login.do_login("piyush@gmail.com", "Piyush@123")
        expected_result = "Invalid login credentials"
        assert self.base.get_text(self.login.invalid_creds) == expected_result

    def test_04_verify_login_with_invalid_password(self,setup):
        self.driver = setup
        self.login = Login(self.driver)
        self.base = Base(self.driver)
        self.login.do_login("piyush.alphabin@gmail.com", "Piyush")
        expected_result = "Invalid login credentials"
        assert self.base.get_text(self.login.invalid_creds) == expected_result

        





