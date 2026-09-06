import time
from pages.basepage import BasePage
from pages.login_page.loginproperties import LoginProperties


class LoginPage(LoginProperties,BasePage):

    def login(self,username,password):
        # LOGIN ELEMENT USERNAME
        self.username_field.send_keys(username)
        # LOGIN ELEMENT PASSWORD
        self.password_field.send_keys(password)
        # LOGIN ELEMENT LOGIN BUTTON
        self.login_button.click()



