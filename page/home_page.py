import allure

class HomePage:
    def __init__(self, page):
        self.page = page

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
