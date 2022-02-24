import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path="D:\chromedriver_win32 (8)\chromedriver.exe")

driver.get("http://shareselenium.herokuapp.com/DropDown.html")

driver.maximize_window()

drp = Select(driver.find_element_by_id("dropdown1"))
drp.select_by_index(1)

element = driver.find_element_by_name("dropdown2")
drp1 = Select(element)
drp1.select_by_value("2")

drp2 = Select(driver.find_element_by_id("dropdown3"))
drp2.select_by_visible_text("UFT/QTP")


print(len(drp.options))


all_options = drp.options

for option in all_options:
     print(option.text)

