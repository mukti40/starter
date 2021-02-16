from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path="D:\webdrivers\chromedriver\chromedriver_win32\chromedriver.exe")

driver.maximize_window()

driver.get("http://......./")

rows = len(driver.find_element_by_xpath("....")        # path common to all rows of table array and counts rows
columns = len(driver.find_element_by_xpath("....")        # path common to all rows of table array & counts columns

for r in range(2,rows+1):
    for c in range(1,columns+1):
        value = driver.find_element_by_xpath("....").text    # we have to replace r & c in respective row/column index no. place in the xpath
        print(value,end="    ")
    print()


