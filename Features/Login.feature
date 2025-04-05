Feature: Login ke SauceDemo

  Scenario: Login berhasil dengan kredensial yang valid
    Given pengguna berada di halaman login SauceDemo
    When pengguna memasukkan username "standard_user" dan password "secret_sauce"
    And pengguna menekan tombol login
    Then pengguna berhasil masuk ke halaman utama
