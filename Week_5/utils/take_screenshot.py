import os

def take_screenshot(driver, filename):
    i = 1
    while True:
        if not os.path.isfile(f'./screenshots/{filename}{i}.png'):
            driver.save_screenshot(f'./screenshots/{filename}{i}.png')
            print("Screenshot saved successfully!!")
            break
        i += 1