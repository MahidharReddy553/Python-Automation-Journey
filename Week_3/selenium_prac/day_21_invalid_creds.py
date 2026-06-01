from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/login")
print('Title :', driver.title)
print('url :', driver.current_url)

driver.find_element(By.NAME, 'username').send_keys("tomsmith1")

driver.find_element(By.CSS_SELECTOR, '#password').send_keys("SuperSecretPassword!")
time.sleep(2)

driver.find_element(By.CLASS_NAME, 'radius').click()

invalid_msg = driver.find_element(By.ID, 'flash').text.strip()

if "Your username is invalid" in invalid_msg:
    print("Login failed !!. Username is invalid.")
elif "Your password is invalid" in invalid_msg:
    print("Login Failed !!. Password is invalid.")
else:
    print("logged in successfully")

driver.quit()