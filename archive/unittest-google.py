import unittest
from selenium import webdriver

class GoogleTestCase(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get("https://google.com")
        
    def test_page_title(self):
        self.assertEqual(self.browser.title, "Google")

    def test_page_title(self):
        self.assertIn("Google", self.browser.title)
    
    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()