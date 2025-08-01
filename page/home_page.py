import allure
from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def click_buat_event(self):
        self.page.get_by_role("button", name="Buat Event").click()

    def click_lihat_event(self):
        with self.page.expect_popup() as popup_info:
            self.page.get_by_role("button", name="Lihat").click()
        popup = popup_info.value
        popup.close()  # Jika harus langsung ditutup
        return popup

    def click_atur_event(self):
        self.page.get_by_role("button", name="Atur").click()

    def click_nav_menu(self, menu_name):
        self.page.get_by_role("link", name=menu_name).click()