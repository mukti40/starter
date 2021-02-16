import openpyxl
import XLUtils
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="D:\webdrivers\chromedriver\chromedriver_win32\chromedriver.exe")

driver.maximize_window()

driver.get("https://www.facebook.com/")
time.sleep(3)

path = "D:/Users/Mukesh/Desktop/selenium_python/basic_concepts/data_2.xlsx"

rows = XLUtils.getRowCount(path,'Sheet1')
for r in range(2,rows+1):
    username=XLUtils.readData(path,"Sheet1",r,1)
    password=XLUtils.readData(path,"Sheet1",r,2)

    driver.find_element_by_id("email").send_keys(username)
    driver.find_element_by_id("pass").send_keys(password)
    driver.find_element_by_xpath("//*[@id='u_0_b']").click()

    print(driver.title)

    time.sleep(10)

    if driver.title=="login success":
        print("pass")
        XLUtils.writeData(path,"Sheet1",r,3,"pass")
    else:
        print("fail")
        XLUtils.writeData(path,"Sheet1",r,3,"fail")
    
    time.sleep(10)
    driver.back()
    time.sleep(3)
    driver.find_element_by_id("email").clear()

driver.close()