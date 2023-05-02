from playwright.sync_api import Page, Response

class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page
    #
    def visit(self, url: str) -> Response |None:
        return self.page.goto(url, wait_until='networkidle')


    def reload(self) -> Response | None:
        return self.page.reload(wait_until='domcontentloaded')