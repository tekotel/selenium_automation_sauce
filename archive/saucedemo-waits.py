from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inisialiasi WebDriver
browser = webdriver.Firefox()

# Inisialiasi Waits
wait = WebDriverWait(browser,10)

# Tunggu beberapa detik
browser.implicitly_wait(0.5) #0.5 detik

# Buka halaman login
browser.get('https://www.saucedemo.com')

# Assert Browser Title
assert 'Swag Labs' in browser.title

print("Website opened successfully")

# Fitur Login
# Isi username dan password
login_element = wait.until(EC.presence_of_element_located((By.ID,"user-name"))) #explicity waits
login_element.send_keys('standard_user')

#browser.find_element(By.ID, "user-name").send_keys('standard_user')
browser.find_element(By.CSS_SELECTOR,'[data-test="password"]').send_keys('secret_sauce')

# Klik tombol login
browser.find_element(By.ID, "login-button").click()

# Verifikasi login berhasil dengan URL assertion
expected_url = "https://www.saucedemo.com/inventory.html"
assert browser.current_url == expected_url, f"URL tidak sesuai. Expected URL: {expected_url}, Current URL: {browser.current_url}"

print("Website logged in successfully")

# Add to Cart
add_to_cart_button = browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
add_to_cart_button.click()

print("Success add to cart")

# Verifikasi berhasil ditambahkan ke keranjang
cart_badge = browser.find_element(By.CLASS_NAME,"shopping_cart_badge")
assert cart_badge.text == "1"

print("Add to cart assertion successful")

# Checkout Fitur 
# Klik ikon keranjang
browser.find_element(By.CLASS_NAME,"shopping_cart_link").click()

# Verifikasi berhasil diarahkan ke halaman cart 
expected_url = "https://www.saucedemo.com/cart.html"
assert browser.current_url == expected_url, f"URL tidak sesuai. Expected URL: {expected_url}, Current URL: {browser.current_url}"

# Klik tombol checkout
browser.find_element(By.ID,"checkout").click()

# Verifikasi berhasil diarahkan ke halaman checkout 
expected_url = "https://www.saucedemo.com/checkout-step-one.html"
assert browser.current_url == expected_url, f"URL tidak sesuai. Expected URL: {expected_url}, Current URL: {browser.current_url}"

# Isi informasi Checkout
browser.find_element(By.ID,"first-name").send_keys("Maya")
browser.find_element(By.ID,"last-name").send_keys("Maulani")
browser.find_element(By.ID,"postal-code").send_keys("12345")
browser.find_element(By.ID,"continue").click()

# Verifikasi berhasil diarahkan ke halaman checkout overview
expected_url = "https://www.saucedemo.com/checkout-step-two.html"
assert browser.current_url == expected_url, f"URL tidak sesuai. Expected URL: {expected_url}, Current URL: {browser.current_url}"

# Klik tombol Finish
browser.find_element(By.ID,"finish").click()

# Verifikasi checkout berhasil
message = browser.find_element(By.CLASS_NAME,"complete-header")
assert message.text == "Thank you for your order!"

# Tutup browser
browser.quit()






