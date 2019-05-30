from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent, FakeUserAgentError
import pyautogui
import time


options = Options()
try:
    ua = UserAgent()
    ua.update()
    userAgent = ua.random
except FakeUserAgentError:
    userAgent = "Mozilla / 5.0 (Windows NT 10.0; Win64; x64) AppleWebKit / 537.36 (KHTML, как Gecko) Chrome / " \
                "72.0.3626.121 Safari / 537.36"

options.add_argument(f'user-agent={userAgent}')
browser = webdriver.Chrome(options=options, executable_path="../chromedriver.exe")
# browser = webdriver.Chrome()

# Переходим на страницу, на которой нужно что-то сделать
browser.get('https://www.instagram.com/')

time.sleep(5)
print('start')
duration = 1
interval = 0.1

imgXY = pyautogui.locateCenterOnScreen('../imgs/start.png')
pyautogui.moveTo(imgXY[0], imgXY[1]+85, duration=duration)
pyautogui.click()
pyautogui.typewrite(['k', 'r', 'o', 'n', 's', 'i', 'r', 'i', 'u', 's', '@', 'g', 'm', 'a', 'i',
                     'l', '.', 'c', 'o', 'm'], interval=interval)
time.sleep(1)

# imgXY = pyautogui.locateCenterOnScreen('../imgs/name.png')
pyautogui.moveTo(imgXY[0], imgXY[1]+125, duration=duration)
pyautogui.click()
pyautogui.typewrite(['M', 'u', 'r', 'a', 'd', 'enter'], interval=interval)
time.sleep(1)

# imgXY = pyautogui.locateCenterOnScreen('../imgs/username.png')
pyautogui.moveTo(imgXY[0], imgXY[1]+175, duration=duration)
pyautogui.click()
pyautogui.typewrite(['m', 'u', 'r', 'a', 'd', '4', '0', '1', 't', 'enter'], interval=interval)
time.sleep(1)

# imgXY = pyautogui.locateCenterOnScreen('../imgs/password.png')
pyautogui.moveTo(imgXY[0], imgXY[1]+220, duration=duration)
pyautogui.click()
pyautogui.typewrite(['3', '2', '4', '4', 'd', 'm', 'k', 'enter'], interval=interval)
time.sleep(1)

# imgXY = pyautogui.locateCenterOnScreen('../imgs/reg.png')
pyautogui.moveTo(imgXY[0], imgXY[1]+265, duration=duration)
pyautogui.click()

# -----------------------------------------------------------------------------------------------------------
# Получаем указатель на поле ввода текста в форме постинга
# login = browser.find_element_by_name('login')
# password = browser.find_element_by_name('password')
# webdriver.ActionChains(browser).move_to_element(login).click(login).perform()
# webdriver.ActionChains(browser).move_to_element(password).click(password).perform()
# login.send_keys('deit91@yandex.ru')
# password.send_keys('M3244dmk')

# textarea1 = browser.find_elements_by_class_name('header-services-menu-link-fsJlE header-services-menu-link-
# not-authenticated-3Uyu_')
# webdriver.ActionChains(browser).move_to_element(textarea[0]).click(textarea[0]).perform()
# webdriver.ActionChains(browser).key_down().send_keys('c').key_up().perform()
# textarea[1].send_keys('909 484-31-21')
# print(textarea[1].get_attribute('value'))

# submit = browser.find_elements_by_tag_name('button')
# print(submit)
# for sub in submit:
#    if (sub.get_attribute('data-marker') == 'login-form/submit'):
#        print(sub.get_attribute('class'))
#        print('-------')
#        print(sub.text)
#        sub.click()
