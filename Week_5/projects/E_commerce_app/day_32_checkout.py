from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.waits import wait_for_visibility, wait_for_clickable
from utils.validations import validate_text
from utils.take_screenshot import take_screenshot
from day_30_login_tests import login


def checkout():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    try:
        login(driver, "standard_user", "secret_sauce")

        wait_for_clickable(driver, (By.ID, "add-to-cart-sauce-labs-backpack")).click()
        wait_for_clickable(driver, (By.CLASS_NAME, "shopping_cart_link")).click()

        wait_for_clickable(driver, (By.ID, "checkout")).click()
        driver.find_element(By.ID, "first-name").send_keys("Loki")
        driver.find_element(By.ID, "last-name").send_keys("Thor")
        driver.find_element(By.ID, "postal-code").send_keys("500004")
        driver.find_element(By.ID, "continue").click()

        products = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        for p, pr in zip(products, prices):
            print(f"{p.text} - {pr.text}")

        driver.find_element(By.ID, "finish").click()

        success_msg = wait_for_visibility(driver, (By.CLASS_NAME, "complete-header"))
        assert validate_text(success_msg.text, "Thank you for your order!"), "Error in order placement"

        take_screenshot(driver, "order_success")
    except Exception as e:
        print(e)
    finally:
        driver.quit()

checkout()
