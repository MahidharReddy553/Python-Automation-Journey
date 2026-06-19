from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

DEFAULT_TIMEOUT = 10
def wait_for_visibility(driver, element, timeout = DEFAULT_TIMEOUT):
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.visibility_of_element_located((element)))

def wait_for_clickable(driver, element, timeout = DEFAULT_TIMEOUT):
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.element_to_be_clickable((element)))

def wait_for_presence(driver, element, timeout = DEFAULT_TIMEOUT):
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.presence_of_element_located((element)))

def take_screenshot(driver, filename):
    i = 1
    while True:
        if not os.path.isfile(f'./screenshots/{filename}{i}.png'):
            driver.save_screenshot(f'./screenshots/{filename}{i}.png')
            print("Screenshot saved successfully!!")
            break
        i += 1

def validate_url(actual, expected):
    if expected in actual:
        print(f"'{expected}' is present in the url : '{actual}'")
        return True
    else:
        print(f"{expected} is not present in the url : '{actual}'")
        return False
    
def validate_text(actual, expected):
    if expected in actual:
        print(f"Text matched successfully!! \nActual : '{actual}'\nExpected : '{expected}'")
        return True
    else:
        print(f"Text is not matched!! \nActual : '{actual}'\nExpected : '{expected}'")
        return False