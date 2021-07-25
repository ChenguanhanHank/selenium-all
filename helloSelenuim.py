from selenium import webdriver

path = "C:\\Programs\\Python36\\chromedriver.exe"

driver = webdriver.Chrome(path)

driver.get("http://www.yahoo.com")

print(driver.current_url)
print(driver.title)

driver.close()
driver.quit()