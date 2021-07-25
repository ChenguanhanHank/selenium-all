from selenium import webdriver
import time

path ="C:\\Programs\\Python36\\chromedriver.exe"

driver = webdriver.Chrome(path)
driver.get("http://kennethhutw.github.io/demo/Selenium/index.html")

signup = driver.find_element_by_class_name("btn-primary")
signup.click()
time.sleep(2)
driver.back()
time.sleep(2)


signin = driver.find_element_by_class_name("btn-default")
signin.click()
time.sleep(3)

driver.close()
driver.quit()

