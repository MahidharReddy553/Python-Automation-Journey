from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def main():
    with webdriver.Chrome() as driver:
        wait = WebDriverWait(driver, 10)

        driver.get("https://demo.automationtesting.in/Frames.html")

        i_frame = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#singleframe')))

        driver.switch_to.frame(i_frame)
        
        demo = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/section/div/h5')))

        print(demo.text)

        wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/section/div/div/div/input'))).send_keys('Pranamamulu!!!')

        output = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/section/div/div/div/input')))

        driver.switch_to.default_content()

        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a'))).click()

        time.sleep(2)

        frame1 = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="Multiple"]/iframe')))

        driver.switch_to.frame(frame1)

        f1_text = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/section/div/div/h5')))

        print(f1_text.text)

        frame2 = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/section/div/div/iframe')))

        driver.switch_to.frame(frame2)

        f2_text = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/section/div/h5')))

        print(f2_text.text)

        wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/section/div/div/div/input'))).send_keys("Bagunnara!!!")

        time.sleep(1)

        driver.switch_to.parent_frame()

        f11_text = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/section/div/div/h5')))

        print(f11_text.text)

        driver.switch_to.default_content()

        main_t = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header"]/div/div/div/div[2]/h1')))

        print(main_t.text)

        driver.save_screenshot('./screenshots/iframes.png')


main()