import configparser
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# based on your internet speed, you can change time unit
TIME_UNIT = 1


def sign_in(driver):
    config = configparser.ConfigParser()
    config.read('LoginData.ini')

    my_username = config['instagram']['username']
    my_password = config['instagram']['password']

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
        print("waiting for instagram to open completely...")
        sleep(TIME_UNIT)

    print('We logged in.')


def open_url(driver, post_url):
    # post_url = input('write post url: ')
    driver.get(post_url)
    sleep(TIME_UNIT)

    while post_url not in driver.current_url:
        print("Driver is still on: " + driver.current_url)
        driver.get(post_url)
        sleep(TIME_UNIT * 2)


def open_likes(driver):
    likes_button_xpath = '//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[' \
                         '2]/div/div/a/span'

    print("Clicking on likes button...")

    try:
        likes_button = driver.find_element_by_xpath(likes_button_xpath)
        likes_button.click()
    except NoSuchElementException:
        print("couldn't open likes. trying another way.")
        sleep(TIME_UNIT * 2)
        likes_button_xpath = '//*[@id="react-root"]/section/main/div/div[1]/article/div/div[3]/div/div/section[' \
                             '2]/div/div/a'
        likes_button = driver.find_element_by_xpath(likes_button_xpath)
        likes_button.click()

    sleep(TIME_UNIT * 2)


def check_likes(driver):

    print('checking likes...')

    # liked_users_class = 'FPmhX notranslate MBL3Z'
    liked_users_class = 'Jv7Aj mArmR MqpiF  '
    sleep(TIME_UNIT * 2)
    liked_users_elements = driver.find_elements_by_class_name(liked_users_class)

    print('liked by (elements):')
    print(liked_users_elements)

    liked_users = []
    for liked_user in liked_users_elements:
        username = liked_user.text
        liked_users.append(username)

    print('liked by (ids):')
    print(liked_users)

    checking_ids = ['3rna_._', 'zeinabpanahi82', 'm_ch211', 'nara_mezon']

    for checking_id in checking_ids:
        if checking_id in liked_users:
            print('yes: ' + checking_id)
        else:
            print('no:  ' + checking_id)


if __name__ == '__main__':

    # Choose your favorite browser :)
    chrome_driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    # driver = webdriver.Opera()

    sign_in(chrome_driver)

    open_url(chrome_driver, 'https://www.instagram.com/p/CXbiYpqISG0/')

    open_likes(chrome_driver)

    check_likes(chrome_driver)
