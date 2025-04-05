from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
import time

browsers = ["chrome","firefox","edge"]

# Inisialisasi Browser dengan Looping For

for browser in browsers: #for n <=5
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu") # untuk stabilitas
        options.add_argument("--window-size=1920,1080") 
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    elif browser == "edge":
        options = EdgeOptions()
        options.add_argument("--headless")
        driver = webdriver.Edge(options=options)

    try:
        # Buka halaman login
        driver.get('https://www.saucedemo.com')

        # Assert Browser Title
        assert 'Swag Labs' in driver.title
        print("Website opened successfully")

        # Fitur Login
        # Isi username dan password
        driver.find_element(By.ID, "user-name").send_keys('standard_user')
        driver.find_element(By.CSS_SELECTOR,'[data-test="password"]').send_keys('secret_sauce')

        # Klik tombol login
        driver.find_element(By.ID, "login-button").click()

        # Verifikasi login berhasil dengan URL assertion
        expected_url = "https://www.saucedemo.com/inventory.html"
    
        if driver.current_url != expected_url:
            raise AssertionError(f"URL tidak sesuai. Expected URL: {expected_url}, Current URL: {driver.current_url}")

        # Print login menggunakan browser tertentu sesuai dengan urutan variabel
        print(f"Login Berhasil! with browser {browser}")

    except NoSuchElementException as e:
        print(f"Element tidak ditemukan: {e}")

    except AssertionError as e:
        print(f"Assertion Error: {e}")
    
    except WebDriverException as e:
        print(f"Webdriver Error: {e}")

    finally:
        time.sleep(2)
        driver.quit()
