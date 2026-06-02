from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
print('Title :', driver.title)
print('url :', driver.current_url)

time.sleep(1)

# driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("tomsmith")

element = driver.find_element(By.NAME, 'username')
print("name of username element :", element.get_attribute('name'))
print("id of username element :", element.get_attribute('id'))


element.send_keys("tomsmith123")
element.clear()
driver.find_element(By.NAME, 'username').send_keys('tomsmith')

time.sleep(2)
# driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, '#password').send_keys("SuperSecretPassword!")
time.sleep(2)
# driver.find_element(By.XPATH, '//*[@id="login"]/button').click()

driver.find_element(By.CLASS_NAME, 'radius').click()
print('---------------------')
print('Title :', driver.title)
print('url :', driver.current_url)
msg = driver.find_element(By.ID, 'flash').text.strip()
print('-----------------------')

if "secure area" in msg:
    print("Login Success")
    driver.find_element(By.CSS_SELECTOR, '#content > div > a').click()
    msg = driver.find_element(By.ID, 'flash')
    if 'logged out' in msg.text:
        print('logged out successfully')
    else:
        print('logout failed.')

else:
    print("Login Failed")

time.sleep(1)
driver.quit()

