from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.waits import wait_for_visibility, wait_for_clickable, wait_for_eles_visibility
from utils.validations import validate_text
from utils.take_screenshot import take_screenshot
from day_30_login_tests import login
import logging

# logging.basicConfig(filename="logs/automation.log", level=logging.INFO)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/automation.log"),  # Save logs to file
        logging.StreamHandler()                  # Print logs to console
    ]
)

def e2e_flow():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    try:
        logging.info("Login Started")
        if login(driver, "standard_user", "secret_sauce"):
            logging.info("Login Successful")
        else:
            logging.info("Login Failed")

        products = wait_for_eles_visibility(driver, (By.CLASS_NAME, "inventory_item_name"))
        assert len(products) == 6
        logging.info("Products Validated")

        wait_for_clickable(driver, (By.ID, "add-to-cart-sauce-labs-backpack")).click()
        wait_for_clickable(driver, (By.ID, "add-to-cart-sauce-labs-bike-light")).click()
        wait_for_clickable(driver, (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")).click()
        logging.info("Products Added")

        wait_for_clickable(driver, (By.CLASS_NAME, "shopping_cart_link")).click()
        cart_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        for item in cart_items:
            print(item.text)
        logging.info("Cart Validated")
        take_screenshot(driver, "screenshots/cart_page.png")

     
        wait_for_clickable(driver, (By.ID, "checkout")).click()
        driver.find_element(By.ID, "first-name").send_keys("Loki")
        driver.find_element(By.ID, "last-name").send_keys("Asgard")
        driver.find_element(By.ID, "postal-code").send_keys("500004")
        wait_for_clickable(driver, (By.ID, "continue")).click()
        logging.info("Checkout Started")

        prods = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        for p, pr in zip(prods, prices):
            print(f"{p.text} - {pr.text}")

        
        wait_for_clickable(driver, (By.ID, "finish")).click()
        success_msg = wait_for_visibility(driver, (By.CLASS_NAME, "complete-header"))
        validate_text(success_msg.text, "Thank you for your order!")
        logging.info("Order Completed")

        take_screenshot(driver, "e-2-e_order_success")

        wait_for_clickable(driver, (By.CSS_SELECTOR, "#react-burger-menu-btn")).click()
        wait_for_clickable(driver, (By.ID, "logout_sidebar_link")).click()
        logging.info("Logout Successful")

    except Exception as e:
        print(e)

    finally:
        driver.quit()

e2e_flow()
