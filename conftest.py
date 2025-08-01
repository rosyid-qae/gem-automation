# conftest.py
import os
import pytest
import allure
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Dapatkan hasil test
    outcome = yield
    rep = outcome.get_result()

    # Hanya jika test gagal saat fase 'call' (bukan setup/teardown)
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)
        if page:
            screenshot_path = f"screenshots/{item.name}.png"
            os.makedirs("screenshots", exist_ok=True)
            page.screenshot(path=screenshot_path)
            allure.attach.file(screenshot_path, name="screenshot", attachment_type=allure.attachment_type.PNG)
