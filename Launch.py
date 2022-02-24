from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\chromedriver_win32 (8)\chromedriver.exe")


#driver = webdriver.Firefox(executable_path="D:\geckodriver-v0.30.0-win64 (3)\geckodriver.exe")


driver.maximize_window()

driver.get("https://www.facebook.com/")

#driver.get("http://shareselenium.herokuapp.com/CheckBox.html")

#driver.find_element_by_id("email").send_keys("Testing")

#driver.find_element(By.ID,'email').send_keys("Testing id")

#driver.find_element_by_name("pass").send_keys("Testing name")

#driver.find_element(By.NAME, 'pass').send_keys("Test Name")

#driver.find_element_by_class_name("inputtext _55r1 _6luy").send_keys("Test class name")

#driver.find_element_by_tag_name("button").click()

#driver.find_element_by_link_text("Forgotten password?").click()

#driver.find_element_by_partial_link_text("Forgotten password").click()

#driver.find_element_by_css_selector("input[class='inputtext _55r1 _6luy']").send_keys("testing css selector")

#driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input").send_keys("testing absolute xpath")

#driver.find_element_by_xpath("//input[@class='inputtext _55r1 _6luy']").send_keys("testing xpath")

#driver.find_element_by_xpath("(//input[@type='checkbox'])[5]").click()

forgot_password = driver.find_element_by_xpath("//a[text()='Forgotten password?']")
forgot_password.click()

