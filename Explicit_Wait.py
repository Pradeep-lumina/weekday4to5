import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path="D:\chromedriver_win32 (8)\chromedriver.exe")

driver.get("http://shareselenium.herokuapp.com/RadioButton.html")

wait = WebDriverWait(driver, 30)

wait.until(EC.visibility_of_element_located(By.ID, "value")).click()