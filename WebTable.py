import time

import openpyxl

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="D:\chromedriver_win32 (11)\chromedriver.exe")

driver.get("http://shareselenium.herokuapp.com/WebTable.html")

driver.maximize_window()

table = driver.find_element_by_xpath("//table[@cellspacing='0']")

rows = table.find_elements_by_tag_name("tr")

print(len(rows))

for row in rows:
    cells = row.find_elements_by_tag_name("td")
    for cell in cells:
        print(cell.text)
