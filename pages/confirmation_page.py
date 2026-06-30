from playwright.sync_api import Page, expect

class ConfirmationPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/confirmation"

    def verificar_mensaje_compra_exito(self):
        expect(self.page.get_by_role(
        "heading", name="¡Compra Realizada con Éxito!")).to_be_visible()

    def verificar_producto(self,producto):
         expect(self.page.get_by_text(producto)).to_be_visible()

    def verificar_precio_producto(self, precio):
        expect(self.page.get_by_role("listitem").filter(
        has_text=precio).locator("data")).to_be_visible()

    def verificar_desglose_producto(self,precio):
        expect(self.page.get_by_role("definition").filter(
        has_text=precio).locator("data")).to_be_visible()

    def ir_a_inicio(self):
        self.page.get_by_role("link", name="Ir al Inicio", exact=True).click()