from selenium import webdriver
import time

path ="C:\\Programs\\Python36\\chromedriver.exe"

driver = webdriver.Chrome(path)
driver.get("http://kennethhutw.github.io/demo/Selenium/index.html")

driver.find_element_by_xpath("//a[@name='signup']").click()
time.sleep(2)
driver.back()
time.sleep(2)


driver.find_element_by_xpath("//a[@id='signin']").click()
time.sleep(3)

driver.close()
driver.quit()

