from selenium import webdriver
from selenium.webdriver.common.by import By

# Inisiasi web driver
driver = webdriver.Chrome()

# Open browser
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
driver.maximize_window()
assert "Web form" in driver.title
print("Website opened successfully")

driver.implicitly_wait(1) #0.5 detik

# Cari elemen form
driver.find_element(By.NAME,"my-text").send_keys("Selenium")
driver.find_element(By.CSS_SELECTOR,".btn").click()
message = driver.find_element(By.ID,"message").text
assert "Received!" in message
print("Submit test successfully")

# Menutup browser
driver.quit()




