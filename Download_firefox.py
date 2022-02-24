from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

fp = webdriver.FirefoxProfile()

fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain,application/pdf")

fp.set_preference("browser.download.manager.showWhenStarting", False)

fp.set_preference("browser.download.dir", "D:\Fita class\Selenium Python")

fp.set_preference("browser.download.folderList",2)

fp.set_preference("pdfjs.disabled",True)

driver = webdriver.Firefox(executable_path="D:\geckodriver-v0.30.0-win64 (3)\geckodriver.exe", firefox_profile=fp)

driver.maximize_window()

driver.get("http://demo.automationtesting.in/FileDownload.html")

driver.find_element_by_id("textbox").send_keys("Download file")
time.sleep(2)

driver.find_element_by_id("createTxt").click()
time.sleep(2)

driver.find_element_by_id("link-to-download").click()
