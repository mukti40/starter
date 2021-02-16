from selenium import webdriver                       
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path="D:\webdrivers\chromedriver\chromedriver_win32\chromedriver.exe")  # driver path

driver.maximize_window()

driver.get("http://www.flipkart.com")  
time.sleep(2)      
driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()

time.sleep(3)
driver.find_element_by_name("q").send_keys("football",Keys.ENTER)

time.sleep(5)
#tbox = driver.find_element_by_class_name("col-12-12 _1MRYA1").send_keys("football")
#drp=Select(tbox)
#time.sleep(2)
#drp.select_by_visible_text("football boots")

driver.close()

