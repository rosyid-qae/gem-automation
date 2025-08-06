# conftest.py
# Konfigurasi pytest untuk Playwright dengan screenshot otomatis saat test gagal
import os
import pytest
import allure
from playwright.sync_api import sync_playwright
from page.login_page import LoginPage
from page.search_organization_page import SearchOrganizationPage
from page.home_page import HomePage
from page.events.manage_event_page import ManageEventPage


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

# ✅ Fixture tambahan khusus untuk test yang butuh login & masuk organisasi
@pytest.fixture(scope="function")
def go_to_home_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        page = browser.new_page()
        page.goto("https://gem.goersapp.com")

        login = LoginPage(page)
        login.login_valid("userdua95@gmail.com", "testing02")

        search = SearchOrganizationPage(page)
        search.search_organization("SQA PROD")
        search.wait_for_organization_page()
        page.wait_for_load_state("networkidle")

        yield page
        browser.close()

# ✅ Fixture baru: langsung masuk ke menu Event
@pytest.fixture(scope="function")
def go_to_event_page(go_to_home_page):
    page = go_to_home_page
    home = HomePage(page)
    home.redirect_to_event()

    try:
        page.wait_for_selector("text=BUAT EVENT", timeout=5000)
        print("[DEBUG] Halaman Event berhasil dimuat")
    except:
        print("[WARNING] Halaman Event tidak berhasil dimuat")
        page.screenshot(path="screenshots/debug_event_failed.png")
        raise

    return page

# 🔥 Screenshot otomatis jika test gagal
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        # Coba ambil fixture 'page' atau 'go_to_home_page' (keduanya mengandung Page)
        test_page = item.funcargs.get("page") or item.funcargs.get("go_to_home_page")
        if test_page:
            screenshot_path = f"screenshots/{item.name}.png"
            os.makedirs("screenshots", exist_ok=True)
            test_page.screenshot(path=screenshot_path)
            allure.attach.file(
                screenshot_path,
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )