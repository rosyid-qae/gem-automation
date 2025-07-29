# test/test_login.py
import allure
from playwright.sync_api import sync_playwright
from page.login_page import LoginPage



def test_login_valid():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        page = browser.new_page()

        with allure.step("Buka halaman login"):
            page.goto('https://gem.goersapp.com', timeout=60000)

        with allure.step("Isi email dan password valid"):
            login = LoginPage(page)
            login.login_valid("userdua95@gmail.com", "testing02")

        with allure.step("Tunggu redirect setelah login"):
            try:
                # Tunggu maksimal 10 detik untuk redirect ke halaman lain
                page.wait_for_url("**/organization**", timeout=10000)
            except:
                print("⚠️ Halaman belum berpindah ke organization dalam 10 detik")

        with allure.step("Ambil screenshot setelah login"):
            page.screenshot(path="login_valid_result.png")
            allure.attach.file("login_valid_result.png", name="Login Berhasil", attachment_type=allure.attachment_type.PNG)

        with allure.step("Verifikasi halaman setelah login"):
            current_url = page.url
            print("📍 Current URL:", current_url)
            assert "organization" in current_url or "dashboard" in current_url, "Login gagal, tidak masuk dashboard/organization"

        browser.close()


def test_login_invalid():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        page = browser.new_page()

        with allure.step("Buka halaman login"):
            page.goto('https://gem.goersapp.com', timeout=60000)

        with allure.step("Isi email dan password salah"):
            login = LoginPage(page)
            login.login_invalid("usersatu96@gmail.com", "salahbanget")

        with allure.step("Coba ambil pesan error"):
            try:
                error_element = page.wait_for_selector("div.___alert__message", timeout=8000)
                error_message = error_element.inner_text()
            except:
                error_message = None

        with allure.step("Ambil screenshot hasil"):
            page.screenshot(path="login_invalid_result.png")
            allure.attach.file("login_invalid_result.png", name="Login Gagal", attachment_type=allure.attachment_type.PNG)

        with allure.step("Pastikan pesan error tampil"):
            assert error_message is not None, "Tidak menemukan pesan error"
            assert "tidak cocok" in error_message.lower(), "Pesan error tidak sesuai"

        browser.close()