import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import user_data
from pages.base_page import Base

class All_pages(Base):
    click_upload = (By.CSS_SELECTOR, "[class='menu-toggle']")
    click_on_file = (By.XPATH, "//span[text()='Upload File']")
    click_on_new = (By.CSS_SELECTOR, "[class='UnifiedNewDropdownMenuToggleButton-label']")
    click_on_folder = (By.XPATH, "//span[text()='Folder']")
    folder_name = (By.NAME, "folder-name")
    invite_additional_details = (By.CSS_SELECTOR, "[class='bdl-PillSelector-input pill-selector-input']")
    permission_drop_down = (By.NAME, "invite-permission")
    click_on_create_btn = (By.XPATH, "//div[@class='modal-actions']/button[2]")
    upload_notification = (By.XPATH, "//div[@class='notification info wrap notification-enter-done']/span")
    tooltip_user_create_folder_with_same_name = (By.CSS_SELECTOR, "[class='tooltip bdl-Tooltip is-error']")
    remove_folder = (By.CSS_SELECTOR, "[class='menu-item TrashMenuItem']")
    click_on_remove_ok_btn = (By.XPATH, "//span[text()='Okay']")
    after_remove_folder_pop_up = (By.XPATH, "//div[@class='notification info wrap']/span")


    def upload_file(self,folder_name,new_email,drop_down):
        self.do_click(self.click_on_new)
        self.do_click(self.click_on_folder)
        self.send_key(self.folder_name,folder_name)
        self.send_key(self.invite_additional_details, new_email)
        self.drop_down(self.permission_drop_down, drop_down)
        self.do_click(self.click_on_create_btn)
        time.sleep(4)

    def remove_folder(self):
        action = ActionChains(self.driver)
        folder_element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "(//a[@class='item-link item-link '])[1]")))
        action.context_click(folder_element).perform()
        action.send_keys(Keys.DOWN*2).perform()
        action.send_keys(Keys.ENTER).perform()
        time.sleep(3)
        # self.driver.find_element(self.click_on_remove_ok_btn).click()
        self.do_click(self.click_on_remove_ok_btn)
        time.sleep(3)


