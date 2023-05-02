import pytest
from playwright.sync_api import Page, sync_playwright
from pages.signin_page import SigninPage



@pytest.fixture(scope='function')
def chromium_page() -> Page:
    with sync_playwright() as playwright:
        chromium = playwright.chromium.launch(headless=False)
        yield chromium.new_page()


@pytest.fixture(scope='function')
def signin_page(chromium_page: Page) -> SigninPage:
    return SigninPage(chromium_page)


# @pytest.fixture(scope='function')
# def playwright_languages_page(chromium_page: Page) -> PlaywrightLanguagesPage:
#     return PlaywrightLanguagesPage(chromium_page)