from selenium.webdriver.common.by import By
from Library import get_locator, read_config
from selenium.webdriver.common.action_chains import ActionChains
import time
 

class checkoutSuccess:
    def __init__(self, browser):
        self.browser = browser

    def co_information(self):
        get_url = self.browser.current_url
        
        if '/checkout-step-one.html'in get_url:
            print("Website CO successfully")
            return True
        else:
            print("Failed")
            return False
    
    def fill_in_information(self):
        time.sleep(2)
        self.browser.find_element(By.XPATH,"(//input[@id='first-name'])[1]").send_keys("Amalia")
        time.sleep(2)
        self.browser.find_element(By.XPATH,"(//input[@id='last-name'])[1]").send_keys("Fi")
        time.sleep(2)
        self.browser.find_element(By.XPATH,"(//input[@id='postal-code'])[1]").send_keys(123456)

    def next(self):
        self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
        time.sleep(5)
        self.browser.find_element(By.XPATH,"(//input[@id='continue'])[1]").click()

    def confirm_co(self):
        time.sleep(2)
        self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
        time.sleep(2)
        item_total = self.browser.find_element(By.XPATH, "(//div[@class='summary_subtotal_label'])[1]")
        tax = self.browser.find_element(By.XPATH, "(//div[@class='summary_tax_label'])[1]")
        total = self.browser.find_element(By.XPATH, "(//div[@class='summary_total_label'])[1]")
        
        # Extract text and clean the numbers
        item_total = float(item_total.text.replace("Item total: $", ""))
        time.sleep(2)
        tax = float(tax.text.replace("Tax: $", ""))
        time.sleep(2)
        total_price = float(total.text.replace("Total: $", ""))
        
        # Assert that the total price is correct
        totalPrice = item_total + tax
        assert total_price == totalPrice, f"Mismatch! Expected {totalPrice}, but got {total_price}"
        
        return total_price
        
    
    def co_final(self):
        get_url = self.browser.current_url
        
        if '/checkout-step-two.html'in get_url:
            print("Checkout successfully")
            return True
        else:
            print("Failed")
            return False
    
    def finish(self):
        time.sleep(5)
        self.browser.find_element(By.XPATH,"(//button[normalize-space()='Finish'])[1]").click()
        time.sleep(5)
        
    
    
    
        
   
        




   