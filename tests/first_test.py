import logging
import random
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.ui
def test_google_title(driver):
    driver.get('https://www.google.com')
    time.sleep(5)
    logging.info(f"Title: {driver.title}")


@pytest.mark.smoketest
def test_demo(driver):
    driver.get('https://www.saucedemo.com/')
    time.sleep(5)
    logging.info(f"Title: {driver.title}")
    element = driver.find_element(By.ID,"login_credentials")
    logindata= element.text.split("\n")
    logging.info(f"data_collected: {logindata}")

    element2 = driver.find_element(By.CLASS_NAME,"login_password")
    passdata = element2.text.split("\n")
    logging.info(f"data_collected: {passdata}")
    randomizer = random.randint(1,len(logindata)-1)
    driver.find_element(By.ID,"user-name").send_keys(logindata[randomizer])
    driver.find_element(By.ID,"password").send_keys(passdata[1])
    driver.find_element(By.ID,"login-button").click()
    time.sleep(5)







