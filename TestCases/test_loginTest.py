import unittest
from Base import InitiateDriver
from Pages import LoginPage
from Library import read_config

class TestLoginSuccess(unittest.TestCase):
    credentials = [
        {"username": read_config("Credentials_standard", "username"),
         "password": read_config("Credentials_standard", "password")},
        {"username": read_config("Credentials_problem", "username"),
         "password": read_config("Credentials_problem", "password")},
        {"username": read_config("Credentials_visual", "username"),
         "password": read_config("Credentials_visual", "password")}
    ]


    @classmethod
    def setUpClass(cls):
        cls.browser = InitiateDriver.StartBrowser()
        cls.login_page = LoginPage(cls.browser)        

    
    def test_success_login(self):
        for username in self.credentials:
            with self.subTest(username=username["username"]):
                self.login_page.enter_username(username["username"])
                self.login_page.enter_password(username["password"])
                self.login_page.click_login()
        
                # Verifikasi login berhasil
                self.assertTrue(self.login_page.is_login_successfull())
                self.login_page.logout() 
                       
        
    @classmethod   
    def tearDownClass(cls): 
        InitiateDriver.CloseBrowser()

if __name__ == '__main__':
    unittest.main()
    
    
    

    
    
    