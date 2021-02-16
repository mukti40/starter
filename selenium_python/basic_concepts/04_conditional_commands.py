from selenium import webdriver                       
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="D:\webdrivers\chromedriver\chromedriver_win32\chromedriver.exe")  # driver path

driver.maximize_window()

driver.get("http://www.flipkart.com")  
time.sleep(2)      

driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()

time.sleep(3)
element = driver.find_element_by_name("q")
print(element.is_displayed())       # returnes status on the element is displayed or not as True or False
print(element.is_enabled())         # returnes status on the element is enabled or not as True or False
print(element.is_selected())        # returnes status on the element is selected or not as True or False

driver.close()