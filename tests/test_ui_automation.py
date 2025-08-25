import pytest
import allure

def test_navigate_to_login_page(login_page):
    login_page.navigate()
    assert login_page.page.is_visible(login_page.username_input)
    assert login_page.page.is_visible(login_page.password_input)

@allure.title("Enter Valid Username")
def test_enter_valid_username(login_page):
    login_page.navigate()
    login_page.enter_username('rahulshettyacademy')
    assert login_page.page.input_value(login_page.username_input) == 'rahulshettyacademy'

@allure.title("Enter Valid Password")
def test_enter_valid_password(login_page):
    login_page.navigate()
    login_page.enter_password('learning')
    assert login_page.page.input_value(login_page.password_input) == 'learning'

@allure.title("Select Admin as User Type")
def test_select_admin(login_page):
    login_page.navigate()
    login_page.select_admin()
    assert login_page.page.is_checked(login_page.admin_radio)

@allure.title("Select Role from Dropdown")
def test_select_role_from_dropdown(login_page):
    login_page.navigate()
    login_page.select_role('Student')
    assert 'Student' in login_page.page.inner_text(login_page.role_dropdown)

@allure.title("Agree to Terms and Conditions")
def test_agree_terms(login_page):
    login_page.navigate()
    login_page.agree_terms()
    assert login_page.page.is_checked(login_page.terms_checkbox)

@allure.title("Submit the Login Form")
def test_submit_login_form(login_page):
    login_page.navigate()
    login_page.submit()
    assert login_page.page.is_visible(login_page.login_button)

@allure.title("Verify 'iphone X' in Product List")
def test_verify_iphone_x(login_page):
    login_page.navigate()
    login_page.enter_username('rahulshettyacademy')
    login_page.enter_password('learning')
    login_page.select_admin()
    login_page.select_role('Student')
    login_page.agree_terms()
    login_page.submit()
    assert login_page.is_product_visible('iphone X')

@allure.title("Verify 'Realme 9 pro' in Product List")
def test_verify_realme_9_pro(login_page):
    login_page.navigate()
    login_page.enter_username('rahulshettyacademy')
    login_page.enter_password('learning')
    login_page.select_admin()
    login_page.select_role('Student')
    login_page.agree_terms()
    login_page.submit()
    assert login_page.is_product_visible('Realme 9 pro')
