import unittest
from Base import InitiateDriver
from Pages import LoginPage
from Library import read_config
from selenium.webdriver.common.by import By
import time

class TestLoginUnSuccess(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = InitiateDriver.StartBrowser()
        cls.login_page = LoginPage(cls.browser)        

    
    def test_failed1(self):
     self.login_page.test_failed_login1()

     # Verifikasi login failed dengan URL assertion
     error_message = self.browser.find_element(By.CSS_SELECTOR,'[data-test="error"]').text
     self.assertIn('Epic sadface: Username and password do not match any user in this service', error_message)
     time.sleep(5)
     print("Website logged in failed : need valid password / username")
     self.browser.quit()
    

    def test_failed2(self):
     self.login_page.test_failed_login2()
      # Verifikasi login failed dengan URL assertion
     error_message = self.browser.find_element(By.CSS_SELECTOR,'[data-test="error"]').text
     self.assertIn('Epic sadface: Username is required', error_message)
     time.sleep(5)
 
     print("Website logged in failed : need to be filled in")
    #  self.browser.quit()
 
        
    @classmethod   
    def tearDownClass(cls): 
        InitiateDriver.CloseBrowser()

if __name__ == '__main__':
    unittest.main()
    
    
    

    
    
    