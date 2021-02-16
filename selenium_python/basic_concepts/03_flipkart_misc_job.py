from selenium import webdriver                        #importing webdriver module
from selenium.webdriver.common.keys import Keys
import time                                           #importing time module 

driver = webdriver.Chrome(executable_path="D:\webdrivers\chromedriver\chromedriver_win32\chromedriver.exe")  # driver path

driver.maximize_window()     # maximizes active window

driver.get("http://www.flipkart.com")  # opens desired window
time.sleep(3)         # gives delay before proceding further
print(driver.title)   # prints title of the page

driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()   # Skipping login by clicking close popup window

time.sleep(3)
mob = driver.find_element_by_xpath("//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input").send_keys("mobile",Keys.ENTER)      # input "mobile" word in searchbox and presses Enter Key

time.sleep(10)
driver.back()      # navigates to back page
time.sleep(10)
driver.forward()   # navigates to next page

time.sleep(10)
#driver.close()     # Closing the web browser
driver.quit()     # closes all web pages