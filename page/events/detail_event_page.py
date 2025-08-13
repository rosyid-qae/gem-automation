import allure

class DetailEventPage:
    def __init__(self, page):
        self.page = page
        self.informasi_event_tab = '[data-testid="cta-sidemenu-kelola-event-submenu-informasi-event"]'
        self.tiket_event_tab = '[data-testid="cta-sidemenu-kelola-event-submenu-tiket-event"]'
        self.formulir_pemesanan_tab = '[data-testid="cta-sidemenu-kelola-event-submenu-formulir-pemesanan"]'

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
