from selenium import webdriver
from pages.login_page import LoginPage


def test_login():
    driver = webdriver.Chrome()
    driver.get("https://saucedemo.com")

    login = LoginPage(driver)

    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    assert "inventory" in driver.current_url

    driver.quit()
