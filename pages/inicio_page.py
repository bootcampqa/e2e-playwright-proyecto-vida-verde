from playwright.sync_api import Page, expect

class InicioPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/"

    def visitar_inicio(self):
        self.page.goto(self.url)

    def verificar_titulo(self):
        expect(self.page.get_by_role("heading", name="Vida Verde")).to_be_visible()
    def verificar_url(self):
        #esta comprueba que la url contenga (preferible esta opción)
        expect(self.page).to_have_url(self.url)
        