import allure
from playwright.sync_api import Page, expect

class SearchOrganizationPage:
    def __init__(self, page: Page):
        self.page = page
        self.search_input = 'input[placeholder="Cari Organisasi"]'
        self.org_card = 'div.___organization-list__item'
        self.create_button = 'a.___add__organization'
        self.search_button = 'Item__button'

    @allure.step("Tunggu halaman organisasi siap")
    def wait_for_organization_page(self):
        self.page.wait_for_selector('input[placeholder="Cari Organisasi"]', timeout=15000)

    @allure.step("Klik organisasi yang ditemukan")
    def click_found_organization(self):
        self.page.wait_for_selector(self.org_card, timeout=5000)
        self.page.click(self.search_button)

    @allure.step("Klik tombol Buat Organisasi Baru")
    def click_create_organization(self):
        self.page.locator(self.create_button).wait_for(state="visible", timeout=10000)
        self.page.click(self.create_button)
        self.page.wait_for_timeout(5000)

    @allure.step("Verifikasi tidak ada hasil organisasi")
    def verify_no_result(self):
        expect(self.page.locator(self.org_card)).to_have_count(0)

    @allure.step("Cari organisasi dengan nama: {name}")
    def search_organization(self, name):
        self.page.locator(self.search_input).wait_for(state="visible", timeout=10000)
        self.page.locator(self.search_input).fill(name)

        try:
            self.page.locator("span.input-group-btn button").click(timeout=3000)
            print("[DEBUG] Tombol search diklik")
        except Exception as e:
            print(f"[DEBUG] Tombol search tidak bisa diklik — lewati klik. Error: {e}")

        self.page.wait_for_timeout(1000)

        org_elements = self.page.locator('div.___organization')
        count = org_elements.count()

        found = False
        for i in range(count):
            org_text = org_elements.nth(i).inner_text().strip()
            print(f"[DEBUG] Ditemukan organisasi ke-{i+1}: {org_text}")
            if name.lower() in org_text.lower():
                print(f"[INFO] Organisasi '{name}' ditemukan di urutan ke-{i+1}")
                
                # Dapatkan tombol 'PILIH' yang sesuai berdasarkan urutan
                pilih_buttons = self.page.locator('a[data-testid="cta-select-organization"]')
                pilih_buttons.nth(i).wait_for(state="visible", timeout=5000)
                pilih_buttons.nth(i).click()
                found = True
                break

        if not found:
            raise Exception(f"[ERROR] Organisasi '{name}' tidak ditemukan atau tombol PILIH tidak tersedia.")

        self.page.wait_for_load_state('networkidle')



