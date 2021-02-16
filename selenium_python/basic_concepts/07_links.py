from selenium import webdriver                       
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path="D:\webdrivers\chromedriver\chromedriver_win32\chromedriver.exe")  # driver path

driver.maximize_window()

driver.get("http://www.mercurytouroperator.com/")  
time.sleep(2)

links = driver.find_elements_by_tag_name("a")
print("number of links are :",len(links))

for link in links:       # printing all links in the webpage one by one
    print(link.text)

driver.find_element_by_link_text("Contact Us").click()       # using link text
time.sleep(2)

driver.back()
time.sleep(2)
driver.find_element_by_partial_link_text("CONDITIONS").click()  # using partial link text

time.sleep(5)
driver.close()