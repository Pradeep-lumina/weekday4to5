import unittest

from selenium import webdriver


class Google(unittest.TestCase):
    def test_google(self):
        self.driver = webdriver.Chrome(executable_path="D:\chromedriver_win32 (11)\chromedriver.exe")

        self.driver.get("http://www.gmail.com/")

        self.driver.maximize_window()

        title = self.driver.title

        #self.assertEqual("Gmails", title)

        #self.assertNotEqual("Gmails", title)

        #self.assertTrue(title == "Gmails")

        #self.assertFalse(title =="Gmails")

        #self.driver = None

        #self.assertIsNone(self.driver)

        #self.assertIsNotNone(self.driver)

        list={"python", "selenium", "fita"}

        #self.assertIn("Python",list)

        #self.assertNotIn("Python", list)

        self.assertLess(10, 100)
        self.assertLessEqual(100, 100)

        self.assertGreater(101, 100)
        self.assertGreaterEqual(100, 100)


if __name__ == "__main__":
    unittest.main()
