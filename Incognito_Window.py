import time

from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.ChromeOptions()

browser.add_argument("--incognito")

driver = webdriver.Chrome(executable_path="D:\chromedriver_win32 (8)\chromedriver.exe", options=browser)

driver.get("https://blueimp.github.io/jQuery-File-Upload/")