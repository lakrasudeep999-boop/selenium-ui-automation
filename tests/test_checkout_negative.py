from pages.checkout_page import CheckoutPage
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
import logging
from config import BASE_URL,USERNAME,PASSWORD


def test_checkout_empty_first_name(driver):
    driver.get(BASE_URL)

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    #login
    login.login(USERNAME,PASSWORD)

    inventory.wait_for_inventory_page()

    #add product
    inventory.add_first_product_to_cart()

    #go to cart
    cart.open_cart()

    assert cart.is_cart_page_loaded()
    assert cart.is_product_added()

    #proceed to checkout
    cart.checkout_page()

    #leave first name empty
    checkout.fillout_form("","lakra",560043)
    checkout.click_continue()

    #validation
    error = checkout.get_error_message()

    assert "ERROR:" in error

    logging.info("First name empty")

