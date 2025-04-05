from selenium.webdriver.common.by import By
from Library import get_locator, read_config
from selenium.webdriver.common.action_chains import ActionChains
import time

class ShoppingChartPage:
    def __init__(self, browser):
        self.browser = browser

    def add_cart(self):
        self.browser.find_element(By.XPATH,"(//button[@id='add-to-cart-sauce-labs-backpack'])[1]").click()
        time.sleep(2)
        self.browser.find_element(By.XPATH,"(//button[@id='add-to-cart-sauce-labs-bike-light'])[1]").click()


    def go_to_cart(self):
        time.sleep(5)
        self.browser.find_element(By.XPATH,"(//a[@class='shopping_cart_link'])[1]").click()
    
    def confirm_co(self):
        time.sleep(5)
        try:
            cart_badge_locator = "shopping_cart_badge"
            cart_badge = self.browser.find_element(By.CLASS_NAME, cart_badge_locator)
            return int(cart_badge.text) if cart_badge else 0
        except:
            return 0
        


    def proceed_to_checkout(self):
        self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
        time.sleep(5)
        checkout_button_locator = "(//button[normalize-space()='Checkout'])[1]"
        self.browser.find_element(By.XPATH, checkout_button_locator).click()
    

    def co_oke(self):
        get_url = self.browser.current_url
        
        if '/cart.html'in get_url:
            print("Website Ccart successfully")
            return True
        else:
            print("Failed")
            return False
    
        
   
        




   