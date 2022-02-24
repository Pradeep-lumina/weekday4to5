import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="D:\chromedriver_win32 (8)\chromedriver.exe")

driver.get("https://demoqa.com/menu")

driver.maximize_window()

driver.find_element_by_id("details-button").click()

driver.find_element_by_id("proceed-link").click()

element = driver.find_element_by_xpath("//a[text()='Main Item 2']")

action = ActionChains(driver)

action.move_to_element(element).perform()