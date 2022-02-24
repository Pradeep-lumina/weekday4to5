import unittest
from selenium import webdriver
import HtmlTestRunner

class OrangeHRMTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path="D:\chromedriver_win32 (11)\chromedriver.exe")
        cls.driver.maximize_window()

    def test_homePage(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.assertEqual("OrangeHRM", self.driver.title)

    def test_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        self.assertEqual("OrangeHRM", self.driver.title)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()

if __name__=='__main__':
    #unittest.main()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C://Users\wellcome\PycharmProjects\weekday4to5\Reports'))