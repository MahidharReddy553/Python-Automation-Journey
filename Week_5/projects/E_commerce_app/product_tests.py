from selenium import webdriver
from selenium.webdriver.common.by import By
from day_30_login_tests import login
from utils.waits import wait_for_eles_visibility

with webdriver.Chrome() as driver:
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    def product_count():
        login(driver, "standard_user", "secret_sauce")
        inventory = wait_for_eles_visibility(driver, (By.CLASS_NAME, "inventory_item"))
        assert len(inventory) == 6, f"Expected number of products is 6, found {len(inventory)}"
        print("Inventory count is valid")
    def products_names():
        products = wait_for_eles_visibility(driver, (By.CLASS_NAME, "inventory_item_name"))
        products = [product.text for product in products]
        for product in products:
            print(product)
        return products
    
    def get_prices():
        prices = wait_for_eles_visibility(driver, (By.CLASS_NAME, "inventory_item_price"))
        prices = [price.text for price in prices]
        assert all(price.startswith("$") for price in prices), "Invalid price format"
        return prices
        
    product_count()

    def product_info():
        products = products_names()
        prices = get_prices()
        products_with_prices = dict(zip(products, prices))
        for n, p in products_with_prices.items():
            print(n, ":", p)
        return products_with_prices

    product_info()