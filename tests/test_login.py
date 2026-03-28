from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config import BASE_URL, USERNAME, PASSWORD
import logging

def test_login(driver):
    driver.get(BASE_URL)
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    #login
    login.login("standard_user","secret_sauce")

    #wait for inventory page
    inventory.wait_for_inventory_page()

    assert "inventory" in driver.current_url

    #logs
    logging.info("Login Successful")
