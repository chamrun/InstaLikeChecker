import configparser
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# based on your internet speed, you can change time unit
TIME_UNIT = 1


def sign_in(driver):
    config = configparser.ConfigParser()
    # config.read('LoginData.ini')
    config.read('login_data.ini')

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
        print("waiting for instagram to be opened completely...")
        sleep(1)

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
    sleep(TIME_UNIT)
    likes_button_xpath = '//*[@id="react-root"]/section/main/div/div[1]/article/div/div[3]/div/div/section[' \
                         '2]/div/div/a'

    print("Clicking on likes button...")
    sleep(TIME_UNIT * 2)
    try:
        likes_button = driver.find_element_by_xpath(likes_button_xpath)
        likes_button.click()
    except NoSuchElementException:
        try:
            print("couldn't open likes. trying another way.")
            sleep(TIME_UNIT * 2)
            likes_button_xpath = '//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/' \
                                 'section[2]/div/div/a/span'
            likes_button = driver.find_element_by_xpath(likes_button_xpath)
            likes_button.click()
        except NoSuchElementException:
            print("couldn't open likes. trying another way.")
            sleep(TIME_UNIT * 2)
            likes_button_xpath = '//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/' \
                                 'section[2]/div/div/a/span'
            likes_button = driver.find_element_by_xpath(likes_button_xpath)
            likes_button.click()

    sleep(TIME_UNIT * 2)


def check_likes(driver, checking_ids):
    """
    print('second method: Done.')
    userid_element = \
    driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[2]/div/div/a')[0].click()
    sleep(2)

    # here, you can see user list you want.
    # you have to scroll down to download more data from instagram server.
    # loop until last element with users table view height value.

    users = []

    height = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div").value_of_css_property("padding-top")
    match = False
    while match == False:
        last_height = height

        # step 1
        elements = driver.find_elements_by_xpath("//*[@id]/div/a")

        # step 2
        for element in elements:
            if element.get_attribute('title') not in users:
                users.append(element.get_attribute('title'))

        # step 3
        driver.execute_script("return arguments[0].scrollIntoView();", elements[-1])
        sleep(1)

        # step 4
        height = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div").value_of_css_property(
            "padding-top")
        if last_height == height:
            match = True

    print(users)
    print(len(users))

    print('second method: Done.')
    """
    # elems = driver.find_elements_by_class_name("//a[@class='FPmhX notranslate']")

    """
    elems = 

    # elems = driver.find_elements_by_

    print('elems: ')
    print(elems)
    users = []

    for elem in elems:
        users.append(elem.get_attribute('title'))
        print('Title : ' + elem.get_attribute('title'))

    print(users)

    print('checking likes...')

    liked_users_class = 'FPmhX notranslate MBL3Z'
    # liked_users_class = 'Jv7Aj mArmR MqpiF'
    sleep(TIME_UNIT * 2)
    liked_users_elements = driver.find_elements_by_class_name(liked_users_class)

    print('liked by (elements):')
    print(liked_users_elements)
"""

    liker_users_elements = driver.find_elements_by_xpath("//a[@class='FPmhX notranslate MBL3Z']")
    liker_users = []
    for liker_users_element in liker_users_elements:
        liker_users.append(liker_users_element.get_attribute('title'))
        print('liked by : ' + liker_users_element.get_attribute('title'))
    """
    for liked_user in liked_users_elements:
        username = liked_user.get_attribute('title')
        liker_users.append(username)
    """

    height = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div/div").value_of_css_property(
        "padding-top")

    match = False

    while not match:
        last_height = height

        # step 1
        elements = driver.find_elements_by_xpath("//a[@class='FPmhX notranslate MBL3Z']")

        # step 2
        for element in elements:
            if element.get_attribute('title') not in liker_users:
                liker_users.append(element.get_attribute('title'))
                print('liked by : ' + element.get_attribute('title'))

        # step 3
        driver.execute_script("return arguments[0].scrollIntoView();", elements[-1])
        sleep(1)

        # step 4
        height = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div/div").value_of_css_property(
            "padding-top")
        if last_height == height:
            match = True

    print('liked by (ids):')
    print(liker_users)

    for checking_id in checking_ids:
        if checking_id in liker_users:
            print('yes: ' + checking_id)
        else:
            print('no:  ' + checking_id)


def main():
    input('write anything to start\n')

    # Choose your favorite browser :)
    chrome_driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    # driver = webdriver.Opera()

    sign_in(chrome_driver)

    # Change post url, here :D
    open_url(chrome_driver, 'https://www.instagram.com/p/CXbiYpqISG0/')

    open_likes(chrome_driver)

    # Change 
    checking_ids = ['_mahla_f', 'herbalbeauty.shopp', '3rna_._', 'zeinabpanahi82', 'm_ch211', 'nara_mezon',
                    '_divacosmetics_']
    check_likes(chrome_driver, checking_ids)

    input('write anything to exit\n')


if __name__ == '__main__':
    main()
