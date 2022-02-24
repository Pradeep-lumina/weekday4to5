import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path="D:\chromedriver_win32 (8)\chromedriver.exe")

driver.get("http://shareselenium.herokuapp.com/Alerts.html")

driver.maximize_window()

element = driver.find_element_by_xpath("//button[text()='Alert Box']")
element.click()
time.sleep(5)

alert=driver.switch_to.alert
alert.accept()


confirm_box = driver.find_element_by_xpath("//button[text()='Confirm Box']")
confirm_box.click()
time.sleep(2)

alert.dismiss()

prompt_box = driver.find_element_by_xpath("//button[text()='Prompt Box']")
prompt_box.click()
time.sleep(2)

alert.send_keys("Automation")
alert.accept()