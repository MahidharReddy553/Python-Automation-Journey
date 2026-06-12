import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



# ---------------- Logging Configuration ----------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("login_suite.log"),  # Save logs to file
        logging.StreamHandler()                  # Print logs to console
    ]
)

# ---------------- Selenium Setup ----------------
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)
# ---------------- Helper Functions ----------------
def take_screenshot(name):
    """Capture screenshot with given filename"""
    driver.save_screenshot(name)
    logging.info(f"Screenshot saved: {name}")

# ---------------- Positive Login Test ----------------
def positive_login():
    try:
        logging.info("Starting Positive Login Test")
        driver.get("https://the-internet.herokuapp.com/login")
        logging.info("Navigated to login page")

        driver.find_element(By.ID, "username").send_keys("tomsmith")
        logging.info("Entered valid username")

        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        logging.info("Entered valid password")

        driver.find_element(By.CSS_SELECTOR, "button.radius").click()
        logging.info("Clicked login button")

        # Assertions
        assert "secure" in driver.current_url, "URL validation failed"
        logging.info("URL validation passed")

        success_msg = driver.find_element(By.ID, "flash").text
        assert "You logged into a secure area!" in success_msg, "Success message validation failed"
        logging.info("Success message validation passed")

        take_screenshot("positive_login_success.png")

    except Exception as e:
        logging.error(f"Positive login test failed: {e}")
        take_screenshot("positive_login_failure.png")

# ---------------- Negative Login Test ----------------
def negative_login():
    try:
        logging.info("Starting Negative Login Test")
        driver.get("https://the-internet.herokuapp.com/login")
        logging.info("Navigated to login page")

        driver.find_element(By.ID, "username").send_keys("wronguser")
        logging.info("Entered invalid username")

        driver.find_element(By.ID, "password").send_keys("wrongpassword")
        logging.info("Entered invalid password")

        driver.find_element(By.XPATH, '//*[@id="login"]/button').click()
        logging.info("Clicked login button")

        # Assertions
        error_msg = wait.until(EC.visibility_of_element_located((By.ID, "flash"))).text
        assert "Your username is invalid!" in error_msg or "Your password is invalid!" in error_msg, "Error message validation failed"
        logging.info("Error message validation passed")

        take_screenshot("negative_login_success.png")

    except Exception as e:
        logging.error(f"Negative login test failed: {e}")
        take_screenshot("negative_login_failure.png")

# ---------------- Run Tests ----------------
positive_login()
time.sleep(2)
negative_login()

driver.quit()
logging.info("Test Suite Finished")