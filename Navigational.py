import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\chromedriver_win32 (8)\chromedriver.exe")

driver.maximize_window()

driver.get("https://www.facebook.com/")

driver.get("https://www.gmail.com/")

driver.back()
print(driver.title)

driver.forward()
print(driver.title)

driver.refresh()

