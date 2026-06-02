from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/text-box?utm_source=chatgpt.com")
print('Title :', driver.title)
time.sleep(1)

driver.find_element(By.ID, "userName").send_keys("Loki")
time.sleep(1)
driver.find_element(By.ID, "userEmail").send_keys("example@gmail.com")
time.sleep(1)
driver.find_element(By.ID, "currentAddress").send_keys("TVA")
time.sleep(1)
driver.find_element(By.ID, "permanentAddress").send_keys("Asgard")
driver.execute_script('window.scrollTo(0,400);')
time.sleep(1)
driver.find_element(By.ID, "submit").click()
time.sleep(1)

output = driver.find_element(By.ID, "output")
time.sleep(1)
print(output.text)
driver.quit()