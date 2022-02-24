import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="D:\chromedriver_win32 (8)\chromedriver.exe")

driver.get("https://demo.guru99.com/test/simple_context_menu.html")

driver.maximize_window()

element = driver.find_element_by_xpath("//button[text()='Double-Click Me To See Alert']")

Action=ActionChains(driver)
Action.double_click(element).perform()