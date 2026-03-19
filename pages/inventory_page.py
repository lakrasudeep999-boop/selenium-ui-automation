from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self,driver):
        self.driver = driver

    #locators
    inventory_container = (By.ID,"inventory_container")
    first_add_to_cart_button =(By.ID, "add-to-cart-sauce-labs-backpack")

    #methods
    def is_inventory_page_loaded(self):
        return self.driver.find_element(*self.inventory_container).is_displayed()

    def add_first_product_to_cart(self) :
        self.driver.find_element(*self.first_add_to_cart_button).click()
