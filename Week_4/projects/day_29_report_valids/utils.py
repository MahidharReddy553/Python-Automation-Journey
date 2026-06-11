def validate_msg(actual, expected):
    if expected in actual:
        return True
    return False

def take_screenshot(driver, filename):
    driver.save_screenshot(f"./screenshots/{filename}.png")

