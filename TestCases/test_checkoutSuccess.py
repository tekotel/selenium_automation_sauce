import unittest
from Base import InitiateDriver
from Pages import LoginPage,addtocartPage,checkout
from Library import read_config
import time


class checkoutSuccess(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = InitiateDriver.StartBrowser()
        cls.login_page = LoginPage(cls.browser)     
        cls.cart_page = addtocartPage.ShoppingChartPage(cls.browser)
        cls.checout_page = checkout.checkoutSuccess(cls.browser)

        cls.username = read_config("Credentials_standard", "username")
        cls.password = read_config("Credentials_standard", "password")

        cls.login_page.enter_username(cls.username)
        cls.login_page.enter_password(cls.password)
        cls.login_page.click_login()
        assert cls.login_page.is_login_successfull(), "Login Sukses!"
        time.sleep(5)
        cls.cart_page.add_cart()
        cls.cart_page.go_to_cart()
        cls.cart_page.confirm_co()
        cls.cart_page.proceed_to_checkout()


    
    def test_checkout_success(self):
       self.checout_page.fill_in_information()
       self.checout_page.co_information()
       self.checout_page.next()
       self.checout_page.co_final()
       self.checout_page.finish()
       


        
    @classmethod   
    def tearDownClass(cls):
        InitiateDriver.CloseBrowser()

if __name__ == '__main__':
    unittest.main()
    
    
    

    
    
    