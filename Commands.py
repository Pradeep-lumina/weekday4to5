import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\chromedriver_win32 (8)\chromedriver.exe")

driver.maximize_window()

driver.get("https://www.facebook.com/")

#print(driver.title)

title = driver.title
print(title)

current_url = driver.current_url
print(current_url)

page_source = driver.page_source
print(page_source)

user_name = driver.find_element_by_id("email")
user_name.send_keys("selenium")

#user_name.clear()

#driver.find_element_by_link_text("Forgotten password?").click()
#time.sleep(2)

#driver.find_element_by_link_text("Instagram").click()
#time.sleep(5)

#driver.quit()

texting = driver.find_element_by_xpath("//h2[@class='_8eso']")
#get_text = texting.text
#print(get_text)

print(texting.text)

print(user_name.get_attribute("value"))