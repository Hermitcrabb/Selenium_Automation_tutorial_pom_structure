from pages.login_page.loginlocator import LoginLocator


class LoginProperties:

    @property
    def username_field(self):
        return self.driver.find_element(*LoginLocator.USERNAME_FIELD)


    @property
    def password_field(self):
        return self.driver.find_element(*LoginLocator.PASSWORD_FIELD)


    @property
    def login_button(self):
        return self.driver.find_element(*LoginLocator.LOGIN_BUTTON)

