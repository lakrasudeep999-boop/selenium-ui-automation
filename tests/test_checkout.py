from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverViewPage
import logging


def test_checkout(checkout_page):
    driver = checkout_page

    assert "checkout-step-one" in driver.current_url

