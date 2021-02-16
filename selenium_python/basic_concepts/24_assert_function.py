# import all required frameworks 
import unittest 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 

class PythonOrgSearch(unittest.TestCase):      # inherit TestCase Class and create a new test class

	def setUp(self): 
		self.driver = webdriver.Chrome(executable_path = "D:\webdrivers\chromedriver\chromedriver_win32\chromedriver.exe")

	def test_search_in_python_org(self):   # Test case method. It should always start with test_ 
		
		driver = self.driver   # get driver 
		driver.get("http://www.python.org") 

		self.assertIn("Python", driver.title)   # assertion to confirm if title has python keyword in it 

		elem = driver.find_element_by_name("q")   # locate element using name 
		elem.send_keys("pycon") 
		elem.send_keys(Keys.RETURN) 
		assert "No results found." not in driver.page_source

	def tearDown(self):   # cleanup method called after every test performed 
		self.driver.close() 

if __name__ == "__main__":   # execute the script 
	unittest.main() 
