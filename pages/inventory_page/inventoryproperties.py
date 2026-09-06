from pages.inventory_page.inventorylocators import InventoryLocators


class InventoryProperties:

    @property
    def logo(self):
        return self.driver.find_element(*InventoryLocators.APP_TITLE)

    @property
    def item_description(self):
         return self.driver.find_elements(*InventoryLocators.INVENTORY_DESCRIPTION)


    @property
    def item_name(self):
        return self.driver.find_element(*InventoryLocators.INVENTORY_ITEM_NAME)

    @property
    def item_price(self):
        return self.driver.find_element(*InventoryLocators.INVENTORY_ITEM_PRICE)

    @property
    def cart_link(self):
        return self.driver.find_element(*InventoryLocators.CART_LINK)

    @property
    def cart_list(self):
        return self.driver.find_elements(*InventoryLocators.CART_ITEM)

    @property
    def checkout_link(self):
        return self.driver.find_element(*InventoryLocators.CHECKOUT)

    @property
    def checkout_first_name(self):
        return self.driver.find_element(*InventoryLocators.FIRST_NAME)

    @property
    def checkout_last_name(self):
        return self.driver.find_element(*InventoryLocators.LAST_NAME)

    @property
    def checkout_postal(self):
        return self.driver.find_element(*InventoryLocators.POSTAL_CODE)
    @property
    def checkout_continue(self):
        return self.driver.find_element(*InventoryLocators.CONTINUE)

    # @property
    # def checkout_total(self):
    #     pass

    @property
    def page_finish(self):
        return self.driver.find_element(*InventoryLocators.FINISH)

