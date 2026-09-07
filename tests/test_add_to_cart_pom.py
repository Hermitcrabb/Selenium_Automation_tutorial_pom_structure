import logging
import time


from pages.inventory_page.inventorypage import InventoryPage
from pages.login_page.loginpage import LoginPage
from testdata.inventorydata import products
from testdata.logindata import users

def test_get_items(driver):
    # Login to the page
    login(driver)
    #Get the items and add to cart
    inventory_page = InventoryPage(driver)
    # assert inventory_page.get_page_logo().is_displayed()

    for product in products:

        logging.info(product["title"])
        inventory_page.add_to_cart(product["title"])


    inventory_page.open_cart()

    actual_products = inventory_page.get_cart_list()

    expected_products = [product["title"] for product in products]
    assert actual_products == expected_products

    logging.info(f"Assert: items_added{actual_products} = {expected_products}")

    inventory_page.open_checkout()
    inventory_page.set_first_name(users[1]["username"])
    inventory_page.set_last_name(users[1]["password"])
    inventory_page.set_postal_code("44600")
    inventory_page.click_continue()
    inventory_page.click_finish()

    time.sleep(2)






def login(driver):
    login_page = LoginPage(driver)
    driver.get(login_page.SYSTEM_URL)
    username = users[1]["username"]
    password = users[1]["password"]
    login_page.login(username,password)



# def check_product(driver):
#     inventory_page = InventoryPage(driver)
#     pass