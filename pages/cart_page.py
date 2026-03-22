from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class CartPage:
    def __init__(self,driver):
        self.driver = driver

    #locator
    cart_icon = (By.CSS_SELECTOR,"a.shopping_cart_link")
    cart_item = (By.CLASS_NAME,"inventory_item_name")
    checkout_btn = (By.ID,"checkout")
    cart_title = (By.CLASS_NAME,"title")

    #method
    def open_cart(self):
        wait = WebDriverWait(self.driver, 10)

        element = wait.until(EC.presence_of_element_located(self.cart_icon))

        # force real browser click
        self.driver.execute_script("arguments[0].click();", element)

        wait.until(lambda d: "cart" in d.current_url)

    def is_cart_page_loaded(self):
        return "cart" in self.driver.current_url

    def is_product_added(self):
        return len(self.driver.find_elements(*self.cart_item))>0

    def checkout_page(self):
        wait = WebDriverWait(self.driver, 10)

        element = wait.until(EC.presence_of_element_located(self.checkout_btn))
        self.driver.execute_script("arguments[0].click();", element)

        wait.until(lambda d: "checkout" in d.current_url)


