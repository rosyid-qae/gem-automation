import allure
from playwright.sync_api import Page, expect

class SearchOrganizationPage:
    def __init__(self, page: Page):
        self.page = page
        self.search_input = 'input[placeholder="Cari Organisasi"]'
        self.org_card = 'div.___organization-list__item'
        self.create_button = 'a.___add__organization'
        self.search_button = 'Item__button'

    def wait_for_organization_page(self):
        self.page.wait_for_selector('input[placeholder="Cari Organisasi"]', timeout=15000)

    @allure.step("Cari organisasi dengan nama: {name}")
    def search_organization(self, name):
        self.page.locator(self.search_input).wait_for(state="visible", timeout=10000)
        self.page.locator(self.search_input).fill(name)

        try:
            self.page.locator("span.input-group-btn button").click(timeout=3000)
            print("[DEBUG] Tombol search diklik")
        except Exception as e:
            print(f"[DEBUG] Tombol search tidak bisa diklik — lewati klik. Error: {e}")

        # Tunggu hasil pencarian muncul
        try:
            self.page.locator(self.org_card).first.wait_for(state="visible", timeout=5000)
        except:
            print("[WARNING] Tidak ada organisasi muncul setelah pencarian")

        self.page.wait_for_timeout(1000)
        # Debugging: Ambil screenshot setelah pencarian
        self.page.screenshot(path="debug_search_organization.png")
        # Debugging: Log page content after search
        print("[DEBUG] Page content after search:")
        print(self.page.content())
        # Verifikasi apakah ada organisasi yang ditemukan
        expect(self.page.locator(self.org_card)).to_have_count_greater_than(0, timeout=5000)
        # Debugging: Ambil screenshot setelah verifikasi
        self.page.screenshot(path="debug_verify_organization.png")
        # Debugging: Log jumlah organisasi ditemukan
        count = self.page.locator(self.org_card).count()
        print(f"[DEBUG] Jumlah organisasi ditemukan: {count}")
        if count == 0:
            raise Exception(f"[ERROR] Tidak menemukan organisasi dengan nama: {name}")
        # Ambil screenshot untuk debugging
        self.page.screenshot(path="debug_search_result.png")
        # Debugging: Log page content after waiting for organization card
        print("[DEBUG] Page content after waiting for organization card:")
        print(self.page.content())
        # Tunggu tombol "PILIH" muncul di dalam org_card
        self.page.locator(f'{self.org_card}:has-text("{name}")').locator("text=PILIH").wait_for(state="visible", timeout=10000)
        # Debugging: Ambil screenshot setelah tombol "PILIH" muncul
        self.page.screenshot(path="debug_select_button.png")
        # Debugging: Log page content before clicking "PILIH"
        print("[DEBUG] Page content before clicking 'PILIH':")
        print(self.page.content())
        # Klik tombol "PILIH" di dalam org_card
        self.page.locator(f'{self.org_card}:has-text("{name}")').locator("text=PILIH").click()
        # Tunggu load state setelah klik
        self.page.wait_for_load_state('networkidle')

  

    # @allure.step("Pilih organisasi dengan nama: {name}")
    # def select_organization(self, name):
    #     # Tunggu hingga halaman selesai dimuat
    #     self.page.wait_for_load_state("networkidle")

    #     # Cari elemen organisasi berdasarkan nama
    #     org_card = self.page.locator(f'div.___organization-list__item:has-text("{name}")')

    #     # Debug: Ambil screenshot sebelum pencarian
    #     self.page.screenshot(path="before_search.png")

    #     # Hitung jumlah elemen yang ditemukan
    #     count = org_card.count()
    #     print(f"[DEBUG] Jumlah organisasi ditemukan: {count}")

    #     # Jika tidak ada elemen yang ditemukan, lemparkan error
    #     if count == 0:
    #         self.page.screenshot(path="debug_no_result.png")
    #     raise Exception(f"[ERROR] Tidak menemukan organisasi dengan nama: {name}")

    #     # Tunggu elemen pertama menjadi visible
    #     org_card.first.wait_for(state="visible", timeout=20000)

    #     # Debug: Ambil screenshot hasil pencarian
    #     self.page.screenshot(path="debug_search_result.png")

    #     # Klik tombol PILIH di dalam org_card
    #     org_card.first.locator("text=PILIH").click()

    #     # Tunggu hingga halaman selesai dimuat setelah klik
    #     self.page.wait_for_load_state('networkidle')


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

    # Di SearchOrganizationPage
    def wait_for_organization_page(self):
        print("Menunggu halaman organisasi siap")
        self.page.wait_for_selector("text=Pilih Organisasi", timeout=10000)



