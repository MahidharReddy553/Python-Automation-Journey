from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

with webdriver.Chrome() as driver:

    wait = WebDriverWait(driver, 10)

    driver.maximize_window()
    
    driver.get("https://demoqa.com/menu?utm_source=chatgpt.com#")

    ele1 = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="nav"]/li[1]/a')))

    ActionChains(driver).move_to_element(ele1).perform()

    ele2 = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="nav"]/li[3]/a')))

    ActionChains(driver).move_to_element(ele2).perform()

    ele = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nav"]/li[2]/a')))

    ActionChains(driver).move_to_element(ele).perform()

    sub = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="nav"]/li[2]/ul/li[3]/a')))

    ActionChains(driver).move_to_element(sub).perform()

    driver.save_screenshot('./screenshots/hover.png')