import logging

from selenium.webdriver.common.by import By
from conftest import driver

class AddToCart:

    ADD_TO_CART = []
    def __init__(self,driver):
        self.driver = driver

    def get_items(self):
        parent_element = self.driver.find_elements(*self.INVENTORY_DESCRIPTION)

        item_list = []
        for parent in parent_element:
            item_pair = []
            item_name = parent.find_element(*self.INVENTORY_ITEM_NAME)
            item_price = parent.find_element(*self.INVENTORY_ITEM_PRICE)
            item_pair.append(item_name.text.lower().replace(" ","-"))
            item_pair.append(item_price.text)
            item_list.append(item_pair)

        return item_list
        # for item in items:
        #     item_name.append(item.text)



