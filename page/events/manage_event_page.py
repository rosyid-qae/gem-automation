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
    
    # @allure.step("Klik menu Analitik Event")
    # def click_analytics_menu(self):
    #     analytics_button = self.page.locator('a[data-testid="cta-sidemenu-analitik-event"]')

    #     try:
    #         analytics_button.wait_for(state="visible", timeout=10000)  # Perpanjang timeout jadi 10 detik
    #         analytics_button.click()
    #         self.page.wait_for_url("**/events/analytics", timeout=10000)
    #         print("[INFO] Menu Analitik Event berhasil diklik")
    #     except Exception as e:
    #         print("[ERROR] Menu Analitik Event tidak muncul atau tidak bisa diklik")
    #         self.page.screenshot(path="screenshots/analytics_menu_not_found.png")
    #         raise e

    #     return self.page
