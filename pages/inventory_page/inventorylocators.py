from selenium.webdriver.common.by import By


class InventoryLocators:
    SYSTEM_URL = "https://www.saucedemo.com/"
    APP_TITLE = (By.CLASS_NAME,"app_logo")
    INVENTORY_CONTAINER= (By.ID,"inventory_container")
    INVENTORY_CLASS = (By.CLASS_NAME,"inventory_list")
    INVENTORY_ITEM_NAME = (By.CLASS_NAME,"inventory_item_name")
    INVENTORY_ITEM_PRICE = (By.CLASS_NAME,"inventory_item_price")
    INVENTORY_DESCRIPTION = (By.CLASS_NAME,"inventory_item_description")
    CART_LINK = (By.CLASS_NAME,"shopping_cart_link")
    CART_ITEM = (By.CLASS_NAME,"cart_item")
    CHECKOUT = (By.ID,"checkout")
    FIRST_NAME = (By.ID,"first-name")
    LAST_NAME = (By.ID,"last-name")
    POSTAL_CODE = (By.ID,"postal-code")
    CONTINUE = (By.ID,"continue")
    FINISH = (By.ID,"finish")

    @staticmethod
    def ADD_TO_CART(element_name):
        element_name = element_name.lower().replace(" ","-")

        return (By.ID, f"add-to-cart-{element_name}")

