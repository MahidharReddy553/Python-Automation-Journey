from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.waits import *
from day_30_login_tests import *

with webdriver.Chrome() as driver:
    driver.get("https://www.saucedemo.com/")

    def add_single_product():
        login(driver, "standard_user", "secret_sauce")
        assert "inventory.html" in driver.current_url, "Product page is loaded"

        add_btn = wait_for_clickable(driver, (By.ID, "add-to-cart-sauce-labs-backpack"))
        add_btn.click()
        print("Added to cart successfully")

        cart_count = wait_for_visibility(driver, (By.CSS_SELECTOR, "#shopping_cart_container > a > span"))
        assert cart_count.text == "1", f"Expected cart count 1, got {cart_count.text}"
        print(cart_count.text)

    def add_mul_prods(*products):
        for product in products:
            product.click()
            print("Product added to cart successfully")
        wait_for_clickable(driver, (By.CLASS_NAME, "shopping_cart_link")).click()
        cart_items = wait_for_eles_visibility(driver, (By.CLASS_NAME, "cart_item"))
        assert len(cart_items) >= 1, f"Expected at least 1 item, got {len(cart_items)}"
        print(len(cart_items))

    def cart_validation():
        wait_for_clickable(driver, (By.CLASS_NAME, "shopping_cart_link"), 30).click()
        names = [name.text for name in wait_for_eles_visibility(driver, (By.CLASS_NAME, "inventory_item_name"))]
        prices = [price.text for price in wait_for_eles_visibility(driver, (By.CLASS_NAME, "inventory_item_price"))]
        cart_items = dict(zip(names, prices))
        print(cart_items)
        return cart_items

    def view_cart(cart):
        for i, j in enumerate(cart):
            print(i + 1, ':', j)

    def remove_product(cart, product_name):
        """Remove product by name using relative XPath instead of input()."""
        wait_for_clickable(driver, (By.CLASS_NAME, "shopping_cart_link")).click()
        remove_btn = driver.find_element(
            By.ID,
            "remove-"+product_name.lower().replace(' ', '-')
        )
        remove_btn.click()
        print(f"Product '{product_name}' removed successfully")
        wait_for_clickable(driver, (By.CLASS_NAME, "shopping_cart_link"), 30).click()
        driver.refresh()
        cart_validation()

    # Example run
    login(driver, "standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url, "Product page is loaded"

    add_mul_prods(
        wait_for_clickable(driver, (By.ID, "add-to-cart-sauce-labs-backpack")),
        wait_for_clickable(driver, (By.ID, "add-to-cart-sauce-labs-bike-light"))
    )

    cart = cart_validation()
    view_cart(cart)

    # Remove a product by name directly (no input())
    cart = remove_product(cart, "Sauce Labs Backpack")