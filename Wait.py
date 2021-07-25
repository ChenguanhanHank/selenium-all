from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

path ="C:\\Programs\\Python36\\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get('http://kennethhutw.github.io/demo/Selenium/bload.html')
#time.sleep(3)
#WebDriverWait(driver, 30). until(EC.element_to_be_clickable((By.ID,'bload')))
WebDriverWait(driver, 30). until(EC.visibility_of_element_located((By.ID,'bload')))

Aboutlink = driver.find_element_by_id('bload')
Aboutlink.click()

print(driver.current_url)
time.sleep(2)
driver.close()
driver.quit()