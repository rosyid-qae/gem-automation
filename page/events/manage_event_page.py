import allure

class ManageEventPage:
    def __init__(self, page):
        self.page = page
        page.wait_for_url("**/events", timeout=10000)

    @allure.step("Klik menu Event dan redirect ke halaman Event")
    def redirect_to_event(self):
        menu_event = self.page.locator('a[data-testid="cta-menu-event"]')
        menu_event.wait_for(state="visible", timeout=5000)
        menu_event.click()
        self.page.wait_for_url("**/events", timeout=10000)
        return self.page

    @allure.step("Klik menu Analitik Event")
    def click_analytics_menu(self):
        analytics_button = self.page.locator('a[data-testid="cta-sidemenu-analitik-event"]')
        analytics_button.wait_for(state="visible", timeout=5000)
        analytics_button.click()
        self.page.wait_for_url("**/events/analytics", timeout=10000)    
        return self.page

@allure.step("Pindah-pindah tab event: Semua → Draf → Tayang → Berakhir → Semua")
def switch_event_tabs(self):
    # Tunggu 2 detik sebelum mulai berpindah tab (setelah buka menu event)
    self.page.wait_for_timeout(2000)

    tab_texts = [
        ("SEMUA EVENT", 2000),
        ("DRAF", 2000),
        ("TAYANG", 2000),
        ("BERAKHIR", 2000),
        ("SEMUA EVENT", 3000),
    ]

    for tab, delay in tab_texts:
        try:
            tab_selector = f'a.nav-link:has-text("{tab}")'
            self.page.locator(tab_selector).click()
            print(f"[INFO] Klik tab: {tab}")
            self.page.wait_for_selector("div.card", timeout=5000)
            self.page.wait_for_timeout(delay)  # delay setelah pindah tab
        except Exception as e:
            print(f"[ERROR] Gagal klik tab: {tab} → {str(e)}")
            self.page.screenshot(path=f"screenshots/tab_{tab.lower().replace(' ', '_')}_error.png")
            raise e

    print("[INFO] Selesai jelajahi semua tab event")


    @allure.step("Klik tombol Buat Event")
    def click_create_event(self):
        create_button = self.page.locator("a.btn-success[href='/events/create/package']")
        create_button.wait_for(state="visible", timeout=5000)
        create_button.click()
        self.page.wait_for_url("**/events/create", timeout=10000)
        print("[INFO] Berhasil klik tombol Buat Event")
        return self.page

    @allure.step("Cari event dengan mengetik dan tekan Enter: {keyword}")
    def search_event(self, keyword: str):
        try:
            search_input = self.page.locator("input[placeholder='Cari event']")
            search_input.fill("")  # kosongkan dulu
            search_input.fill(keyword)
            print(f"[INFO] Mengetik keyword: {keyword}")

            search_input.press("Enter")
            print("[INFO] Tekan Enter setelah input keyword")

            self.page.wait_for_load_state("networkidle")
            self.page.wait_for_timeout(1000)  # delay untuk tampilkan hasil
        except Exception as e:
            print(f"[ERROR] Gagal cari event dengan Enter: {e}")
            self.page.screenshot(path=f"screenshots/search_event_{keyword}.png")
            raise
