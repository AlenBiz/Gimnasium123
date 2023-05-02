from playwright.sync_api import Page
from page_factory.link import Link
from page_factory.button import Button


class Navbar:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.home_link = Link(page, locator="", name='Обзор')
        self.docs_link = Link(page, locator="", name='Новости')
        self.home_link = Link(page, locator="", name='Предметы')
        self.docs_link = Link(page, locator="", name='Расписание')
        self.home_link = Link(page, locator="", name='Расписание классов')




    def visit_docs(self):
        self.docs_link.click()

    def visit_api(self):
        self.api_link.click()

    # def open_search(self):
    #     self.search_button.should_be_visible()
    #
    #     self.search_button.hover()
    #     self.search_button.click()
    #
    #     self.search_modal.modal_is_opened()