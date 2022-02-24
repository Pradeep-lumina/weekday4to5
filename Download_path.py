import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromeOptions = Options()

chromeOptions.add_experimental_option("prefs",{"download.default_directory":"D:\Fita class\Selenium Python"})

driver = webdriver.Chrome(executable_path="D:\chromedriver_win32 (8)\chromedriver.exe", chrome_options=chromeOptions)

driver.get("http://demo.automationtesting.in/FileDownload.html")

driver.maximize_window()

driver.find_element_by_id("textbox").send_keys("Download file")
time.sleep(2)

driver.find_element_by_id("createTxt").click()
time.sleep(2)

driver.find_element_by_id("link-to-download").click()