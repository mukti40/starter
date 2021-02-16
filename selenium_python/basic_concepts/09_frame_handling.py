from selenium import webdriver                       
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path="D:\webdrivers\chromedriver\chromedriver_win32\chromedriver.exe")

driver.maximize_window()

#driver.get("http://......./")


#Switching between diferent frames in a single webpage
driver.switch_to.frame(".........")
driver.find_elements_by_link_text(".......").click()

#now steps to Switching to diferent frame item
driver.switch_to.default_content()
driver.switch_to.frame(".........")
driver.find_elements_by_link_text(".......").click()

