from selenium import webdriver                       
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path="D:\webdrivers\chromedriver\chromedriver_win32\chromedriver.exe")

driver.maximize_window()

driver.get("http://......./")

driver.find_elements_by_xpath(".....")
print(driver.current_window_handle)     # gives handle value of the current window

handles = driver.window_handles         # returnes all the handele values of the opened browser windows
for handle in  handles:
    driver.switch_to_window(handle)
    print(driver.title)

driver.quit()    # closes all the open windows