import logging
import time

from pages.inventory_page.inventorypage import InventoryPage
import pytest
from testdata.logindata import users
from pages.login_page.loginpage import LoginPage


def test_login_flow(driver):
    login_page = LoginPage(driver)
    driver.get(login_page.SYSTEM_URL)
    username = users[1]["username"]
    password = users[1]["password"]
    login_page.login(username,password)
    # dont add the action step in

    title_page = InventoryPage(driver)
    logo = title_page.get_page_logo()
    assert logo == "Swag Labs"
    logging.info(f"Logo text: {logo}")


