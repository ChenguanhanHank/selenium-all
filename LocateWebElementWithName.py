from selenium import webdriver
import time

path ="C:\\Programs\\Python36\\chromedriver.exe"

driver = webdriver.Chrome(path)
driver.get("http://kennethhutw.github.io/demo/Selenium/index.html")

signup = driver.find_element_by_name("signup")
signup.click()
time.sleep(2)
driver.back()
time.sleep(2)


signin = driver.find_element_by_name("signin")
signin.click()
time.sleep(2)

driver.close()
driver.quit()

