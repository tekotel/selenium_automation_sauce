from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless") # Aktifkan mode headless

# Inisialiasi WebDriver
browser = webdriver.Chrome(options=options)

# Buka halaman login
browser.get('https://www.saucedemo.com')

# Assert Browser Title
assert 'Swag Labs' in browser.title

print("Website opened successfully")

# Fitur Login
# Isi username dan password
browser.find_element(By.ID, "user-name").send_keys('standard_user')
browser.find_element(By.CSS_SELECTOR,'[data-test="password"]').send_keys('secret_sauce')

# Klik tombol login
browser.find_element(By.ID, "login-button").click()

# Verifikasi login berhasil dengan URL assertion
expected_url = "https://www.saucedemo.com/inventory.html"
assert browser.current_url == expected_url, f"URL tidak sesuai. Expected URL: {expected_url}, Current URL: {browser.current_url}"

print("Website logged in successfully")



