import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="D:\chromedriver_win32 (8)\chromedriver.exe")

driver.get("https://www.gmail.com")

driver.maximize_window()

maintab = driver.current_window_handle

print(maintab)

help = driver.find_element_by_xpath("//a[text()='Help']")
help.click()

tabs = driver.window_handles

print(tabs)

for tab in tabs:
     driver.switch_to.window(tab)
     title = driver.title
     print(title)
     if title == "Google Account Help":
         element = driver.find_element_by_xpath("//a[text()='Create a Google Account']")
         element.click()
