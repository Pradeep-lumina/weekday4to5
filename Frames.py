import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="D:\chromedriver_win32 (8)\chromedriver.exe")

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

driver.maximize_window()

driver.switch_to.frame(2)

help = driver.find_element_by_xpath("(//a[text()='Help'])[1]")
help.click()

driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")

action = driver.find_element_by_xpath("//span[text()='Action']")
action.click()