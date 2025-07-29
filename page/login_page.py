# page/login_page.py

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.email_input = 'input[placeholder="Masukkan alamat email Anda"]'
        self.password_input = 'input[placeholder="Password Anda"]'
        self.login_button = 'a.btn-success'  # tombol login adalah <a>, bukan <button>


    def login_valid(self, email, password):
        self.page.goto("https://gem.goersapp.com/login")
        print("Halaman login dibuka")

        # Tunggu sampai input email muncul
        self.page.wait_for_selector(self.email_input, timeout=5000)
        print("Input email ditemukan")

        self.page.fill(self.email_input, email)
        print("Email diisi")

        self.page.fill(self.password_input, password)
        print("Password diisi")

        self.page.click(self.login_button)
        print("Tombol login diklik")

        self.page.wait_for_load_state('networkidle')
        print("Selesai login")


    def login_invalid(self, email, password):
        self.page.goto("https://gem.goersapp.com/login")
        self.page.wait_for_selector(self.email_input)
        self.page.fill(self.email_input, email)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)
        self.page.wait_for_timeout(2000)

    def get_error_message(self):
        try:
            self.page.wait_for_selector("div.Toastify__toast--error", timeout=8000)
            error_element = self.page.query_selector("div.Toastify__toast--error")
            return error_element.inner_text() if error_element else None
        except:
            return None
