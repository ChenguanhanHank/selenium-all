from selenium import webdriver
import time

path ="C:\\Programs\\Python36\\chromedriver.exe"

driver = webdriver.Chrome(path)
driver.get("http://kennethhutw.github.io/demo/Selenium/Signin.html")

#part1
driver.find_element_by_id('Signin').click()
alert = driver.find_element_by_class_name('alert-danger')
print('sign in without username and password')
print(alert.text)
time.sleep(3)

driver.find_element_by_id('username').send_keys('kenneth')
driver.find_element_by_id('password').send_keys('password')
driver.find_element_by_id('Signin').click()
print('input corrected username and password')
success = driver.find_element_by_class_name('alert-success')
print(success.text)
time.sleep(3)


#part2
driver.find_element_by_id('password').clear()
driver.find_element_by_id('Signin').click()
alert = driver.find_element_by_class_name('alert-danger')
print('sign in without password')
print(alert.text)
time.sleep(3)

driver.refresh()
driver.find_element_by_id('password').send_keys('password')
driver.find_element_by_id('Signin').click()
alert = driver.find_element_by_class_name('alert-danger')
print('sign in without account')
print(alert.text)
time.sleep(3)

driver.refresh()
driver.find_element_by_id('username').send_keys('alan')
driver.find_element_by_id('password').send_keys('password')
driver.find_element_by_id('Signin').click()
print('input wrong')
danger = driver.find_element_by_class_name('alert-danger')
print(danger.text)
time.sleep(2)

#part 3
driver.find_element_by_id('username').clear()
driver.find_element_by_id('username').send_keys('kenneth')
time.sleep(2)
driver.find_element_by_id('dashboard').click()
driver.find_element_by_id('Signin').click()
time.sleep(2)
username = driver.find_element_by_xpath('//*[@id="username"]')
print('user : ' + username.text + ' login successfully! ')
time.sleep(2)
print('Pass!!')


driver.close()
driver.quit()