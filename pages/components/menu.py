from playwright.sync_api import Page, expect

class MenuComponent:

    def __init__(self, page: Page):
        self.page = page

    def clic_carrito_compra(self):
         self.page.get_by_role("link", name="Carrito de compra").click()