from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = "input#username"
        self.password_input = "input#password"
        self.admin_radio = "input[value='admin']"
        self.role_dropdown = "select.form-control"
        self.terms_checkbox = "input[type='checkbox']"
        self.login_button = "input#signInBtn"

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    def enter_username(self, username):
        self.page.fill(self.username_input, username)

    def enter_password(self, password):
        self.page.fill(self.password_input, password)

    def select_admin(self):
        self.page.check(self.admin_radio)

    def select_role(self, role):
        self.page.select_option(self.role_dropdown, label=role)

    def agree_terms(self):
        self.page.check(self.terms_checkbox)

    def submit(self):
        self.page.click(self.login_button)

    def is_product_visible(self, product_name):
        self.page.wait_for_selector(".card-title", timeout=5000)
        products = self.page.locator(".card-title").all_text_contents()
        return any(product_name.lower() in p.lower() for p in products)
