from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="D:\webdrivers\chromedriver\chromedriver_win32\chromedriver.exe")

driver.maximize_window()

driver.get("http://www.flipkart.com")
time.sleep(3)

driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()

#driver.get_screenshot_as_file("D:/Users/Mukesh/Desktop/selenium_python/basic_concepts/image1.png")

driver.save_screenshot("D:/Users/Mukesh/Desktop/selenium_python/basic_concepts/image1.png")

#driver.get_screenshot_as_png()

driver.close()