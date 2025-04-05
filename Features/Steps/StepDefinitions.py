from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given('pengguna berada di halaman login SauceDemo')
def step_given_pengguna_di_halaman_login(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")

@when('pengguna memasukkan username "{username}" dan password "{password}"')
def step_when_pengguna_memasukkan_kredensial(context, username, password):
    context.driver.find_element(By.ID, "user-name").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)
    

@when('pengguna menekan tombol login')
def step_when_pengguna_menekan_tombol_login(context):
    context.driver.find_element(By.ID, "login-button").click()
    time.sleep(2)  # Tunggu sebentar untuk memastikan halaman dimuat

@then('pengguna berhasil masuk ke halaman utama')
def step_then_pengguna_berhasil_login(context):
    assert "inventory" in context.driver.current_url
    context.driver.quit()
