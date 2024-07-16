from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.generate_log import LogGen

class Base:

    logs = LogGen.loggenerate()
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def do_click(self,by_locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(by_locator))
            element.click()
            self.logs.info(f"Clicked on element located by {by_locator}")
        except Exception as E:
            self.logs.error(f"Failed to click on element located by {by_locator}: {E}")
            raise

    def send_key(self,by_locator,data):
        try:
            element = self.wait.until(EC.visibility_of_element_located(by_locator))
            element.send_keys(data)
            self.logs.info(f"Sent keys '{data}' to element located by {by_locator}")
        except Exception as E:
            self.logs.error(f"Failed to send keys '{data}' to element located by {by_locator}: {E}")
            raise

    def get_text(self, by_locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(by_locator))
            text = element.text
            self.logs.info(f"Retrieved text '{text}' from element located by {by_locator}")
            return text
        except Exception as E:
            self.logs.error(f"Failed to get text from element located by {by_locator}: {E}")
            raise

    def get_title(self):
        try:
            title = self.driver.title
            self.logs.info(f"Retriveing the page {title}")
            return title
        except Exception as E:
            self.logs.error(f"Failed to get page title: {E}")
            raise

    def is_displayed(self, by_locator):
        try:
            elements = self.wait.until(EC.visibility_of_element_located(by_locator))
            displayed = elements.is_displayed()
            self.logs.info(f"Element located by {by_locator} is {'displayed' if displayed else 'not displayed'}")
            return displayed
        except Exception as E:
            self.logs.error(f"Failed to check if element located by {by_locator} is displayed: {E}")
            raise

    def drop_down(self,by_locator,visible_text):
        try:
            element = self.wait.until(EC.visibility_of_element_located(by_locator))
            select = Select(element)
            self.logs.info(f"Selected '{visible_text}' from dropdown located by {by_locator}")
            return select.select_by_visible_text(visible_text)
        except Exception as E:
            self.logs.error(f"Failed to select '{visible_text}' from dropdown located by {by_locator}: {E}")
            raise

    def assertion(self, actual_value, expected_value):
        try:
            assert actual_value == expected_value
            self.logs.info(f"Assertion passed: {actual_value} == {expected_value}")
        except Exception as E:
            self.logs.error(f"Assertion failed: {actual_value} == {expected_value}")

