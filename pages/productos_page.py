from playwright.sync_api import Page, expect

class ProductosPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/products"

    #abrir la página de productos
    def visitar_productos(self):
        self.page.goto(self.url)

    def verificar_titulo(self):
        expect(self.page.get_by_role("heading", name="Catálogo de Productos")).to_be_visible()

    def verificar_categoria(self,categoria):
        expect(self.page.get_by_text(categoria).nth(2)).to_be_visible()

    def verificar_nombre_producto(self, nombre):
        expect(self.page.get_by_role("heading", name=nombre)).to_be_visible()

    def verificar_precio_producto(self,precio):
        expect(self.page.get_by_text(precio)).to_be_visible()
    