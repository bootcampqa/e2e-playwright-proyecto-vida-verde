from playwright.sync_api import Page, expect

class QuienesSomosPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/about"

    def verificar_titulo(self):
         expect(self.page.get_by_role("heading", name="Quiénes Somos")).to_be_visible()

    def verificar_url(self):
        assert self.page.url == self.url