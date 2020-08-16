from selenium import webdriver

url="http://www.amazon.ca"

driver=webdriver.Chrome() # chromedriver.exe location should be in PATH environment variable
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(url)
assert "Amazon" in driver.title
driver.close()