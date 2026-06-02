from selenium import webdriver
from selenium.webdriver.common.by import By
import time

name = "Loki"
email = "example@gmail.com"
current_address = "TVA"
permanent_address = "Asgard"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/text-box?utm_source=chatgpt.com")
print('Title :', driver.title)
time.sleep(1)

driver.find_element(By.ID, "userName").send_keys(name)
time.sleep(1)
driver.find_element(By.ID, "userEmail").send_keys(email)
time.sleep(1)
driver.find_element(By.ID, "currentAddress").send_keys(current_address)
time.sleep(1)
driver.find_element(By.ID, "permanentAddress").send_keys(permanent_address)
driver.execute_script('window.scrollTo(0,400);')
time.sleep(1)
driver.find_element(By.ID, "submit").click()
time.sleep(1)

output_name = driver.find_element(By.ID, "name")
output_email = driver.find_element(By.ID, "email")
output_curr_address = driver.find_element(By.CSS_SELECTOR, "#currentAddress.mb-1")
output_perm_address = driver.find_element(By.CSS_SELECTOR, "#permanentAddress.mb-1")

def validate(actual, expected):
    if expected.lower() in actual.lower():
        print(f"{expected} -> PASS")
    else:
        print(f"{expected} -> FAIL")

validate(output_name.text, name)
validate(output_email.text, email)
validate(output_curr_address.text, current_address)
validate(output_perm_address.text, permanent_address)

time.sleep(1)
driver.quit()