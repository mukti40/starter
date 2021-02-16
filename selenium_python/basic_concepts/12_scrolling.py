from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path="D:\webdrivers\chromedriver\chromedriver_win32\chromedriver.exe")

driver.maximize_window()

driver.get("https://en.wikipedia.org/wiki/Portal:Current_events")
time.sleep(2)

## 1. scrolling down page by pixel
driver.execute_script("window.scrollBy(0,1000)","")

time.sleep(5)

## 2. scrolling down the page till the element found
flag = driver.find_element_by_xpath("//*[@id='2021_January_3']/div[1]/div[1]")
driver.execute_script("arguments[0].scrollIntoView();",flag)

time.sleep(5)

## 3. scrolling to end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

time.sleep(5)

driver.close()