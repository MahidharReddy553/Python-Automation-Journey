from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.waits import validate

with webdriver.Chrome() as driver:

    driver.get("https://the-internet.herokuapp.com/login?utm_source=chatgpt.com")

    driver.implicitly_wait(10)

    driver.find_element(By.NAME, 'username').send_keys('tomsmith')

    driver.find_element(By.CSS_SELECTOR, '#password').send_keys("SuperSecretPassword!")

    driver.find_element(By.CLASS_NAME, 'radius').click()

    output = driver.find_element(By.ID, 'flash')

    validate(output.text, 'You logged into a secure area!')

    # driver.find_element(By.CLASS_NAME, 'radius').click()

    # output1 = driver.find_element(By.ID, 'flash')

    # validate(output1.text, 'You logged out of the secure area!')