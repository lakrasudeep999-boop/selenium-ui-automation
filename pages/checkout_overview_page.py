from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutOverViewPage:
    def __init__(self,driver):
        self.driver = driver


    #locators

    title = (By.CLASS_NAME,"title")
    product_name = (By.CLASS_NAME,"inventory_item_name")
    product_price = (By.CLASS_NAME,"inventory_item_price")
    item_total = (By.CLASS_NAME,"summary_subtotal_label")
    tax = (By.CLASS_NAME,"summary_tax_label")
    total = (By.CLASS_NAME,"summary_total_label")
    finish_btn = (By.ID,"finish_btn")


    #wait for overview page

    def wait_for_overview_page(self):
        wait = WebDriverWait(self.driver, 10)

        wait.until(lambda d : "checkout-step-two" in d.current_url)
        wait.until(EC.visibility_of_element_located(self.title))

    #get summary

    def get_product_name(self):
        return self.driver.find_element(*self.product_name).text

    def get_product_price(self):
        price_text = self.driver.find_element(*self.product_price).text
        return float(price_text.replace("$", ""))

    def get_item_total(self):
        text = self.driver.find_element(*self.item_total).text
        return float(text.split("$")[1])

    def get_tax(self):
        text = self.driver.find_element(*self.tax).text
        return float(text.split("$")[1])

    def get_total(self):
        text = self.driver.find_element(*self.total).text
        return float(text.split("$")[1])

    def is_total_correct(self):
        item_total = self.get_item_total()
        tax = self.get_tax()
        total = self.get_total()

        return round(item_total + tax,2) == total

