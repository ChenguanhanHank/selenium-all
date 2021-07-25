from selenium import webdriver
import time

path ="C:\\Programs\\Python36\\chromedriver.exe"

driver = webdriver.Chrome(path)
driver.get("http://kennethhutw.github.io/demo/Selenium/Signup.html")

username = driver.find_element_by_xpath('//input[@id="username"]')
username.send_keys('kenneth')
print(username.text)

psw = driver.find_element_by_xpath('//input[@id="password"]')
psw.send_keys('kenneth')
print(psw.text)

driver.find_elements_by_css_selector("input[type='radio'][value='Female']")[0].click()


country = driver.find_element_by_xpath('//select[@id="country"]/option[2]')
country.click()
print(country.text)

driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div[2]/form/div[5]/div/label[1]/input').click()
driver.find_element_by_id('dashboard').click()

time.sleep(3)
driver.find_element_by_id('signup').click()
driver.maximize_window()
time.sleep(2)



driver.close()
driver.quit()