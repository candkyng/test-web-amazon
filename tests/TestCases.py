import unittest
import HtmlTestRunner
import time
from resources.TestData import TestData
from resources.Locators import Locators
from pageObjects.Pages import HomePage,SearchResultsPage,ProductDetailsPage,SubCartPage,CartPage
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class AMZNTestCase(unittest.TestCase):

    url_home = "http://www.amazon.ca"

    def setUp(self):
        chrome_options=webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(options=chrome_options) # chromedriver.exe location should be in PATH environment variable
    
    def test_TC001_load_website(self):
        """Ensure Amazon home page is loaded"""
        self.homepage = HomePage(self.driver)
        self.assertIn(TestData.HOME_PAGE_TITLE,self.homepage.driver.title,msg="Page title does not contain 'Amazon'")
    
    def test_TC002_search(self):
        """Ensure user can perform a search"""
        self.homepage = HomePage(self.driver)       
        self.homepage.search()
        title = TestData.HOME_PAGE_TITLE + " : " + TestData.SEARCH_TERM
        
        self.assertIn(title,self.homepage.driver.title,"Page not load properly.")
        self.assertNotIn(TestData.NO_RESULTS_TEXT, self.homepage.driver.page_source ,"No Search result.")
    
    def test_TC003_add_to_cart(self):
        """Ensure user can add the first item to cart"""
        self.homepage = HomePage(self.driver)       
        self.homepage.search()
        self.search_result_page = SearchResultsPage(self.homepage.driver)
        self.search_result_page.click_search_result()
        self.product_detail_page = ProductDetailsPage(self.search_result_page.driver)
        self.product_detail_page.click_add_to_cart_button()
        self.sub_cart_page = SubCartPage(self.product_detail_page.driver)
        
        self.assertEqual(self.sub_cart_page.cartCount,1)        
        self.assertTrue(self.sub_cart_page.is_visible(Locators.SUB_CART_DIV))
        self.assertTrue(self.sub_cart_page.is_enabled(Locators.PROCEED_TO_BUY_BUTTON))
        
  
    def test_TC004_delete_item_in_cart(self):
        """Ensure user delete item from cart"""
        self.homepage = HomePage(self.driver)       
        self.homepage.search()
        self.search_result_page = SearchResultsPage(self.homepage.driver)
        self.search_result_page.click_search_result()
        self.product_detail_page = ProductDetailsPage(self.search_result_page.driver)
        self.product_detail_page.click_add_to_cart_button()
        self.sub_cart_page = SubCartPage(self.product_detail_page.driver)
        self.sub_cart_page.click_cart_button()
        self.cart_page = CartPage(self.sub_cart_page.driver)
        self.cart_page.delete_item()        
        
        # Ensure the cart is empty when the deleted item was the last item
        self.assertIn(TestData.EMPTY_CART_TEXT,self.cart_page.driver.page_source)
   
    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__=="__main__":      
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports',report_title="Test Results"))