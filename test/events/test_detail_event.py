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

@allure.title("Step 2: Kelola Peserta Acara Flow")
def test_kelola_peserta_acara(go_to_event_page):
    page = go_to_event_page
    manage_event = ManageEventPage(page)

    manage_event.search_event("Testing Event 1")
    manage_event.click_event_by_name("Testing Event 1")

    kelola_peserta = DetailEventPage(page)
    kelola_peserta.open_kelola_peserta_menu()
    kelola_peserta.go_to_data_pemesan()
    kelola_peserta.go_to_daftar_peserta()


@allure.title("Step 3: Laporan dan Analitik Flow")
def test_laporan_analitik(go_to_event_page):
    page = go_to_event_page
    manage_event = ManageEventPage(page)

    manage_event.search_event("Testing Event 1")
    manage_event.click_event_by_name("Testing Event 1")

    laporan_analitik = DetailEventPage(page)
    laporan_analitik.open_laporan_analitik_menu()
    laporan_analitik.page.click(laporan_analitik.penjualan_event_tab)
    laporan_analitik.page.click(laporan_analitik.analitik_event_tab)
    laporan_analitik.page.click(laporan_analitik.ulasan_event_tab)

@allure.title("Step 4: Menu Pengiriman Tiket WA Flow")
def test_pengiriman_tiket_wa(go_to_event_page):
    page = go_to_event_page
    manage_event = ManageEventPage(page)

    manage_event.search_event("Testing Event 1")
    manage_event.click_event_by_name("Testing Event 1")

    pengiriman_tiket = DetailEventPage(page)
    pengiriman_tiket.open_pengiriman_tiket_wa_menu()

@allure.title("Step 5: Menu Pengaturan Email Blast Flow")
def test_pengaturan_email_blast(go_to_event_page):
    page = go_to_event_page
    manage_event = ManageEventPage(page)

    manage_event.search_event("Testing Event 1")
    manage_event.click_event_by_name("Testing Event 1")

    email_blast = DetailEventPage(page)
    email_blast.open_email_blast_menu()

@allure.title("Step 6: Menu Pengaturan Widget Flow")
def test_pengaturan_widget(go_to_event_page):
    page = go_to_event_page
    manage_event = ManageEventPage(page)

    manage_event.search_event("Testing Event 1")
    manage_event.click_event_by_name("Testing Event 1")

    pengaturan_widget = DetailEventPage(page)
    pengaturan_widget.open_pengaturan_widget_menu()

@allure.title("Step 7: Menu Layanan Tambahan Flow")
def test_layanan_tambahan(go_to_event_page):
    page = go_to_event_page
    manage_event = ManageEventPage(page)

    manage_event.search_event("Testing Event 1")
    manage_event.click_event_by_name("Testing Event 1")

    layanan_tambahan = DetailEventPage(page)
    layanan_tambahan.open_layanan_tambahan_menu()
    layanan_tambahan.go_to_paket_layanan()
    layanan_tambahan.go_to_daftar_layanan()