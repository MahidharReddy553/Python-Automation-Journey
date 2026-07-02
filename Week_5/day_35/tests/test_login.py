import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize(("username"), ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user"])
def test_login(login_fixture, username):

    assert "inventory" in login_fixture.current_url, "Login failed"
    print('Login success')
