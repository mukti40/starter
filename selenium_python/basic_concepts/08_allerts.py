from selenium import webdriver                       
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path="D:\webdrivers\chromedriver\chromedriver_win32\chromedriver.exe")

driver.maximize_window()

#driver.get("http://www.mercurytouroperator.com/")
#time.sleep(2)

driver.switch_to_alert().accept()     # Clicks ok button on the popup window when it appeares by any operation
driver.switch_to_alert().dismiss()    # Clicks cancel button on the popup window when it appeares by any operation
