from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="D:\webdrivers\chromedriver\chromedriver_win32\chromedriver.exe")

driver.maximize_window()

driver.get("http://www.flipkart.com")
time.sleep(2)
print(driver.title)

#login by entering user id and password
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input").send_keys(9439749279)
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input").send_keys("manojyavam")
driver.find_element_by_xpath("(//*[@type='submit'])[2]").click()

time.sleep(10)
driver.find_element_by_name("q").send_keys("mobile",Keys.ENTER)
time.sleep(2)
#driver.find_element_by_xpath("//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/button").click()

time.sleep(10)
driver.close()     # Closing the web browser
