import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="D:\chromedriver_win32 (8)\chromedriver.exe")

driver.get("https://amazon.in")

driver.maximize_window()

#driver.execute_script("window.scrollBy(0,1000)","")

element = driver.find_element_by_xpath("(//img[@class='product-image'])[76]")

#driver.execute_script("arguments[0].scrollIntoView();", element)

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

