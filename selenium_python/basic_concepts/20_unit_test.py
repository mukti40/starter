import unittest
from selenium import webdriver

class SearchEngineTest(unittest.TestCase):    # Defining two tests in a single class using UNITTEST module
    def test_google(self):
        self.driver=webdriver.Chrome(executable_path="D:\webdrivers\chromedriver\chromedriver_win32\chromedriver.exe")
        self.driver.get("http://www.google.co.in")
        print("Title of the page is :" +self.driver.title)
        self.driver.close()

    def test_bing(self):
        self.driver=webdriver.Chrome(executable_path="D:\webdrivers\chromedriver\chromedriver_win32\chromedriver.exe")
        self.driver.get("http://www.bing.com")
        print("Title of the page is :" +self.driver.title)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
