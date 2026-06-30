from playwright.sync_api import Page, expect

class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/checkout"

    def verificar_titulo(self):
        expect(self.page.get_by_role("heading", name="Resumen del Pedido")).to_be_visible()

    def verificar_nombre_producto(self, producto):
        expect(self.page.get_by_role("listitem").filter(
        has_text=producto)).to_be_visible()

    def verificar_precio_producto(self, precio):
        expect(self.page.get_by_role("listitem").filter(
        has_text=precio).locator("data")).to_be_visible()

    def verificar_desglose_precio(self,precio):
        expect(self.page.get_by_role("definition").filter(
        has_text=precio).locator("data")).to_be_visible()

    def verificar_total(self,precio):
        expect(self.page.get_by_text(precio)).to_be_visible()

    def rellenar_nombre(self,nombre):
        self.page.get_by_role(
        "textbox", name="Nombre Completo *").fill(nombre)

    def rellenar_email(self,email):
         self.page.get_by_role("textbox", name="Email *").fill(email)

    def rellenar_direccion(self,direccion):
        self.page.get_by_role(
        "textbox", name="Dirección *").fill(direccion)

    def rellenar_tarjeta(self, tarjeta):
        self.page.get_by_role(
        "textbox", name="Número de Tarjeta de Crédito *").fill(tarjeta)

    def completar_compra(self):
        self.page.get_by_role("button", name="Completar Compra").click()