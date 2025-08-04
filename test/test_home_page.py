import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
import allure
from playwright.sync_api import sync_playwright
from page.login_page import LoginPage
from page.search_organization_page import SearchOrganizationPage
from page.home_page import HomePage


@pytest.fixture(scope="function")
def login_and_go_to_home():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        page = browser.new_page()
        page.goto("https://gem.goersapp.com")

        login = LoginPage(page)
        login.login_valid("userdua95@gmail.com", "testing02")

        search = SearchOrganizationPage(page)
        search.search_organization("SQA PROD")

        try:
            print("[DEBUG] Menunggu elemen Home muncul...")
            page.wait_for_selector("text=BUAT AKTIVITAS", timeout=5000)
            print("[DEBUG] Halaman Home berhasil dimuat")
        except:
            print("[WARNING] Halaman Home tidak berhasil dimuat")
            page.screenshot(path="debug_home_failed.png")
            raise

        yield page
        browser.close()


@allure.title("Klik tombol LIHAT membuka tab baru ke public page organisasi")
def test_click_button_lihat(login_and_go_to_home):
    page = login_and_go_to_home
    home = HomePage(page)

    popup = home.click_button_lihat()
    popup.wait_for_selector("h1, .organization-header, .event-list", timeout=10000)

    # Tambahan assert jika diperlukan
    assert popup.url.startswith("https://www.goersapp.com/organizations/sqa-prod--pppllvnap?utm_source=gem&utm_medium=share"), "URL popup salah"

    # Tutup popup di akhir
    popup.close()


@allure.title("Klik tombol ATUR dan berhasil redirect ke /organizations")
def test_click_button_atur(login_and_go_to_home):
    page = login_and_go_to_home
    home = HomePage(page)

    # Klik tombol ATUR
    home.click_button_atur()

    # Validasi URL sudah redirect ke halaman organisasi
    assert "/organizations" in page.url, f"Redirect gagal, current URL: {page.url}"


@allure.title("Redirect ke menu Event")
def test_redirect_to_event(login_and_go_to_home):
    page = login_and_go_to_home
    home = HomePage(page)

    home.redirect_to_event()

    assert "/events" in page.url, f"Redirect ke menu Event gagal, current URL: {page.url}"
    page.wait_for_timeout(2000)  # Tunggu sebentar untuk memastikan halaman siap

@allure.title("Redirect ke menu Venue")
def test_redirect_to_venue(login_and_go_to_home):
    page = login_and_go_to_home
    home = HomePage(page)

    home.redirect_to_venue()

    assert "/venues" in page.url, f"Redirect ke menu Venue gagal, current URL: {page.url}"
    page.wait_for_timeout(2000)  # Tunggu sebentar untuk memastikan halaman siap

@allure.title("Redirect ke menu Layanan")
def test_redirect_to_layanan(login_and_go_to_home):
    page = login_and_go_to_home
    home = HomePage(page)

    home.redirect_to_layanan()

    assert "/services/additional-service" in page.url, f"Redirect ke menu Layanan Tambahan gagal, current URL: {page.url}"
    page.wait_for_timeout(2000)  # Tunggu sebentar untuk memastikan halaman siap

@allure.title("Redirect ke menu Settlement Venue dari Penagihan")
def test_go_to_settlement_venue(login_and_go_to_home):
    page = login_and_go_to_home
    home = HomePage(page)
    home.go_to_settlement_venue()
    assert "/billings/venues" in page.url
    page.wait_for_timeout(2000)  # Tunggu sebentar untuk memastikan halaman siap

@allure.title("Redirect ke menu Penagihan Event dari Penagihan")
def test_go_to_penagihan_event(login_and_go_to_home):
    page = login_and_go_to_home
    home = HomePage(page)
    home.go_to_penagihan_event()
    assert "/billings/events" in page.url
    page.wait_for_timeout(2000)  # Tunggu sebentar untuk memastikan halaman siap

@allure.title("Redirect ke menu Organisasi")
def test_redirect_to_organizations(login_and_go_to_home):
    page = login_and_go_to_home
    home = HomePage(page)

    home.redirect_to_organizations()

    assert "/organizations" in page.url, f"Redirect ke menu Organisasai gagal, current URL: {page.url}"
    page.wait_for_timeout(2000)  # Tunggu sebentar untuk memastikan halaman siap