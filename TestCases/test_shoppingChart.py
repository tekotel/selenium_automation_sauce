import unittest
from Base import InitiateDriver
from Pages import LoginPage,addtocartPage
from Library import read_config
import time


class ShoppingChart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = InitiateDriver.StartBrowser()
        cls.login_page = LoginPage(cls.browser)     
        cls.cart_page = addtocartPage.ShoppingChartPage(cls.browser)

        cls.username = read_config("Credentials_standard", "username")
        cls.password = read_config("Credentials_standard", "password")

        cls.login_page.enter_username(cls.username)
        cls.login_page.enter_password(cls.password)
        cls.login_page.click_login()
        assert cls.login_page.is_login_successfull(), "Login Sukses!"
        time.sleep(5)

    
    def test_success_shopping(self):
        self.cart_page.add_cart()

        # Arahkan ke shopping cart dan verifikasi jumlah barang
        self.cart_page.go_to_cart()
        cart_count = self.cart_page.confirm_co()
        self.assertEqual(cart_count, 2, "Jumlah item di cart tidak sesuai!")

        
    @classmethod   
    def tearDownClass(cls):
        InitiateDriver.CloseBrowser()

if __name__ == '__main__':
    unittest.main()
    
    
    

    
    
    