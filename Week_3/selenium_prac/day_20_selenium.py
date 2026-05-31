from selenium import webdriver
import time

driver = webdriver.Chrome()
time.sleep(2)
driver.maximize_window()
driver.get("https://www.google.com/")
time.sleep(2)

print(driver.current_url)
print(driver.title)

driver.get("https://www.github.com/")
time.sleep(2)

print(driver.title)
print(driver.current_url)

driver.quit()