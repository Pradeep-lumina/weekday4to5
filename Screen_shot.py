import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="D:\chromedriver_win32 (8)\chromedriver.exe")

driver.get("https://amazon.in")

driver.maximize_window()

driver.save_screenshot("D:\\Fita class\\Selenium Python\\amazon.png")

#driver.get_screenshot_as_file("D:\\Fita class\\Selenium Python\\amazon.png")