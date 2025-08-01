
from playwright.sync_api import sync_playwright
import random
import string

def select_organization_by_name(page, org_name):
    buttons = page.locator('[data-testid="cta-select-organization"]')
    for i in range(buttons.count()):
        button = buttons.nth(i)
        parent = button.locator("xpath=..")
        if org_name.upper() in parent.inner_text().upper():
            button.click()
            print(f"✅ Berhasil pilih organisasi '{org_name}'")
            return
    raise Exception(f"❌ Organisasi '{org_name}' tidak ditemukan")

# Definisi untuk menuju ke Menu
def go_to_menu(page, menu_text, expected_url, content_selector=None):
    page.click(f'nav.site-menu a:has-text("{menu_text}")', force=True)
    page.wait_for_timeout(2000)
    if not page.url.endswith(expected_url):
        print(f"⚠️ URL belum pindah, sekarang: {page.url}")
    else:
        print(f"✅ Berhasil pindah ke {menu_text} -> {page.url}")
    if content_selector:
        page.wait_for_selector(content_selector, timeout=10000)
        print(f"✅ Konten {menu_text} muncul")

# Definisi untuk menuju ke Event
def click_event_by_name(page, event_name: str, timeout=10000):
    try:
        selector = f'div.___event-card__content__name:has-text("{event_name}")'
        page.wait_for_selector(selector, timeout=timeout)
        page.click(selector)
        page.wait_for_selector('h1', timeout=timeout)
        print(f"✅ Berhasil masuk detail event '{event_name}'")
    except Exception as e:
        print(f"❌ Gagal klik event '{event_name}':", e)

# Definisi untuk membuka halaman event berdasarkan ID
def open_event_by_id(page, event_id: int, timeout=10000):
    try:
        url = f"https://gem.goersapp.com/events/{event_id}"
        page.goto(url, timeout=timeout)
        page.wait_for_selector('h1', timeout=timeout)
        print(f"✅ Berhasil masuk ke halaman event dengan ID {event_id}")
    except Exception as e:
        print(f"❌ Gagal membuka event ID {event_id}:", e)


# Definisi untuk menuju ke submenu suatu event
def go_to_event_submenu(page, menu_text: str, expected_path: str, timeout=10000):
    try:
        # Tunggu link dengan teks yang sesuai muncul
        link = page.wait_for_selector(f'#kelola-event a:has-text("{menu_text}")', timeout=timeout)
        link.scroll_into_view_if_needed()
        link.click(force=True)

        # Tunggu URL berubah sesuai path yang diinginkan
        page.wait_for_url(f"**{expected_path}", timeout=timeout)

        if expected_path in page.url:
            print(f"✅ Berhasil masuk submenu '{menu_text}' ➜ {page.url}")
        else:
            print(f"❌ Gagal masuk submenu '{menu_text}'. URL sekarang: {page.url}")
    except Exception as e:
        print(f"❌ Error saat pindah ke submenu '{menu_text}':", e)


# ISI FORM HALAMAN BUAT TIKET BERBAYAR
def fill_ticket_form(page, name=None, price='15000', quota='100'):
    ticket_name_input = 'input[placeholder="Masukkan nama tiket"]'
    ticket_price_input = 'div.___ticket__input__price input'
    ticket_quota_input = 'input[placeholder="Masukkan kuota tiket"]'
    ticket_session_checkboxes = 'div.Session__Wrapper-cMPCOk input[type="checkbox"]:not([disabled])'

    if name is None:
        name = generate_random_ticket_name()

    try:
        page.wait_for_selector(ticket_name_input, timeout=5000)
        page.wait_for_selector(ticket_price_input, timeout=5000)
        page.wait_for_selector(ticket_quota_input, timeout=5000)

        page.fill(ticket_name_input, name)
        page.fill(ticket_price_input, price)
        page.fill(ticket_quota_input, quota)

        # Centang semua checkbox sesi aktif dengan force=True
        session_checkboxes = page.locator(ticket_session_checkboxes)
        count = session_checkboxes.count()

        for i in range(count):
            checkbox = session_checkboxes.nth(i)
            checkbox.scroll_into_view_if_needed()
            checkbox.check(force=True)
        
        print(f"✅ Form tiket '{name}' berhasil diisi dan {count} sesi aktif dicentang")

    except Exception as e:
        print(f"❌ Gagal mengisi form tiket: {e}")
    
# Fungsi membuat nama tiket acak
def generate_random_ticket_name():
    random_number = random.randint(100, 999)
    return f"Tiket Automation {random_number}"



with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    page.goto('https://gem.goersapp.com', timeout=60000)


    # Halaman Login
    username = page.wait_for_selector('input[type="text"]')    
    username.type('userdua95@gmail.com')
    password = page.wait_for_selector('input[type="password"]')
    password.type('testing02')

    page.click('.btn-success')
    page.wait_for_selector('input[placeholder="Cari Organisasi"]', timeout=15000)
    print("✅ Berhasil login")

    # Cari dan pilih organisasi dengan nama "SQA PROD"
    page.fill('input[placeholder="Cari Organisasi"]', 'SQA PROD')
    page.press('input[placeholder="Cari Organisasi"]', 'Enter')
    print("✅ Berhasil menampilkan organisasi")

    # Gunakan fungsi klik tombol PILIH untuk organisasi
    select_organization_by_name(page, "SQA PROD")
    page.wait_for_selector('nav.site-menu', timeout=30000)

    page.click('nav.site-menu a:has-text("Event")', force=True)
    page.wait_for_timeout(2000)  # Tunggu sebentar supaya SPA load konten baru

    if page.url.endswith("/events"):
        print("✅ Berhasil pindah ke halaman Event")
    else:
        print("❌ Gagal pindah ke halaman Event, URL sekarang")

    page.wait_for_selector('div.Label__Label-jsURsk:has-text("Daftar Event")', timeout=50000)
    print("✅ Konten Event sudah muncul")

    # Klik event berdasarkan ID
    open_event_by_id(page, 43529)

    # ✅ Masuk ke sub-menu Event
    go_to_event_submenu(page, "Tiket Event", "/tickets")

    # Klik tombol "Tiket Baru"
    page.click('a.btn-primary:has-text("Tiket Baru")')
    # Tunggu dropdown muncul
    page.wait_for_selector('div.toolbar-dropdown', timeout=10000)
    # Klik opsi "TIKET BERBAYAR"
    page.click('a.btn.btn-link-info:has-text("TIKET BERBAYAR")')
    print("✅ Berhasil klik Tiket Berbayar")

    # HALAMAN BUAT TIKET BERBAYAR

    # Tunggu form input muncul
    page.wait_for_selector('input[placeholder="Masukkan nama tiket"]', timeout=10000)
    # Input nama, harga dan kouta
    #fill_ticket_form(page, name='Tiket VIP 2', price='150000', quota='100')
    fill_ticket_form(page)  # otomatis isi nama acak, harga 150000, kuota 100

    # Klik checkbox sesi aktif (jika perlu)
    ticket_session_checkboxes = 'div.TicketSales__Group-hoJUzw input[type="checkbox"]:not([disabled])'

    # Klik tombol TAYANGKAN TIKET
    page.click('a.btn-success:has-text("TAYANGKAN TIKET")', force=True)
    page.wait_for_load_state('load')  # atau 'domcontentloaded'

    print("✅ Tiket berhasil disimpan dan ditayangkan")
    
    page.wait_for_timeout(5000)
    #browser.close()