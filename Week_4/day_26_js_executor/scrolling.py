from selenium import webdriver
import time
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:

    driver.maximize_window()

    driver.get("https://demoqa.com/automation-practice-form?utm_source=chatgpt.com")

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    sub = driver.find_element(By.XPATH, '//*[@id="submit"]')

    driver.execute_script('arguments[0].click()', sub)

    driver.save_screenshot('./screenshots/scrolling.png')