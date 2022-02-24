import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="D:\chromedriver_win32 (8)\chromedriver.exe")

driver.get("https://blueimp.github.io/jQuery-File-Upload/")

cookies = driver.get_cookies()

print(len(cookies))

cookie = ({"name":"Mycookie","value":"123456457457"})

driver.add_cookie(cookie)

cookies = driver.get_cookies()

print(len(cookies))

print(cookies)

driver.delete_cookie("Mycookie")

cookies = driver.get_cookies()

print(len(cookies))


#driver.delete_all_cookies()

#cookies = driver.get_cookies()

#print(len(cookies))
