import pytest
import allure
from playwright.sync_api import sync_playwright
from page.login_page import LoginPage
from page.search_organization_page import SearchOrganizationPage
from page.events.manage_event_page import ManageEventPage
from page.events.detail_event_page import DetailEventPage

@allure.title("Step 1: Kelola Event Flow")
def test_kelola_event_flow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        page = browser.new_page()

        # 1. Login
        login = LoginPage(page)
        page.goto("https://gem.goersapp.com")
        login.login_valid("userdua95@gmail.com", "testing02")

        # 2. Search & pilih organisasi
        org_page = SearchOrganizationPage(page)
        org_page.search_organization("SQA PROD")

        # 3. Masuk menu Event
        page.click('a[data-testid="cta-menu-event"]')
        page.wait_for_load_state("networkidle")

        assert "/events" in page.url, f"Redirect ke menu Event gagal, current URL: {page.url}"

        # 4. Search & klik event
        manage_events = ManageEventPage(page)
        manage_events.search_event("Testing Event 1")
        manage_events.click_event_by_name("Testing Event 1")

        # 5. Navigasi tab di detail event
        kelola_event = DetailEventPage(page)
        kelola_event.go_to_informasi_event()
        kelola_event.go_to_tiket_event()
        kelola_event.go_to_formulir_pemesanan()

        browser.close()
