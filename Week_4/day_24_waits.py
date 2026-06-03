from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def validate(actual, expected):
    if expected in actual:
        print(f"{expected} -> Passed ,Actual -> '{actual}'")
    else:
        print(f"{expected} -> Failed ,Actual -> '{actual}'")

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://the-internet.herokuapp.com/login?utm_source=chatgpt.com")

driver.find_element(By.NAME, 'username').send_keys('tomsmith')

driver.find_element(By.CSS_SELECTOR, '#password').send_keys("SuperSecretPassword!")

driver.find_element(By.CLASS_NAME, 'radius').click()

output = wait.until(EC.visibility_of_element_located((By.ID, 'flash')))

validate(output.text, 'You logged into a secure area!')


driver.get("https://the-internet.herokuapp.com/dynamic_loading/1?utm_source=chatgpt.com")

driver.find_element(By.CSS_SELECTOR, "button").click()
hello_op = wait.until(EC.presence_of_element_located((By.ID, "finish")))
validate(hello_op.text, 'Hello World!')
hello_op1 = wait.until(EC.visibility_of_element_located((By.ID, "finish")))
validate(hello_op1.text, 'Hello World!')
driver.quit()
