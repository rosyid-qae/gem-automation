import allure

class HomePage:
    def __init__(self, page):
        self.page = page
        self.page.wait_for_timeout(3000)

    @allure.step("Klik tombol LIHAT dari halaman Home")
    def click_button_lihat(self):
        lihat_button = self.page.locator('a[data-testid="cta-organization-redirect-website"]')

        lihat_button.wait_for(state="visible", timeout=10000)

        self.page.wait_for_function("""
            () => {
                const el = document.querySelector('a[data-testid="cta-organization-redirect-website"]');
                return el && el.getAttribute('href') && !el.getAttribute('href').includes('--undefined');
            }
        """)

        href = lihat_button.get_attribute("href")
        print("[DEBUG] href tombol LIHAT:", href)

        with self.page.expect_popup() as popup_info:
            lihat_button.click()

        popup = popup_info.value
        popup.wait_for_load_state("load")

        print("[DEBUG] URL popup terbuka:", popup.url)
        popup.screenshot(path="debug_popup_success.png")

        # Validasi path agar tidak gagal karena beda www
        from urllib.parse import urlparse
        expected_path = urlparse(href).path
        actual_path = urlparse(popup.url).path
        assert expected_path == actual_path, f"Expected path: {expected_path}, got: {actual_path}"

        return popup

    @allure.step("Klik tombol ATUR dan tunggu redirect ke halaman /organizations")
    def click_button_atur(self):
        atur_button = self.page.locator('a[data-testid="cta-organization-setting"]')
        atur_button.wait_for(state="visible", timeout=10000)
        atur_button.click()
        self.page.wait_for_url("**/organizations", timeout=20000)

    @allure.step("Klik menu Event dan redirect ke halaman Event")
    def redirect_to_event(self):
        menu_event = self.page.locator('a[data-testid="cta-menu-event"]')
        menu_event.wait_for(state="visible", timeout=5000)
        menu_event.click()
        self.page.wait_for_url("**/events", timeout=10000)
        return self.page
    
    @allure.step("Klik menu Venue dan redirect ke halaman Venue")
    def redirect_to_venue(self):
        menu_event = self.page.locator('a[data-testid="cta-menu-venue"]')
        menu_event.wait_for(state="visible", timeout=5000)
        menu_event.click()
        self.page.wait_for_url("**/venues", timeout=10000)
        return self.page

    @allure.step("Klik menu Layanan dan redirect ke halaman Layanan Tambahan")
    def redirect_to_layanan(self):
        menu_event = self.page.locator('a[data-testid="cta-menu-layanan"]')
        menu_event.wait_for(state="visible", timeout=5000)
        menu_event.click()
        self.page.wait_for_url("**/services/additional-service", timeout=10000)
        return self.page
    
    @allure.step("Klik menu Penagihan > Settlement Venue")
    def go_to_settlement_venue(self):
        self.page.hover('[data-testid="cta-menu-penagihan"]')
        self.page.wait_for_selector('[data-testid="cta-menu-penagihan-submenu-settlement-venue"]', state="visible")
        self.page.click('[data-testid="cta-menu-penagihan-submenu-settlement-venue"]')

    @allure.step("Klik menu Penagihan > Penagihan Event")
    def go_to_penagihan_event(self):
        self.page.hover('[data-testid="cta-menu-penagihan"]')
        self.page.wait_for_selector('[data-testid="cta-menu-penagihan-submenu-penagihan-event"]', state="visible")
        self.page.click('[data-testid="cta-menu-penagihan-submenu-penagihan-event"]')

    @allure.step("Klik menu Layanan dan redirect ke halaman Layanan Tambahan")
    def redirect_to_organizations(self):
        menu_event = self.page.locator('a[data-testid="cta-menu-organisasi"]')
        menu_event.wait_for(state="visible", timeout=5000)
        menu_event.click()
        self.page.wait_for_url("**/organizations", timeout=10000)
        return self.page
    
    @allure.step("Klik Buat Aktivitas - Buat Event")
    def click_create_event(self):
        self.page.hover('a[data-testid="cta-create-activity"]')
        self.page.wait_for_selector('a[data-testid="cta-create-event"]', state="visible", timeout=5000)
        self.page.click('a[data-testid="cta-create-event"]')

    @allure.step("Klik Buat Aktivitas - Buat Venue")
    def click_create_venue(self):
        self.page.hover('a[data-testid="cta-create-activity"]')
        self.page.wait_for_selector('a[data-testid="cta-create-venue"]', state="visible", timeout=5000)
        self.page.click('a[data-testid="cta-create-venue"]')

