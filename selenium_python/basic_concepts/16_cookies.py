from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="D:\webdrivers\chromedriver\chromedriver_win32\chromedriver.exe")

driver.maximize_window()

driver.get("http://www.flipkart.com")
time.sleep(3)

cookies = driver.get_cookies()

print("total number of cookies are :",len(cookies))

driver.delete_all_cookies()

cookie = {'name':'MyCookie','value':'12345678'}
driver.add_cookie(cookie)

print(cookies)

driver.delete_cookie('MyCookie')

driver.close()