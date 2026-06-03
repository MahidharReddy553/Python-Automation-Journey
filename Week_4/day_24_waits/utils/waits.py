from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def wait_for_clickable(driver, element):
    wait = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(element))
    return wait

def wait_for_visibility(driver, element):
    wait = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(element))
    return wait

def validate(actual, expected):
    if expected in actual:
        print(f"{expected} -> Passed ,Actual -> '{actual}'")
    else:
        print(f"{expected} -> Failed ,Actual -> '{actual}'")