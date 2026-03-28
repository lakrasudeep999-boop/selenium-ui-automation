from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from config import BASE_URL
import logging


def test_cart(add_to_cart):

    driver = add_to_cart

    cart = CartPage(driver)
    cart.open_cart()

    assert cart.is_cart_page_loaded()
    assert cart.is_product_added()

    logging.info("Product added to cart")