from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options    # for file downloading to desired location
import time

driver = webdriver.Chrome(executable_path="D:\webdrivers\chromedriver\chromedriver_win32\chromedriver.exe")

driver.maximize_window()

driver.get("http://www.flipkart.com")  
time.sleep(2)

   ##-------------Uploading a file---------------
driver.switch_to_frame(0)
driver.find_element_by_xpath("---file upload location---").send_keys("D://-----/---/----/xyz.jpg") # use forward slash'/'

   ##-----------Download a file------------------
driver.find_element_by_xpath("------").click()    # Clicking on download link

   ##-----------Download a file to desired location------------------
chromeOptions = Options()
chromeOptions.add_experimental_option("prefs",{"download.default_directory": "D:\\Desktop"})
driver = webdriver.Chrome(executable_path="D:\webdrivers\chromedriver\chromedriver_win32\chromedriver.exe",chrome_options=chromeOptions)      # additional class calling along with executable path.


   ##-----------Download a file to desired location(in Firefox)------------------
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","text/plain,application/pdf")  # mime type
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir","C:\Desktop")
fp.set_preference("browser.download.folderList",2)
fp.set_preference("pdfjs.disabled",True)

driver=webdriver.Firefox(executable_path="---geko driver path----",firefox_profile=fp) #extra class add to execut_path.

