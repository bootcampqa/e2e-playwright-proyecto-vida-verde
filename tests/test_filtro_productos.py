from playwright.sync_api import Page, expect

from pages.productos_page import ProductosPage

def test_filtrar_nombre_precio_categoria_con_resultados(page: Page):
    productos_page = ProductosPage(page)

    print("Given el usuario abre la página de productos")
    productos_page.visitar_productos()

    print("When filtra por nombre “Sanse”")
    productos_page.filtrar_por_nombre("Sanse")

    print("And filtra por categoria “Plantas”")
    productos_page.filtrar_por_categoria("Plantas")
    
    print("And filtra por precio minimo “10”")
    productos_page.filtrar_por_precio_minimo("10")
    
    print("And filtra por precio máximo “25”")
    productos_page.filtrar_por_precio_maximo("25")

    print("Then debe ver el producto “Sansevieria”")
    productos_page.verificar_nombre_producto("Sansevieria")
   

    print("And debe ver la categoría “Plantas”")
    productos_page.verificar_categoria("Plantas")


    print("And debe ver el precio “22”")
    productos_page.verificar_precio_producto("22.00 €")
    


def test_filtrar_sin_resultados(page: Page):
    productos_page = ProductosPage(page)
    print("Given el usuario abre la página de productos")
    productos_page.visitar_productos()

    print("When filtra por nombre no existente “Test”")
    productos_page.filtrar_por_nombre("Test")
    

    print("Then ve el mensaje no se encontraron productos")
    productos_page.verificar_mensaje_no_resultados()