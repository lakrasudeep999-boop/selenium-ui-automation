from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_login_and_add_product(driver):
    driver.get("https://saucedemo.com")

    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    # assert "inventory" in driver.current_url

    #validate inventory page
    #print(driver.current_url)
    assert inventory.is_inventory_page_loaded()

    #add product
    inventory.add_first_product_to_cart()