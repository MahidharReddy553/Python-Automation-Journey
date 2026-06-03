from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.waits import wait_for_clickable, wait_for_visibility, validate
import time

with webdriver.Chrome() as driver:
    
    driver.get("https://the-internet.herokuapp.com/login?utm_source=chatgpt.com")

    driver.maximize_window()

    username = wait_for_visibility(driver, (By.NAME, 'username'))

    username.send_keys('tomsmith')

    password = wait_for_visibility(driver, (By.CSS_SELECTOR, '#password'))

    password.send_keys("SuperSecretPassword!")

    login = wait_for_clickable(driver, (By.CLASS_NAME, 'radius'))

    login.click()

    output = wait_for_visibility(driver, (By.ID, 'flash'))

    validate(output.text, 'You logged into a secure area!')

    logout = wait_for_clickable(driver, (By.CLASS_NAME, 'radius'))

    logout.click()

    output1 = wait_for_visibility(driver, (By.ID, 'flash'))

    validate(output1.text, 'You logged out of the secure area!')