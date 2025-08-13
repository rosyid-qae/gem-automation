import allure

class DetailEventPage:
    def __init__(self, page):
        self.page = page
        # Menu Kelola Event
        self.informasi_event_tab = '[data-testid="cta-sidemenu-kelola-event-submenu-informasi-event"]'
        self.tiket_event_tab = '[data-testid="cta-sidemenu-kelola-event-submenu-tiket-event"]'
        self.formulir_pemesanan_tab = '[data-testid="cta-sidemenu-kelola-event-submenu-formulir-pemesanan"]'
        # Menu Kelola Peserta Acara
        self.kelola_peserta_menu = '[data-testid="cta-sidemenu-kelola-peserta-acara"]'
        self.data_pemesan_tab = '[data-testid="cta-sidemenu-kelola-peserta-acara-submenu-data-pemesan"]'
        self.daftar_peserta_tab = '[data-testid="cta-sidemenu-kelola-peserta-acara-submenu-daftar-peserta-acara"]'
        # Menu Laporan dan Analitik
        self.laporan_analitik_menu = '[data-testid="cta-sidemenu-laporan-dan-analitik"]'
        self.penjualan_event_tab = '[data-testid="cta-sidemenu-laporan-dan-analitik-submenu-penjualan-event"]'
        self.analitik_event_tab = '[data-testid="cta-sidemenu-laporan-dan-analitik-submenu-analitik-event"]'
        self.ulasan_event_tab = '[data-testid="cta-sidemenu-laporan-dan-analitik-submenu-ulasan-event"]'
        # Menu Pengiriman Tiket WA
        self.pengiriman_tiket_wa_menu = '[data-testid="cta-sidemenu-pengiriman-tiket-whatsapp"]'
        # Menu Email Blast
        self.email_blast_menu = '[data-testid="cta-sidemenu-email-blast"]'
        # Menu Pengaturan Widget
        self.pengaturan_widget_menu = '[data-testid="cta-sidemenu-pengaturan-widget"]'
        # Menu Layanan Tambahan
        self.layanan_tambahan_menu = '[data-testid="cta-sidemenu-layanan-tambahan"]'
        self.paket_layanan_tab = '[data-testid="cta-sidemenu-layanan-tambahan-submenu-paket-layanan"]'
        self.daftar_layanan_tab = '[data-testid="cta-sidemenu-layanan-tambahan-submenu-paket-layanan"]'


    @allure.step("Buka tab Informasi Event")
    def go_to_informasi_event(self):
        self.page.click(self.informasi_event_tab)
        self.page.wait_for_timeout(3000)

    @allure.step("Buka tab Tiket Event")
    def go_to_tiket_event(self):
        self.page.click(self.tiket_event_tab)
        self.page.wait_for_timeout(3000)

    @allure.step("Buka tab Formulir Pemesanan")
    def go_to_formulir_pemesanan(self):
        self.page.click(self.formulir_pemesanan_tab)
        self.page.wait_for_timeout(3000)

    # Menu Kelola Peserta Acara
    @allure.step("Pastikan menu Kelola Peserta Acara terbuka")
    def open_kelola_peserta_menu(self):
        menu = self.page.locator(self.kelola_peserta_menu)
        # jika submenu belum terbuka (aria-expanded="false"), klik untuk buka
        expanded = menu.get_attribute("aria-expanded")
        if expanded != "true":
            menu.click()
            self.page.wait_for_timeout(500)  # beri waktu animasi expand

    @allure.step("Pindah ke tab Data Pemesan")
    def go_to_data_pemesan(self):
        self.page.click(self.data_pemesan_tab)
        self.page.wait_for_timeout(3000)

    @allure.step("Pindah ke tab Daftar Peserta Acara")
    def go_to_daftar_peserta(self):
        self.page.click(self.daftar_peserta_tab)
        self.page.wait_for_timeout(3000)

    # Menu Laporan dan Analitik
    @allure.step("Buka menu Laporan dan Analitik")
    def open_laporan_analitik_menu(self):
        self.page.click(self.laporan_analitik_menu)
        self.page.wait_for_timeout(3000)

    @allure.step("Pindah ke tab Penjualan Event")
    def go_to_penjualan_event(self):
        self.page.click(self.penjualan_event_tab)
        self.page.wait_for_timeout(3000)

    @allure.step("Pindah ke tab Analitik Event")
    def go_to_analitik_event(self):
        self.page.click(self.analitik_event_tab)
        self.page.wait_for_timeout(3000)

    @allure.step("Pindah ke tab Ulasan Event")
    def go_to_ulasan_event(self):
        self.page.click(self.ulasan_event_tab)
        self.page.wait_for_timeout(3000)

    # Menu Pengiriman Tiket WA
    @allure.step("Buka menu Pengiriman Tiket WA")
    def open_pengiriman_tiket_wa_menu(self):
        self.page.click(self.pengiriman_tiket_wa_menu)
        self.page.wait_for_timeout(3000)
    
    # Menu Email Blast
    @allure.step("Buka menu Email Blast")
    def open_email_blast_menu(self):
        self.page.click(self.email_blast_menu)
        self.page.wait_for_timeout(3000)

    # Menu Pengaturan Widget
    @allure.step("Buka menu Pengaturan Widget")
    def open_pengaturan_widget_menu(self):
        self.page.click(self.pengaturan_widget_menu)
        self.page.wait_for_timeout(3000)

    # Menu Layanan Tambahan
    @allure.step("Buka menu Layanan Tambahan")
    def open_layanan_tambahan_menu(self):
        self.page.click(self.layanan_tambahan_menu)
        self.page.wait_for_timeout(3000)
    
    @allure.step("Pindah ke tab Paket Layanan")
    def go_to_paket_layanan(self):
        self.page.click(self.paket_layanan_tab)
        self.page.wait_for_timeout(3000)

    @allure.step("Pindah ke tab Daftar Layanan")
    def go_to_daftar_layanan(self):
        self.page.click(self.daftar_layanan_tab)
        self.page.wait_for_timeout(3000)
        