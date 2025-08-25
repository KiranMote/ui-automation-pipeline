import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

@pytest.fixture
def login_page(page):
    return LoginPage(page)
