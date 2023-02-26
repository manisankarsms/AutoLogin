import pyautogui
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# login credentials
username = "ippbfss"
password = "N0P@ssw0rds"


def main():
    # initialize the Chrome driver
    driver = webdriver.Chrome(r"chromedriver")
    # head to gitHub login page
    driver.get("https://github.com/login")
    # find username/email field and send the username itself to the input field
    driver.find_element("id", "login_field").send_keys(username)
    # find password input field and insert password as well
    driver.find_element("id", "password").send_keys(password)
    # click login button
    driver.find_element("name", "commit").click()
    # wait the ready state to be complete
    WebDriverWait(driver=driver, timeout=10).until(
        lambda x: x.execute_script("return document.readyState === 'complete'")
    )
    error_message = "Login Failed/Incorrect username or password."
    # get the errors (if there are)
    errors = driver.find_elements("css selector", ".flash-error")
    # print the errors optionally
    # for e in errors:
    #     print(e.text)
    # if we find that error message within errors, then login is failed
    if any(error_message in e.text for e in errors):
        print("[!] Login failed")
    else:
        print("[+] Login successful")
        my_screenshot = pyautogui.screenshot()
        my_screenshot.save(r'/Users/manisankar/PycharmProjects/RottenFruitDetection/S1.png')

    # close the driver
    driver.close()


if __name__ == '__main__':
    main()
