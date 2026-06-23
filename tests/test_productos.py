from playwright.sync_api import Page, expect
from pages.productos_page import ProductosPage

def test_ver_productos_y_detalles(page: Page):

    productos_page = ProductosPage(page)

    print("Given la usuaria abre la página de productos")
    productos_page.visitar_productos()

    print("Then la usuaria debe ver el título 'Catálogo de Productos'")
    # Comprobamos que la página contiene el título "Catálogo de Productos"
    productos_page.verificar_titulo()

    print("And la usuaria debe ver la categoría del producto 'Plantas'")
    # Comprobamos que la usuaria ve la categoría del producto "Plantas"
    productos_page.verificar_categoria("Plantas")

    print("And la usuaria debe ver el nombre del producto 'Ficus Lyrata'")
    # Comprobamos que la usuaria ve el nombre del producto "Fycus Lyrata"
    productos_page.verificar_nombre_producto("Ficus Lyrata")

    print("And la usuaria debe ver el precio del producto '35.00 €'")
    # Comprobamos que la usuaria ve el precio del producto "35.00 €"
    productos_page.verificar_precio_producto("35.00 €")