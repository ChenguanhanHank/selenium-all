from selenium import webdriver
import time
path = "C:\\Programs\\Python36\\chromedriver.exe"

driver = webdriver.Chrome(path)

driver.get("https://www.facebook.com/")

#first name
driver.find_element_by_xpath('//*[@id="u_0_i"]').send_keys('Kenneth')
#surname
driver.find_element_by_xpath('//*[@id="u_0_k"]').send_keys('Hu')
#button
driver.find_element_by_xpath('//*[@id="u_0_10"]').click()
time.sleep(3)
driver.close()
driver.quit()

