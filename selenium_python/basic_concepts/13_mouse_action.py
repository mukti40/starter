from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="D:\webdrivers\chromedriver\chromedriver_win32\chromedriver.exe")

driver.maximize_window()

driver.get("http://www.flipkart.com")  
time.sleep(2)      
driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()

time.sleep(2)      

s1 = driver.find_element_by_xpath("//*[@id='container']/div/div[2]/div/div/span[1]")
s2 = driver.find_element_by_xpath("//*[@id='container']/div/div[2]/div/div/div/div[1]/a[6]")

actions = ActionChains(driver)

actions.move_to_element(s1).move_to_element(s2).click().perform() ## ---- mouse hover action -------

actions.double_click(s1).perform()  ##  ----- mouse Double Click -------

actions.context_click(s1).perform()   ##  ------ mouse Righr Click ------

source = driver.find_element_by_xpath("----")  # sorce object element
destination = driver.find_element_by_xpath("-----") # destination location element
actions.drag_and_drop(source,destination).perform()  ##  -------- Drag and drop using mouse ---------


driver.close()
