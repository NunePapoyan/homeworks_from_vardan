from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
op = Options()
op.add_extension('/Users/Nune/Downloads/I-don-t-care-about-cookies.crx')
driver = webdriver.Chrome(options=op)
driver.get("https://www.youtube.com/")
searchFieldElement = driver.find_element(By.NAME, 'search_query')
searchFieldElement.send_keys("Sweden")
searchFieldElement.send_keys(Keys.ENTER)
time.sleep(10)
driver.close()