from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


with webdriver.Chrome() as driver:

    driver.get("https://demoqa.com/select-menu")
    wait = WebDriverWait(driver, 30)
    option = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oldSelectMenu"]')))
    Select(option).select_by_value('9')
    sel_option = Select(option).first_selected_option
    print(sel_option.text)

    option2 = wait.until(EC.visibility_of_element_located((By.ID, "cars")))
    Select(option2).select_by_value('audi')
    Select(option2).select_by_index(2)
    sel_option2 = Select(option2).all_selected_options
    print([i.text for i in sel_option2])