from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time


with webdriver.Chrome() as driver:

    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    driver.get("https://the-internet.herokuapp.com/drag_and_drop?utm_source=chatgpt.com")

    drag = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="column-a"]')))

    drop = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="column-b"]')))

    ActionChains(driver).drag_and_drop(drag, drop).perform()

    driver.save_screenshot('./screenshots/drag_and_drop.png')