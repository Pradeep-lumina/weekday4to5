import pytest
from selenium import webdriver

class TestOrangeTest():

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(executable_path="D:\chromedriver_win32 (11)\chromedriver.exe")
        self.driver.maximize_window()
        yield
        self.driver.close()

    def testhomepage(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        assert self.driver.title == "OrangeHRM"

    def testloginpage(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        assert self.driver.title == "OrangeHRM"
