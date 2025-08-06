import pytest
import allure
from playwright.sync_api import sync_playwright
from page.login_page import LoginPage
from page.search_organization_page import SearchOrganizationPage
from page.home_page import HomePage
from page.events.manage_event_page import ManageEventPage

# ✅ Fixture untuk login dan masuk ke halaman Home
@pytest.fixture(scope="function")
def login_and_go_to_home():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
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

# ✅ Fixture tambahan sampai halaman Event
@pytest.fixture(scope="function")
def login_and_go_to_event(login_and_go_to_home):
    page = login_and_go_to_home
    home = HomePage(page)
    home.redirect_to_event()

    try:
        page.wait_for_selector("text=BUAT EVENT", timeout=5000)
        print("[DEBUG] Halaman Event berhasil dimuat")
    except:
        print("[WARNING] Halaman Event tidak berhasil dimuat")
        page.screenshot(path="debug_event_failed.png")
        raise

    return page

# ✅ Test klik menu event
@allure.title("Redirect ke menu Event")
def test_redirect_to_event(login_and_go_to_home):
    page = login_and_go_to_home
    home = HomePage(page)

    home.redirect_to_event()

    assert "/events" in page.url, f"Redirect ke menu Event gagal, current URL: {page.url}"
    page.wait_for_timeout(2000)  # Tunggu sebentar untuk memastikan halaman siap

# ✅ Test klik menu Analitik Event
@allure.title("Klik menu Analitik Event")
def test_click_analytics_menu(login_and_go_to_event):
    page = login_and_go_to_event
    event_page = ManageEventPage(page)
    event_page.click_analytics_menu()
    assert "/events/analytics" in page.url, f"Redirect ke menu Analitik gagal, current URL: {page.url}"
    page.wait_for_timeout(2000)  # Tunggu sebentar untuk memastikan halaman siap

# ✅ Test pindah antar tab event
@allure.title("Pindah antar tab event dari Semua → Draf → Tayang → Berakhir → Semua")
def test_switch_event_tabs(go_to_event_page):
    page = go_to_event_page
    event_page = ManageEventPage(page)

    event_page.switch_event_tabs()

# ✅ Test klik tombol Buat Event
@allure.title("Klik tombol Buat Event")
def test_click_create_event(go_to_event_page):
    page = go_to_event_page
    event_page = ManageEventPage(page)
    page.wait_for_timeout(2000)

    event_page.click_create_event()

    assert "/events/create" in page.url, f"Redirect ke halaman Buat Event gagal, current URL: {page.url}"
    page.wait_for_timeout(2000)

# ✅ Test pencarian event
@allure.title("Cari event berdasarkan nama")
def test_search_event(go_to_event_page):
    page = go_to_event_page
    event_page = ManageEventPage(page)

    event_page.search_event("Testing Event 1")  # ganti dengan nama event yang kamu tahu ada
   
    page.wait_for_timeout(2000)  # Tunggu sebentar untuk memastikan hasil muncul