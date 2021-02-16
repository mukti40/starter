from selenium import webdriver                       
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path="D:\webdrivers\chromedriver\chromedriver_win32\chromedriver.exe")

driver.maximize_window()

driver.get("https://www.expedia.com/")  
time.sleep(2)

driver.find_element(By.XPATH,"//*[@id='uitk-tabs-button-container']/li[2]/a").click()
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='wizard-flight-tab-roundtrip']/div[2]/div[1]/div/div[1]/div/div/div/button").send_keys("SFO")
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='wizard-flight-tab-roundtrip']/div[2]/div[1]/div/div[2]/div/div/div/button").send_keys("NYC")
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='wizard-flight-pwa-1']/div[3]/div[2]/button").click()
time.sleep(5)

#driver.implicitly_wait(10)         # wait until the time expire is aplicable to all elements of the webpage

wait=WebDriverWait(driver,10)
element = wait.until(EC.element_to_be_clickable(By.ID,"stops-0"))
element.click()

time.sleep(5)
driver.quit()
