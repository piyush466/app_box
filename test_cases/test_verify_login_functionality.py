import time
from test_cases.baseclass import BaseClass

class Test_Login(BaseClass):

    def test_01_verify_login_with_valid_creds(self):
        self.login.do_login("piyush.alphabin@gmail.com", "Piyush@123")
        time.sleep(8)
        expected_result = "All Files | Powered by Box"
        assert self.base.get_title() == expected_result

    def test_02_verify_login_with_invalid_creds(self):
        self.login.do_login("piyush.alphabin12@gmail.com", "Piyush")
        expected_result = "Invalid captcha response. Please try again."
        assert self.base.get_text(self.login.invalid_creds) == expected_result

    def test_03_verify_login_with_invalid_email(self):
        self.login.do_login("piyush@gmail.com", "Piyush@123")
        expected_result = "Invalid captcha response. Please try again."
        assert self.base.get_text(self.login.invalid_creds) == expected_result

    def test_04_verify_login_with_invalid_password(self):
        self.login.do_login("piyush.alphabin@gmail.com", "Piyush")
        expected_result = "Invalid Login Credentials"
        assert self.base.get_text(self.login.invalid_creds) == expected_result







