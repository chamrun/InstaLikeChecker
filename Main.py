import configparser
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# based on your internet speed, you can change time unit
TIME_UNIT = 1

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('LoginData.ini')

    my_username = config['instagram']['username']
    my_password = config['instagram']['password']

    # Choose your favorite browser :)
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    # driver = webdriver.Opera()

    print("Opening instagram...")
    login_url = 'https://www.instagram.com/accounts/login/'
    driver.get(login_url)
    sleep(TIME_UNIT)

    while 'insta' not in driver.current_url:
        print("Driver is still on: " + driver.current_url)
        driver.get(login_url)
        sleep(TIME_UNIT * 2)

    print("Writing username...")
    username_field_xpath = '//*[@id="loginForm"]/div/div[1]/div/label/input'
    username_field = driver.find_element_by_xpath(username_field_xpath)
    username_field.send_keys(my_username)

    print("Writing password...")
    password_field_xpath = '//*[@id="loginForm"]/div/div[2]/div/label/input'
    password_field = driver.find_element_by_xpath(password_field_xpath)
    password_field.send_keys(my_password)

    print("Clicking on login button...")
    login_button_xpath = '//*[@id="loginForm"]/div/div[3]'
    login_button = driver.find_element_by_xpath(login_button_xpath)
    login_button.click()

    while 'login' in driver.current_url:
        sleep(TIME_UNIT)
        