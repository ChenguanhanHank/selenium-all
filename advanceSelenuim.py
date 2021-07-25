from selenium import webdriver
import time

path ="C:\\Programs\\Python36\\chromedriver.exe"

driver = webdriver.Chrome(path)
driver.get("https://www.google.com")

driver.refresh()
#maximize
driver.maximize_window()
print(driver.current_url)
print(driver.title)
time.sleep(3)

#resize
driver.set_window_size("1024","768")
print(driver.current_url)
print(driver.title)
time.sleep(3)

driver.close()
driver.quit()