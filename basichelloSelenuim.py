from selenium import webdriver

path ="C:\\Programs\\Python36\\chromedriver.exe"

driver = webdriver.Chrome(path)
driver.get("https://www.google.com")

print(driver.current_url)
print(driver.title)

print("navigrating to www.yahoo.com")
driver.get("http://www.yahoo.com")
print(driver.current_url)
print(driver.title)

print("going back to www.google.com")
driver.back()
print(driver.current_url)
print(driver.title)

print("going formard to www.yahoo.com")
driver.forward()
print(driver.current_url)
print(driver.title)


driver.close()
driver.quit()