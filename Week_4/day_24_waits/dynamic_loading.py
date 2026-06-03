from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.waits import wait_for_visibility, validate

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/dynamic_loading/1?utm_source=chatgpt.com")

driver.find_element(By.CSS_SELECTOR, '#start button').click()

op_element = (By.ID, "finish")

output = wait_for_visibility(driver, op_element)

validate(output.text, "Hello World!")

driver.quit()