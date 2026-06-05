from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def main():
    with webdriver.Chrome() as driver:

        wait = WebDriverWait(driver, 10)
        driver.get("https://the-internet.herokuapp.com/javascript_alerts?utm_source=chatgpt.com")

        js_alert = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div/ul/li[1]/button')))
        js_alert.click()
        driver.switch_to.alert.accept()
        res = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="result"]')))
        print(res.text)

        js_confirm = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/ul/li[2]/button')))
        js_confirm.click()
        driver.switch_to.alert.accept()
        res2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="result"]')))
        print(res2.text)

        js_msg = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/ul/li[3]/button')))
        js_msg.click()
        driver.switch_to.alert.send_keys('Hello Bagunnava!!')
        driver.switch_to.alert.accept()
        res3 = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="result"]')))
        print(res3.text)

        driver.save_screenshot('./screenshots/alerts.png')


main()