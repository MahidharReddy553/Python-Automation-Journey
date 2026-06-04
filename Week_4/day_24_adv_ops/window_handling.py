from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Chrome() as driver:

    wait = WebDriverWait(driver, 20)

    driver.get('https://the-internet.herokuapp.com/windows?utm_source=chatgpt.com')
    main = driver.current_window_handle
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div/a'))).click()
    for handle in driver.window_handles:
        if handle != main:
            driver.switch_to.window(handle)
            break
    print("new window title :", driver.title)

    driver.switch_to.window(main)
    print("Main window :", driver.title)