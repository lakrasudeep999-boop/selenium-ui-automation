from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver


    #locators
    first_name = (By.ID,"first-name")
    last_name = (By.ID,"last-name")
    postal_code = (By.ID,"postal-code")
    continue_btn = (By.ID,"continue")
    overview_title = (By.CLASS_NAME,"title")
    error_msg = (By.CLASS_NAME,"error-message-container")
    cart_title = (By.CLASS_NAME,"title")

    #methods

    def wait_for_checkout_page_ready(self):
        wait = WebDriverWait(self.driver, 10)
        # wait for URL
        wait.until(lambda d: "checkout-step-one" in d.current_url)
        # wait for page title (VERY IMPORTANT)
        wait.until(EC.text_to_be_present_in_element(self.cart_title, "Checkout"))
        # wait for input to be interactable
        wait.until(EC.element_to_be_clickable(self.first_name))

    def fillout_form(self,fname,lname,zip_code):
        wait = WebDriverWait(self.driver, 10)

        wait.until(lambda d: "checkout-step-one" in d.current_url)

        first = self.driver.find_element(*self.first_name)
        last = self.driver.find_element(*self.last_name)
        zipc = self.driver.find_element(*self.postal_code)

        # FULL JS injection (with React-style events)
        self.driver.execute_script("""
                function setNativeValue(element, value) {
                    const valueSetter = Object.getOwnPropertyDescriptor(element.__proto__, 'value').set;
                    valueSetter.call(element, value);

                    element.dispatchEvent(new Event('input', { bubbles: true }));
                    element.dispatchEvent(new Event('change', { bubbles: true }));
                    element.dispatchEvent(new Event('blur', { bubbles: true }));
                }

                setNativeValue(arguments[0], arguments[1]);
                setNativeValue(arguments[2], arguments[3]);
                setNativeValue(arguments[4], arguments[5]);

            """, first, fname, last, lname, zipc, zip_code)

        # DEBUG
        print("FN:", first.get_attribute("value"))
        print("LN:", last.get_attribute("value"))
        print("ZIP:", zipc.get_attribute("value"))



    def click_continue_and_wait(self):
        wait = WebDriverWait(self.driver, 10)

        btn = wait.until(EC.element_to_be_clickable(self.continue_btn))
        self.driver.execute_script("arguments[0].click();", btn)

        wait.until(EC.visibility_of_element_located(self.overview_title))

    def click_continue(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(self.continue_btn))

        # use JS click
        self.driver.execute_script("arguments[0].click();", element)


    def is_checkout_overview_page(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(lambda  d: "checkout-step-two" in d.current_url)
        return "checkout-step-two" in self.driver.current_url

    def get_error_message(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(self.error_msg))
        return element.text