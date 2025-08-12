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

    @allure.step("Pindah antar tab event dari Semua → Draf → Tayang → Berakhir → Semua")
    def switch_event_tabs(self):
        tabs = ["SEMUA EVENT", "DRAF", "TAYANG", "BERAKHIR"]

        for tab in tabs:
            try:
                tab_selector = f'a.nav-link:has-text("{tab}")'
                tab_element = self.page.locator(tab_selector)

                # Cek kalau tab belum aktif → klik
                if not tab_element.get_attribute("class") or "active" not in tab_element.get_attribute("class"):
                    tab_element.click()
                    print(f"[INFO] Klik tab: {tab}")
                else:
                    print(f"[INFO] Tab {tab} sudah aktif, tidak diklik")

                # Tunggu konten muncul (card atau empty state) max 10 detik
                try:
                    self.page.wait_for_selector(
                        "div.card, div.Empty__Wrapper-btpzwW",
                        state="attached",
                        timeout=3000
                    )
                    print(f"[INFO] Konten tab {tab} berhasil dimuat")
                except:
                    print(f"[WARN] Konten tab {tab} tidak muncul, lanjut ke tab berikutnya")
                    error_path = f"screenshots/tab_{tab.lower()}_empty.png"
                    self.page.screenshot(path=error_path)
                    allure.attach.file(
                        error_path,
                        name=f"Tab {tab} Kosong / Timeout",
                        attachment_type=allure.attachment_type.PNG
                    )
                    continue  # skip ke tab berikutnya

                # Delay 2 detik biar kelihatan di video/screenshot
                self.page.wait_for_timeout(2000)

            except Exception as e:
                print(f"[ERROR] Gagal load tab: {tab} → {str(e)}")
                error_path = f"screenshots/tab_{tab.lower()}_error.png"
                self.page.screenshot(path=error_path)
                allure.attach.file(
                    error_path,
                    name=f"Tab {tab} Error",
                    attachment_type=allure.attachment_type.PNG
                )
                # lanjut ke tab berikutnya walau error
                continue

        print("[INFO] Selesai jelajahi semua tab event")

    @allure.step("Klik detail event: {event_name}")
    def click_event_by_name1S(self, event_name: str):
        try:
            # Cari card event yang mengandung nama event
            event_locator = self.page.locator(f"div.card:has-text('{event_name}')").first
            event_locator.wait_for(state="visible", timeout=5000)
            event_locator.click()
            print(f"[INFO] Klik event: {event_name}")

            # Tunggu halaman detail event terbuka
            self.page.wait_for_load_state("networkidle")
            self.page.wait_for_timeout(1000)
        except Exception as e:
            print(f"[ERROR] Gagal klik event '{event_name}': {e}")
            self.page.screenshot(path=f"screenshots/click_event_{event_name}.png")
            raise

    @allure.step("Klik event berdasarkan nama: {event_name}")
    def click_event_by_name(self, event_name: str):
        try:
            event_link = self.page.locator(f"a:has(div.___event-card__content__name:has-text('{event_name}'))").first
            event_link.wait_for(state="visible", timeout=10000)
            event_link.click()
            print(f"[INFO] Berhasil klik event '{event_name}'")
        except Exception as e:
            print(f"[ERROR] Gagal klik event '{event_name}': {e}")
            self.page.screenshot(path=f"screenshots/click_event_error_{event_name}.png")
            raise

