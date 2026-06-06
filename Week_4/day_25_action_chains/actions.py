from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

with webdriver.Chrome() as driver:
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    driver.get("https://demoqa.com/buttons?utm_source=chatgpt.com")

    # Double click
    db_click = wait.until(EC.element_to_be_clickable((By.ID, "doubleClickBtn")))
    time.sleep(1)
    ActionChains(driver).double_click(db_click).perform()
    time.sleep(1)

    # Right click
    r_click = wait.until(EC.element_to_be_clickable((By.ID, "rightClickBtn")))
    time.sleep(1)
    ActionChains(driver).context_click(r_click).perform()
    time.sleep(1)

    # Dynamic click
    click_ele = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Click Me"]')))
    time.sleep(1)
    ActionChains(driver).click(click_ele).perform()
    time.sleep(1)

    driver.save_screenshot('./screenshots/actions.png')
