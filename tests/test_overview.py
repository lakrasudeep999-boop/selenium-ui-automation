from pages.checkout_overview_page import CheckoutOverViewPage
from pages.checkout_page import CheckoutPage
import logging

from pages.checkout_page import CheckoutPage


def test_overview(checkout_overview_page):
    driver = checkout_overview_page


    overview =CheckoutOverViewPage(driver)
    checkout = CheckoutPage(driver)
    print(driver.current_url)
    assert overview.get_product_name() != ""
    assert overview.get_product_price() > 0
    assert overview.is_total_correct()

    overview.click_finish()
    overview.wait_for_success_page()

    assert overview.is_order_success()

    logging.info("Successfully ordered!!")
