import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
# Browser fixture
def browser_fixture():
    '''to open chrome browser and close it'''
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def login_fixture(browser_fixture, username):
    '''to login with the username and password'''
    browser_fixture.get("https://www.saucedemo.com")
    browser_fixture.find_element(By.ID, "user-name").send_keys(username)
    browser_fixture.find_element(By.ID, "password").send_keys("secret_sauce")
    browser_fixture.find_element(By.ID, "login-button").click()

    return browser_fixture

@pytest.mark.parametrize(("username"), ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user"])
def test_login(login_fixture, username):

    assert "inventory" in login_fixture.current_url, "Login failed"
    print('Login success')
