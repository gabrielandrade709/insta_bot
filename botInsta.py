from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
from pynput.keyboard import Key, Controller

keyboard = Controller()


chromedriver_path = 'C:/Users/gabri/Downloads/bot/chromedriver.exe' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
username.send_keys('seu_usuario)
password = webdriver.find_element_by_name('password')
password.send_keys('sua_senha')

button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button')
button_login.click()
sleep(3)

search = webdriver.find_element_by_class_name('coreSpriteSearchIcon')
search.click()
sleep(3)

search_word = webdriver.find_element_by_css_selector('#react-root > section > nav > div:nth-child(2) > div > div > div:nth-child(2) > input')
search_word.send_keys('@INSTAPOPULAR')
sleep(2)
keyboard.press(Key.enter)
sleep(1)
keyboard.press(Key.enter)
sleep(2)

following = webdriver.find_element_by_css_selector("#react-root > section > main > div > header > section > ul > li:nth-child(3) > a[href*='/popugramsg/following/']")
following.click()
sleep(2)

j = 1
while j <= 4:
    keyboard.press(Key.tab)
    sleep(0.5)
    j += 1

k = 1
while k <= 6:
    keyboard.press(Key.down)
    sleep(0.5)
    k += 1

j = 1
while j <= 4:
    keyboard.press(Key.tab)
    sleep(0.5)
    j += 1

k = 1
while k <= 352:
    keyboard.press(Key.down)
    sleep(0.2)
    k += 1

sleep(2)

while True:
    i= 1
    while i <= 177:
        follow = webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li[' + str(i) + ']/div/div[2]/button')
        follow.click()
        sleep(30)
        i += 1

    sleep(2400)

    i = 1 
    while i <= 177:
        follow = webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li[' + str(i) + ']/div/div[2]/button')
        follow.click()
        sleep(1)
        confirm = webdriver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]')
        confirm.click()
        sleep(30)
        i += 1

    sleep(2400)
