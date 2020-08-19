import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class AMZNTestCase(unittest.TestCase):

    url_home = "http://www.amazon.ca"

    def setUp(self):
        self.driver = webdriver.Chrome() # chromedriver.exe location should be in PATH environment variable
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_TC001_load_website(self):
        """Ensure Amazon home page is loaded"""
        self.driver.get(self.url_home)
        self.assertIn("Amazon",self.driver.title,msg="Page title does not contain 'Amazon'")

    def test_TC002_search(self):
        """Ensure user can perform a search"""
        driver=self.driver
        driver.get(self.url_home)
        search_term="Selenium with Python"
        search_input_box=driver.find_element_by_id("twotabsearchtextbox")
        search_input_box.send_keys(search_term + Keys.RETURN)

        self.assertIn(f"Amazon.ca : {search_term}",driver.title,"Page not load properly.")
        self.assertNotIn(f"No results for {search_term}",driver.page_source,"No Search result.")

    def tearDown(self):
        self.driver.close()

if __name__=="__main__":      
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports',report_title="Test Results"))