from playwright.sync_api import Page, expect

class CarritoPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/cart"

    def verificar_producto_carrito(self,producto):
         expect(self.page.get_by_role("heading", name=producto)).to_be_visible()

    def verificar_producto_eliminado_carrito(self,producto):
          expect(self.page.get_by_role("heading", name=producto)).not_to_be_visible()

    def verificar_precio_carrito(self,precio):
        expect(self.page.get_by_text(precio).first).to_be_visible()

    def eliminar_producto_carrito(self,producto):
        self.page.get_by_role("button", name="Eliminar "+producto).click()

    def vaciar_carrito(self):
         self.page.get_by_role("button", name="Vaciar Carrito").click()
    
    def verificar_carrito_vacio(self):
         expect(self.page.get_by_text("Tu carrito está vacío")).to_be_visible()

    def ver_productos(self):
         self.page.get_by_role("link", name="Ver Productos").click()

    def proceder_al_pago(self):
         self.page.get_by_role("link", name="Proceder al Pago").click()