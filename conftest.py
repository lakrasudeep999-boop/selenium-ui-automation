import pytest
import logging
import time

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.cart_page import  CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverViewPage
from utils.driver_setup import get_driver
from config import BASE_URL,USERNAME,PASSWORD


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    driver.get(BASE_URL)

    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.login(USERNAME,PASSWORD)
    inventory.wait_for_inventory_page()
    return driver

@pytest.fixture
def add_to_cart(login):
    driver = login
    inventory = InventoryPage(driver)

    inventory.add_first_product_to_cart()

    return driver

@pytest.fixture
def cart_page(add_to_cart):
    driver = add_to_cart

    cart = CartPage(driver)
    cart.open_cart()
    return driver

@pytest.fixture
def checkout_page(cart_page):
    driver = cart_page
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    cart.checkout_page()
    checkout.wait_for_checkout_page_ready() #checkout-step-one
    return driver

@pytest.fixture
def checkout_overview_page(checkout_page):
    driver = checkout_page
    checkout = CheckoutPage(driver)
    overview = CheckoutOverViewPage(driver)

    checkout.fillout_form("sudeep","lakra",560043)
    checkout.click_continue_and_wait()
    overview.wait_for_overview_page() #checkout-step-two
    return driver



logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    report = outcome.get_result()

    #execute only after test call
    if report.when == 'call' and report.failed:

        driver = item.funcargs.get("driver")

        if driver:
            file_name = f"screenshots/failure_{int(time.time())}.png"
            driver.save_screenshot(file_name)


