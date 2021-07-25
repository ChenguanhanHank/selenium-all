from selenium import webdriver
import time

path ="C:\\Programs\\Python36\\chromedriver.exe"

driver = webdriver.Chrome(path)
driver.get("http://kennethhutw.github.io/demo/Selenium/index.html")

driver.find_element_by_partial_link_text("up").click()
time.sleep(2)
driver.back()
time.sleep(2)


driver.find_element_by_partial_link_text("in").click()
time.sleep(3)

driver.close()
driver.quit()

