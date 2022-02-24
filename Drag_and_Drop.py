import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="D:\chromedriver_win32 (8)\chromedriver.exe")

driver.get("https://demo.guru99.com/test/drag_drop.html")

driver.maximize_window()

drag = driver.find_element_by_xpath("//a[text()=' BANK ']")

drop = driver.find_element_by_xpath("(//li[@class='placeholder'])[1]")

element = ActionChains(driver)

element.drag_and_drop(drag,drop).perform()