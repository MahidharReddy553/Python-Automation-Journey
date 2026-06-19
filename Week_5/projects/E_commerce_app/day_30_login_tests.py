from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from utils import wait_for_visibility, wait_for_clickable, validate_url, take_screenshot, validate_text

def login(driver, username, password):
    driver.get("https://www.saucedemo.com/")
    wait_for_visibility(driver, (By.ID, "user-name")).send_keys(username)
    wait_for_visibility(driver, (By.ID, "password")).send_keys(password)
    wait_for_clickable(driver, (By.ID, "login-button")).click()

def positive_login():
    with webdriver.Chrome() as driver:
        # driver.maximize_window()
        # driver.get("https://www.saucedemo.com/")
        # username = (By.ID, "user-name")
        # username_ele = wait_for_visibility(driver, username)
        # username_ele.send_keys("standard_user")
        # password = (By.ID, "password")
        # password_ele = wait_for_visibility(driver, password)
        # password_ele.send_keys("secret_sauce")
        # login = (By.ID, "login-button")
        # login_ele = wait_for_clickable(driver, login)
        # login_ele.click()
        login(driver, "standard_user", "secret_sauce")
        assert validate_url(driver.current_url, "inventory")
        take_screenshot(driver, "Positive_login")

def negative_login():
    with webdriver.Chrome() as driver:
        # driver.maximize_window()
        # driver.get("https://www.saucedemo.com/")
        # username = (By.ID, "user-name")
        # username_ele = wait_for_visibility(driver, username)
        # username_ele.send_keys("standard_user1")
        # password = (By.ID, "password")
        # password_ele = wait_for_visibility(driver, password)
        # password_ele.send_keys("secret_sauce")
        # login = (By.ID, "login-button")
        # login_ele = wait_for_clickable(driver, login)
        # login_ele.click()
        login(driver, "standard_user1", "secret_sauce")
        validate_url(driver.current_url, "inventory")
        output = (By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error > h3")
        output_ele = wait_for_visibility(driver, output)
        assert validate_text(output_ele.text, 'Epic sadface: Username and password do not match any user in this service')
        take_screenshot(driver, "Negative_login")


def logout():
    with webdriver.Chrome() as driver:
        driver.maximize_window()
        # driver.get("https://www.saucedemo.com/")
        # username = (By.ID, "user-name")
        # username_ele = wait_for_visibility(driver, username)
        # username_ele.send_keys("standard_user")
        # password = (By.ID, "password")
        # password_ele = wait_for_visibility(driver, password)
        # password_ele.send_keys("secret_sauce")
        # login = (By.ID, "login-button")
        # login_ele = wait_for_clickable(driver, login)
        # login_ele.click()
        login(driver, "standard_user", "secret_sauce")
        if validate_url(driver.current_url, "inventory"):
            menu = (By.ID, "react-burger-menu-btn")
            menu_ele = wait_for_clickable(driver, menu)
            menu_ele.click()
            out = (By.ID, "logout_sidebar_link")
            out_ele = wait_for_clickable(driver, out)
            out_ele.click()
            if validate_url(driver.current_url, "https://www.saucedemo.com/"):
                print("Logout Successfull!!")
                # take_screenshot(driver, "Postive_Logout")
            else:
                print("Logout Failed!!")
                # take_screenshot(driver, "Negative_Logout")
        else:
            print("Login Failed!!!")

logout()