import unittest 
from selenium import webdriver

class Test(unittest.TestCase):      # inherit TestCase Class and create a new test class
	def testName(self):
		
		#driver = webdriver.Chrome(executable_path = "D:\webdrivers\chromedriver\chromedriver_win32\chromedriver.exe")
		#driver.get("http://www.python.org")
        
		#self.assertEqual("Python",driver.title,"Webpage title are not same")

		#self.assertNotEqual("Python",driver.title)

		#self.assertTrue(driver.title=="Python")    # returns true or false

		#self.assertFalse(driver.title=="Python")    # returns true or false

		#self.assertIsNone(driver)    # returns true or false

		#self.assertIsNotNone(driver)    # returns true or false

		self.assertGreater(100,10)       # 1st no. greater than 2nd no.
		self.assertGreaterEqual(10,10)   # 1st no. greater than or equal to 2nd no.
		self.assertLess(10,100)          # 1st no. less than 2nd no.
		self.assertLessEqual(10,100)     # 1st no. less than or equal to 2nd no.

	#def testlist(self):
		#list={"python","java","ruby"}

		#self.assertIn("python",list)   # search a value is present inside a list/set/tupple/dictionary
		#self.assertNotIn("pearl",list)   # search a value is not present inside a list/set/tupple/dictionary

	



if __name__ == "__main__":
	unittest.main() 