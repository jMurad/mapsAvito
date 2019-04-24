# Подключаем selenium (сперва установить через pip install selenium)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

# Получаем в переменную browser указатель на браузер
options = Options()
userAgent = "Mozilla / 5.0 (Windows NT 10.0; Win64; x64) AppleWebKit / 537.36 (KHTML, как Gecko) Chrome / 72.0.3626.121 Safari / 537.36"

options.add_argument(f'user-agent={userAgent}')
browser = webdriver.Chrome(options=options, executable_path='chromedriver.exe')

#browser = webdriver.Chrome()


# Переходим на страницу, на которой нужно что-то сделать
browser.get('https://www.avito.ru/dagestan#login?s=h')

# Получаем указатель на поле ввода текста в форме постинга
#login = browser.find_element_by_name('login')
#password = browser.find_element_by_name('password')
#webdriver.ActionChains(browser).move_to_element(login).click(login).perform()
#webdriver.ActionChains(browser).move_to_element(password).click(password).perform()
#login.send_keys('deit91@yandex.ru')
#password.send_keys('M3244dmk')

#textarea1 = browser.find_elements_by_class_name('header-services-menu-link-fsJlE header-services-menu-link-not-authenticated-3Uyu_')
#webdriver.ActionChains(browser).move_to_element(textarea[0]).click(textarea[0]).perform()
#webdriver.ActionChains(browser).key_down().send_keys('c').key_up().perform()
#textarea[1].send_keys('909 484-31-21')
#print(textarea[1].get_attribute('value'))

#submit = browser.find_elements_by_tag_name('button')
#print(submit)
#for sub in submit:
    #if (sub.get_attribute('data-marker') == 'login-form/submit'):
        #print(sub.get_attribute('class'))
        #print('-------')
        #print(sub.text)
        #sub.click()
