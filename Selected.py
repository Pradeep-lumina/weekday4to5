import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\chromedriver_win32 (8)\chromedriver.exe")

driver.maximize_window()

driver.get("http://shareselenium.herokuapp.com/RadioButton.html")

selected = driver.find_element_by_xpath("(//input[@type='radio'])[4]").is_selected()

print(selected)
