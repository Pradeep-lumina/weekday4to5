import unittest

from selenium import webdriver


class Google(unittest.TestCase):
    def test_google(self):
        self.driver = webdriver.Chrome(executable_path="D:\chromedriver_win32 (11)\chromedriver.exe")

        self.driver.get("http://www.gmail.com/")

        self.driver.maximize_window()

        print("The title of the page is " + self.driver.title)

        self.driver.close()

    def test_facebook(self):
        self.driver = webdriver.Chrome(executable_path="D:\chromedriver_win32 (11)\chromedriver.exe")

        self.driver.get("http://www.facebook.com/")

        self.driver.maximize_window()

        print("The title of the page is " + self.driver.title)

        self.driver.close()

if __name__ == "__main__":
    unittest.main()
