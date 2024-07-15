import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import Base


class Login(Base):
    email = (By.ID, "login-email")
    next_btn = (By.ID, "login-submit")
    password = (By.ID, "password-login")
    log_in_button = (By.ID, "login-submit-password")
    after_login = (By.CSS_SELECTOR, '[aria-label="Box logo"]')
    invalid_creds = (By.CSS_SELECTOR, "[class='form-error']")

    def do_login(self, email, password):
        self.send_key(self.email, email)
        self.do_click(self.next_btn)
        self.send_key(self.password, password)
        self.do_click(self.log_in_button)
        time.sleep(2)



