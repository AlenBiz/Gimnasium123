from playwright.sync_api import Page
from pages.base_page import BasePage
from page_factory.input import Input
from page_factory.button import Button


class SigninPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.email_input = Input(
            page, locator='Эл. почта', name='username'
        )
        self.password_input = Input(
            page, locator='Пароль', name='password'
        )
        self.signin_button = Button(
            page, locator='.signin-form-button', name='submit'
        )

    def login(self, email: str, password: str) -> None:
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.signin_button.click()
