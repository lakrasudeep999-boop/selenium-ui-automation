from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_overview_page import CheckoutOverViewPage
from config import BASE_URL,USERNAME,PASSWORD
import logging

def test_e2e(driver):

  driver.get(BASE_URL)

  login = LoginPage(driver)
  inventory = InventoryPage(driver)
  cart = CartPage(driver)
  checkout = CheckoutPage(driver)
  overview = CheckoutOverViewPage(driver)

  #login
  login.login(USERNAME,PASSWORD)

  #explicit wait
  inventory.wait_for_inventory_page()
  logging.info("successful login")


  #add item to cart
  inventory.add_first_product_to_cart()

  #cart
  cart.open_cart()

  assert cart.is_cart_page_loaded()
  assert cart.is_product_added()

  logging.info("successful added product to cart")

  #proceed to checkout
  cart.checkout_page()

  checkout.wait_for_checkout_page_ready()

  #fill form
  checkout.fillout_form("sudeep","lakra",560043)

  #continue
  checkout.click_continue_and_wait()


  print(driver.current_url)

  #validation
  assert checkout.is_checkout_overview_page()

  overview.wait_for_overview_page()

  #validating checkout summary

  print("Product:", overview.get_product_name())
  print("Price:", overview.get_product_price())

  assert overview.get_product_name() != ""
  assert overview.get_product_price() > 0
  assert overview.is_total_correct()

  #finish btn
  overview.click_finish()

  #wait for success page
  overview.wait_for_success_page()

  #validate success page
  assert overview.is_order_success()

  logging.info("successful order")
