# Roblox Limiteds Sniper
import configparser, time, warnings, os, requests, cloudscraper, cfscrape, bs4
from typing import Counter
from logging import error
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import wait
from selenium.webdriver.support.expected_conditions import _find_element, element_located_selection_state_to_be, presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from configparser import ConfigParser

# Read config file and grab username/password
config = ConfigParser()
config.read('config.ini')
username = config.get('data','username')
password = config.get('data','pass')
following = config.get('data','following')
count = 1

# Disable python logging to console
warnings.filterwarnings("ignore")
clear = lambda: os.system('cls')
clear()
# Setup web-driver
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--hide-scrollbars')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--log-level=3')
options.add_argument('--disable-infobars')
options.add_argument('--start-maximized')
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-extensions")
# options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
clear()

# TODO
class User:
    def login(self):
        driver.get('https://www.roblox.com/newlogin')
        driver.find_element_by_xpath('//*[@id="login-username"]').send_keys(username)
        driver.find_element_by_xpath('//*[@id="login-password"]').send_keys(password)
        driver.find_element_by_xpath('//*[@id="login-button"]').click()
        time.sleep(3)
        # driver.add_cookie(cookie)
        # time.sleep(1)

    def unfollow(self, count):
        driver.get(following)
        time.sleep(5)
        try:
            try:
                for i in range(1, 20):
                    driver.find_element_by_xpath('(//*[@class="avatar-card-menu"])['+str(i)+']').click()
                    driver.find_element_by_xpath('//*[@id="avatar-card-dropdown-menu"]/div[2]/ul/li/a').click()
                    time.sleep(1)
                    print("Unfollowed: " + str(count))
                    count += 1
            except:
                driver.find_element_by_xpath('//*[@id="friends-container"]/div/div[2]/div/div/div[2]/ul/li[3]/button/span').click()
                roblox.unfollow(count)
        except Exception as error:
            print(error)
            print("Unfollowed Everyone!")


roblox = User()
print("[!] Logging in...")
roblox.login()
print("[+] Logged in!")
roblox.unfollow(count)
print("done!")