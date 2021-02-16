from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import logging

driver = webdriver.Chrome(executable_path="D:\webdrivers\chromedriver\chromedriver_win32\chromedriver.exe")

driver.maximize_window()

driver.get("http://www.flipkart.com")
time.sleep(3)

driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()

logging.basicConfig(filename="D:/Users/Mukesh/Desktop/selenium_python/basic_concepts/test.log",
format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S:%p')

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("This is a debug message")
logger.info("This is a info")
logger.warning("This is a warning message")
logger.error("This is a error")
logger.critical("This is Critical")

driver.close()