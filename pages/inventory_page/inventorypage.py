import logging

from pages.basepage import BasePage
from pages.inventory_page.inventorylocators import InventoryLocators
from pages.inventory_page.inventoryproperties import InventoryProperties




class InventoryPage(InventoryProperties,BasePage):

    def get_page_logo(self):
        title = self.logo
        return title


    def get_item_name(self):
        return self.item_name

    def get_item_price(self):
        return self.item_price

    def get_item_description(self):
        return self.item_description


    def get_items(self):
        parent_element = self.get_item_description()

        item_list = []
        for parent in parent_element:
            item_name = parent.find_element(
                *InventoryLocators.INVENTORY_ITEM_NAME
            )

            item_price = parent.find_element(
                *InventoryLocators.INVENTORY_ITEM_PRICE
            )
            item_list.append({
                "title":item_name.text,
                "price":item_price.text
            })
        return item_list

    def add_to_cart(self,element_title):
        locator = InventoryLocators.ADD_TO_CART(element_title)

        logging.info(f"Adding product: {element_title}")
        logging.info(f"Using locator: {locator}")

        button = self.driver.find_element(*locator)

        logging.info(f"Button found: {button.get_attribute('id')}")
        button.click()


    def open_cart(self):
        self.cart_link.click()

    def get_cart_list(self):
        cart_list = []
        parent_element = self.cart_list
        for parent in parent_element:
            item_name = parent.find_element(
                *InventoryLocators.INVENTORY_ITEM_NAME
            )
            cart_list.append(item_name.text)
        return cart_list

    def open_checkout(self):
        self.checkout_link.click()

    def set_first_name(self,username):
        self.checkout_first_name.send_keys(username)

    def set_last_name(self,last_name):
        self.checkout_last_name.send_keys(last_name)

    def set_postal_code(self,postal_code):
        self.checkout_postal.send_keys(postal_code)

    def click_continue(self):
        self.checkout_continue.click()

    def click_finish(self):
        self.page_finish.click()

