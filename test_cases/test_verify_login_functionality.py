import pytest

from Utilities.generate_log import LogGen
from test_cases.baseclass import BaseClass

class Test_Login(BaseClass):
    logs = LogGen.loggenerate()
    @pytest.mark.smoke
    def test_01_verify_login_with_valid_creds(self):
        self.login.do_login("piyush.alphabin@gmail.com", "Piyush@123")
        self.base.assertion(self.base.get_title(), "All Files | Powered by Box")


    def test_02_verify_login_with_invalid_creds(self):
        self.login.do_login("piyush.alphabin12@gmail.com", "Piyush")
        self.base.assertion(self.base.get_text(self.login.invalid_creds), "Invalid captcha response. Please try again.")

    @pytest.mark.smoke
    def test_03_verify_login_with_invalid_email(self):
        self.login.do_login("piyush@gmail.com", "Piyush@123")
        self.base.assertion(self.base.get_text(self.login.invalid_creds), "Invalid captcha response. Please try again.")

    @pytest.mark.smoke
    def test_04_verify_login_with_invalid_password(self):
        self.login.do_login("piyush.alphabin@gmail.com", "Piyush")
        self.base.assertion(self.base.get_text(self.login.invalid_creds), "Invalid captcha response. Please try again.")

    def test_05_verify_user_can_do_logout(self):
        self.logs.info("****test_05_verify_user_can_do_logout****")
        self.login.do_login("piyush.alphabin@gmail.com", "Piyush@123")
        print("After login: ",self.base.get_title())
        self.base.assertion(self.base.get_title(), "All Files | Powered by Box")
        self.all_page.click_on_logout_button()
        print("After logout: ", self.base.get_title())
        self.base.assertion(self.base.get_title(), "Box | Login")










