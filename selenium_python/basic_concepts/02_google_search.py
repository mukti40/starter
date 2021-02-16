from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="D:\webdrivers\chromedriver\chromedriver_win32\chromedriver.exe")

driver.maximize_window()

driver.get("http://www.google.com")
time.sleep(5)
print(driver.title)

driver.find_element_by_name("q").send_keys("mobile")

driver.close()