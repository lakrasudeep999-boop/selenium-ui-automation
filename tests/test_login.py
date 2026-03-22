from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_add_product_to_cart(driver):

  driver.get("https://saucedemo.com")

  login = LoginPage(driver)
  inventory = InventoryPage(driver)
  cart = CartPage(driver)

  #login
  login.enter_username("standard_user")
  login.enter_password("secret_sauce")
  login.click_login()

  #explicit wait
  inventory.wait_for_inventory_page()

  #add item to cart
  inventory.add_first_product_to_cart()

  #cart
  cart.open_cart()

  assert cart.is_cart_page_loaded()
  assert cart.is_product_added()

  #proceed to checkout
  cart.checkout_page()


