import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\chromedriver_win32 (8)\chromedriver.exe")

driver.get("http://shareselenium.herokuapp.com/RadioButton.html")

driver.implicitly_wait(10)

driver.find_element_by_xpath("(//input[@type='radio'])[7]").click()