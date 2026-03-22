from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self,driver):
        self.driver = driver

    #locators
    inventory_container = (By.ID,"inventory_container")
    first_add_to_cart_button =(By.ID, "add-to-cart-sauce-labs-backpack")


    #methods
    def wait_for_inventory_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.inventory_container)
        )

    def add_first_product_to_cart(self):
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable(self.first_add_to_cart_button))
        button.click()

