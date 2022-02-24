import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="D:\chromedriver_win32 (8)\chromedriver.exe")

driver.get("https://blueimp.github.io/jQuery-File-Upload/")

driver.find_element_by_xpath("//input[@type='file']").send_keys("D:\\Fita class\\Selenium Python\\amazon.png")

