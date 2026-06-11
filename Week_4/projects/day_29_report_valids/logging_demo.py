from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils import validate_msg, take_screenshot

with webdriver.Chrome() as driver:
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.get("https://the-internet.herokuapp.com/login?utm_source=chatgpt.com")

    username = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id = 'username']")))
    username.send_keys('tomsmith')
    password = wait.until(EC.visibility_of_element_located((By.ID, 'password')))
    password.send_keys('SuperSecretPassword!')
    submit = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login"]/button')))
    submit.click()
    output = wait.until(EC.visibility_of_element_located((By.ID, 'flash')))

    if validate_msg(output.text, 'Your username is invalid') or validate_msg(output.text, 'Your password is invalid'):
        print('Login Failed!!!')
        take_screenshot(driver, 'login_failed')

    elif validate_msg(output.text, 'You logged into a secure area'):
        print('Login Success!!!')
        take_screenshot(driver, 'login_success')

    else:
        print("Something went wrong in logging")