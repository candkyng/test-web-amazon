from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url="http://www.amazon.ca"
search_term="Selenium with Python"

driver=webdriver.Chrome() # chromedriver.exe location should be in PATH environment variable
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(url)
assert "Amazon" in driver.title

search_input_box=driver.find_element_by_id("twotabsearchtextbox")
search_input_box.send_keys(search_term)
search_input_box.send_keys(Keys.RETURN)

assert f"Amazon.ca : {search_term}" in driver.title
assert f"No results for {search_term}" not in driver.page_source

driver.close()