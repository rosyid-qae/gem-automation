import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
import allure
from playwright.sync_api import sync_playwright
from page.login_page import LoginPage
from page.search_organization_page import SearchOrganizationPage
from page.home_page import HomePage


@pytest.fixture(scope="function")
def login_and_go_to_home():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        page = browser.new_page()
        page.goto("https://gem.goersapp.com")

        login = LoginPage(page)
        login.login_valid("userdua95@gmail.com", "testing02")

        search = SearchOrganizationPage(page)
        search.search_organization("SQA PROD")

        yield page
        browser.close()

@allure.title("Masuk ke Buat Event dari Home Page")
def test_click_buat_event(login_and_go_to_home):
    page = login_and_go_to_home
    home = HomePage(page)
    home.click_buat_event()
    assert "/event/create" in page.url

@allure.title("Klik tombol Lihat dan popup tertutup")
def test_click_lihat_event(login_and_go_to_home):
    page = login_and_go_to_home
    home = HomePage(page)
    popup = home.click_lihat_event()
    assert popup.is_closed()

@allure.title("Klik tombol Atur dan pindah ke halaman atur")
def test_click_atur_event(login_and_go_to_home):
    page = login_and_go_to_home
    home = HomePage(page)
    home.click_atur_event()
    assert "/event/" in page.url and "/manage" in page.url