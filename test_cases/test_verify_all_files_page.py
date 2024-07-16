import random
import string
import time
from test_cases.baseclass import BaseClass

class Test_All_page(BaseClass):

    random_char = random.choice(string.ascii_lowercase)
    email = "piyush" + random_char
    folders_name = email
    email = "piyush@gmail.com"
    drop_down = "Editor"

    def test_01_user_can_create_folder(self):
        self.login.do_login("piyush.alphabin@gmail.com", "Piyush@123")
        self.all_page.upload_file(self.folders_name, self.email, self.drop_down)
        Expected_result = f'"{self.folders_name}" was created successfully.'
        assert self.base.get_text(self.all_page.upload_notification) in Expected_result

    def test_02_user_can_create_same_name_folder(self):
        folder_name = "piyush02"
        self.login.do_login("piyush.alphabin@gmail.com", "Piyush@123")
        self.all_page.upload_file(folder_name, self.email, self.drop_down)
        Expected_result = "Sorry, but a folder with that name already exists."
        assert self.base.get_text(self.all_page.tooltip_user_create_folder_with_same_name) == Expected_result

    def test_03_user_can_remove_the_folder(self):
        folders_name = "test"
        self.login.do_login("piyush.alphabin@gmail.com", "Piyush@123")
        self.all_page.upload_file(folders_name, self.email, self.drop_down)
        self.all_page.remove_folder()
        Expected_result = "Item successfully moved to trash."
        assert self.base.get_text(self.all_page.after_remove_folder_pop_up) == Expected_result








