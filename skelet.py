from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from fake_useragent import UserAgent

import time

user_input = ''
user_password = ''
user_input_i = input('text')

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument('--incognito')
chrome_option.add_argument(f"--user-agent={UserAgent().random}")  # fake user agent
chrome_option.add_argument("--disable-blink-features=AutomationControlled")  # it prove we are not a robot

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_option)

driver.get('https://store.steampowered.com/login/')

element_present = EC.presence_of_element_located(('xpath', '//*[@id="responsive_page_template_content"]/div[3]/div[1]/div/div/div/div[2]/div/form/div[1]/input'))
WebDriverWait(driver, 8).until(element_present)

account_name = driver.find_element('xpath', '//*[@id="responsive_page_template_content"]/div[3]/div[1]/div/div/div/div[2]/div/form/div[1]/input')
account_name.send_keys(f'{user_input}')

password = driver.find_element('xpath', '//*[@id="responsive_page_template_content"]/div[3]/div[1]/div/div/div/div[2]/div/form/div[2]/input')
password.send_keys(f'{user_password}')

button = driver.find_element('xpath', '//*[@id="responsive_page_template_content"]/div[3]/div[1]/div/div/div/div[2]/div/form/div[4]/button')
button.click()

if user_input_i:
    if driver.find_element('xpath', '//*[@id="responsive_page_template_content"]/div[3]/div[1]/div/div/div/div[2]/div'):
        print('end your verify')

        element_present = EC.presence_of_element_located(
            ('xpath', '//*[@id="searchform"]/div'))
        WebDriverWait(driver, 600).until(element_present)
        if element_present:
            print('the end')


time.sleep(50)






