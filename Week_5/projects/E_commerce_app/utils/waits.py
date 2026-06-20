from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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