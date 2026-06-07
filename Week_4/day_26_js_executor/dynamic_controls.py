from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/dynamic_controls?utm_source=chatgpt.com")

wait = WebDriverWait(driver, 10)

remove_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Remove"]')))
driver.execute_script("arguments[0].click();", remove_btn)

msg = wait.until(EC.visibility_of_element_located((By.ID, "message")))
print("After Remove:", msg.text)


add_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Add"]')))
driver.execute_script("arguments[0].click();", add_btn)

msg = wait.until(EC.visibility_of_element_located((By.ID, "message")))
print("After Add:", msg.text)


enable_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Enable"]')))
driver.execute_script("arguments[0].click();", enable_btn)

msg = wait.until(EC.visibility_of_element_located((By.ID, "message")))
print("After Enable:", msg.text)


input_box = wait.until(EC.presence_of_element_located((By.XPATH, '//form[@id="input-example"]/input')))
driver.execute_script("arguments[0].value='Bagunnaraa !!!';", input_box)


disable_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Disable"]')))
driver.execute_script("arguments[0].click();", disable_btn)

msg = wait.until(EC.visibility_of_element_located((By.ID, "message")))
print("After Disable:", msg.text)

driver.save_screenshot('./screenshots/dynamic_controls.png')

driver.quit()