from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    SYSTEM_URL = "https://www.saucedemo.com/"

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)