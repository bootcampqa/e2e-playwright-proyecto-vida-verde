from playwright.sync_api import Page, expect
from pages.carrito_page import CarritoPage
from pages.components.menu import MenuComponent
from pages.productos_page import ProductosPage


def test_carrito(page: Page):

    productos_page = ProductosPage(page)
    carrito_page = CarritoPage(page)
    menu_component = MenuComponent(page)

    print("Given el usuario abre la página de productos")
    productos_page.visitar_productos()
    

    print("When filtra por producto 'Regadera'")
    productos_page.filtrar_por_nombre("regadera")
    

    print("And agrega el producto al carrito")
    productos_page.agregar_producto_al_carrito("Regadera Metálica")

    print("And filtra por producto 'Tijeras'")
    productos_page.filtrar_por_nombre("tijeras")
  

    print("And agrega el producto al carrito")
    productos_page.agregar_producto_al_carrito("Tijeras de Podar")


    print("When visita el carrito")
    menu_component.clic_carrito_compra()

    print("Then debe ver el producto Regadera y su precio")
    carrito_page.verificar_producto_carrito("Regadera Metálica")
    carrito_page.verificar_precio_carrito("24.00 €")
    
  

    print("And debe ver el producto Tijeras y su precio")
    carrito_page.verificar_producto_carrito("Tijeras de Podar")
    carrito_page.verificar_precio_carrito("18.50 €")

    print("And debe ver el resumen del pedido:")
    print("Subtotal:")
    carrito_page.verificar_precio_carrito("42.50 €")

    print("IVA 21%")
    carrito_page.verificar_precio_carrito("8.92 €")
  
    print("Envío")
    carrito_page.verificar_precio_carrito("5.00 €")
    print("Total")
    carrito_page.verificar_precio_carrito("56.42 €")


    print("When elimina el producto Regadera")
    carrito_page.eliminar_producto_carrito("Regadera Metálica")

    print("Then no debe ver el producto Regadera")
    carrito_page.verificar_producto_eliminado_carrito("Regadera Metálica")


    print("And ve resumen del pedido actualizado")
    print("Subtotal")
    carrito_page.verificar_precio_carrito("18.50 €")
    print("IVA 21%")
    carrito_page.verificar_precio_carrito("3.88 €")
    
    print("Envío")
    carrito_page.verificar_precio_carrito("5.00 €")
    print("total")
    carrito_page.verificar_precio_carrito("27.38 €")

    print("When vacía el carrito")
    carrito_page.vaciar_carrito()
    

    print("Then debe ver mensaje carrito vacío")
    carrito_page.verificar_carrito_vacio()

    print("And hace clic en Ver Productos")
    carrito_page.ver_productos()

    print("Then debe ver la página de productos")
    productos_page.verificar_titulo()
   