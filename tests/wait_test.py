import logging
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.mark.parametrize("username,password",[('standard_user','secret_sauce')
                                               ])
def test_login(driver,username,password):
    driver.get('https://www.saucedemo.com/')
    time.sleep(5)
    logging.info(f"Title: {driver.title}")


    driver.find_element(By.ID,"user-name").send_keys(username)
    driver.find_element(By.ID,"password").send_keys(password)
    driver.find_element(By.ID,"login-button").click()

    # explicit wait
    wait = WebDriverWait(driver, 10)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn_primary.btn_small.btn_inventory")))

    logo = driver.find_element(By.CLASS_NAME,"app_logo")
    logo.is_displayed()
    logo.text == "Swag Labs"
    logging.info(f"logo_title: {logo.text}")

    # Hard wait
    time.sleep(5)