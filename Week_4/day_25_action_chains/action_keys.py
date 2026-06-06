from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


with webdriver.Chrome() as driver:
    
    driver.maximize_window()

    action = ActionChains(driver)

    wait = WebDriverWait(driver, 10)

    driver.get("https://demoqa.com/text-box?utm_source=chatgpt.com")

    name = wait.until(EC.visibility_of_element_located((By.ID, 'userName')))

    name.click()

    name.send_keys("Loki")

    action.send_keys(Keys.TAB).send_keys("loki@exp.com").perform()

    action.send_keys(Keys.TAB).send_keys("TVA").perform()

    action.send_keys(Keys.TAB).send_keys("Asgard").perform()

    action.send_keys(Keys.TAB).perform()

    action.send_keys(Keys.ENTER).perform()

    output = wait.until(EC.visibility_of_element_located((By.ID, 'permanentAddress')))

    action.scroll_by_amount(0, 600).perform()

    driver.save_screenshot('./screenshots/keys.png')