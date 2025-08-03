import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
import allure
from playwright.sync_api import sync_playwright
from page.login_page import LoginPage
from page.search_organization_page import SearchOrganizationPage


@allure.title("Cari organisasi dan masuk ke organisasi jika ditemukan")
def test_search_organization_success():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        page = browser.new_page()
        page.goto("https://gem.goersapp.com")

        # Login
        login = LoginPage(page)
        login.login_valid("userdua95@gmail.com", "testing02")

        # Tunggu halaman organisasi siap
        org_page = SearchOrganizationPage(page)
        org_page.wait_for_organization_page()
        page.wait_for_load_state("networkidle")

        search_input = page.locator('input[placeholder="Cari Organisasi"]')
        search_input.click()
        search_input.fill('')
        search_input.type('SQA PROD', delay=100)
        page.wait_for_timeout(3000)  # tunggu hasil pencarian muncul


        # Tunggu hasil pencarian muncul
        page.wait_for_selector('div.___organization:has-text("SQA PROD")')

         # Ambil semua card organisasi
        cards = page.locator('div:has(div.___organization)')
        total_cards = cards.count()
        print(f"🔍 Ditemukan {total_cards} card organisasi")

        clicked = False
        for i in range(total_cards):
            card = cards.nth(i)
            org_name_el = card.locator('div.___organization')

            if org_name_el.count() > 0:
                org_name = org_name_el.first.inner_text().strip()
                print(f"🔎 Card ke-{i+1} nama organisasi: {org_name}")

                if org_name == "SQA PROD":
                    print(f"✅ Organisasi 'SQA PROD' ditemukan di card ke-{i+1}")
                    pilih_button = card.locator('[data-testid="cta-select-organization"]')

                    if pilih_button.count() > 0 and pilih_button.first.is_visible():
                        pilih_button.first.click()
                        print(f"🖱️ Tombol PILIH diklik untuk 'SQA PROD'")
                        clicked = True
                        break

        assert clicked, "❌ Tidak menemukan dan klik tombol PILIH untuk organisasi 'SQA PROD'"

        # Tunggu sampai redirect selesai
        try:
            page.wait_for_url(lambda url: not url.endswith("?redirect=/"), timeout=10000)
        except:
            raise AssertionError("❌ Tidak berhasil meninggalkan halaman redirect dalam 10 detik")

        # Verifikasi URL
        current_url = page.url
        print(f"📍 URL saat ini: {current_url}")
        assert not current_url.endswith("?redirect=/"), "❌ Masih di halaman redirect"

        # Verifikasi navbar terlihat (pastikan sudah masuk organisasi)
        navbars = page.locator("nav")
        found_nav = False
        for i in range(navbars.count()):
            nav = navbars.nth(i)
            if nav.is_visible():
                print(f"✅ Navbar ke-{i+1} terlihat")
                found_nav = True
                break

        assert found_nav, "❌ Tidak ada navbar yang terlihat setelah masuk organisasi"
        page.wait_for_timeout(2000)  # Tunggu sebentar untuk memastikan halaman siap
        browser.close() 

@allure.title("Cari organisasi dengan nama yang tidak ada, pastikan tidak muncul")
def test_search_organization_invalid():
     with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        page = browser.new_page()
        page.goto("https://gem.goersapp.com")
   

        # Login
        login = LoginPage(page)
        login.login_valid("userdua95@gmail.com", "testing02")

        # Tunggu halaman organisasi siap
        org_page = SearchOrganizationPage(page)
        org_page.wait_for_organization_page()
        page.wait_for_load_state("networkidle")


        # Cari nama organisasi yang tidak ada
        search_input = page.locator('input[placeholder="Cari Organisasi"]')
        search_input.click()
        search_input.fill('')  # Kosongkan terlebih dahulu
        search_input.type('ORGANISASI TIDAK ADA', delay=100)  # Ketik pelan agar trigger

        # Tunggu sesaat, lalu cek hasil pencarian
        page.wait_for_timeout(3000)  # kasih delay 3 detik biar hasil muncul

        # Cari teks "Organisasi tidak ditemukan"
        empty_state = page.locator("text='Organisasi tidak ditemukan'")
        try:
            empty_state.wait_for(state='visible', timeout=10000)
            print("✅ Test negatif berhasil — tidak ada organisasi ditemukan.")
        except:
            print("❌ Test gagal — tidak ada teks 'Organisasi tidak ditemukan'")
            raise

@allure.title("Klik tombol Buat Organisasi")
def test_create_organization_redirect():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        page = browser.new_page()
        page.goto("https://gem.goersapp.com")

        login = LoginPage(page)
        login.login_valid("userdua95@gmail.com", "testing02")

        org_page = SearchOrganizationPage(page)
        org_page.wait_for_organization_page()
        org_page.click_create_organization()
    

        allure.attach(page.screenshot(), name="Halaman Buat Organisasi", attachment_type=allure.attachment_type.PNG)
        assert "redirect=" in page.url

        browser.close()

