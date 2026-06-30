from playwright.sync_api import Page, expect

from pages.carrito_page import CarritoPage
from pages.checkout_page import CheckoutPage
from pages.components.menu import MenuComponent
from pages.confirmation_page import ConfirmationPage
from pages.inicio_page import InicioPage
from pages.productos_page import ProductosPage


def test_realizar_compra_datos_validos(page: Page):
    productos_page = ProductosPage(page)
    menu_component = MenuComponent(page)
    carrito_page = CarritoPage(page)
    checkout_page = CheckoutPage(page)
    confirmation_page=ConfirmationPage(page)
    inicio_page = InicioPage(page)


    print("Given la usuaria esta en la página de productos 'https://web-qa.dev.adalab.es/products'")
    productos_page.visitar_productos()

    print("and filtra por nombre 'palas'")
    productos_page.filtrar_por_nombre("palas")
    

    print("and añade el producto al carrito")
    productos_page.agregar_producto_al_carrito("Juego de Palas")
   

    print("and hace clic en finalizar compra")
    menu_component.clic_finalizar_compra()

    print("and hace clic en 'Proceder al pago'")
    carrito_page.proceder_al_pago()

    print("then debe ver en la página de checkout el resumen del pedido con el producto 'Juego de Palas'")
    checkout_page.verificar_titulo()

    print("and nombre del producto es 'Juego de Palas'")
    checkout_page.verificar_nombre_producto("Juego de Palas")
    
    print("And el precio del producto es '15.99 €'")
    checkout_page.verificar_precio_producto("15.99 €")

    print("And el subtotal del producto es '15.99 €'")
    checkout_page.verificar_desglose_precio("15.99 €")
   

    print("and el iva es '3.36 €'")
    checkout_page.verificar_desglose_precio("3.36 €")
    

    print("and el envio es '5.00 €'")
    checkout_page.verificar_desglose_precio("5.00 €")

    print("and el total es '24.35 €'")
    checkout_page.verificar_total("24.35 €")

    print("When rellena el formulario con el nombre 'Elena Nito del Bosque'")
    checkout_page.rellenar_nombre("Elena Nito del Bosque")
   

    print("and rellena el email 'test@gmail.com'")
    checkout_page.rellenar_email("test@gmail.com")

    print("and rellena la dirección 'Calle del Árbol, 8, Burgos'")
    checkout_page.rellenar_direccion("Calle del Árbol, 8, Burgos")

    print("and rellena la tarjeta válida '4242 4242 4242 4242'")
    checkout_page.rellenar_tarjeta("4242 4242 4242 4242")

    print("and hace clic en el botón 'Completar compra'")
    checkout_page.completar_compra()

    print("then debe ver el mensaje 'Compra Realizada con Éxito'")
    confirmation_page.verificar_mensaje_compra_exito()

    print("and debe ver el resumen del pedido con el producto 'Juego de Palas'")
    confirmation_page.verificar_producto("Juego de Palas")

    print("and el precio del producto '15.99 €'")
    confirmation_page.verificar_precio_producto("15.99 €")

    print("and el subtotal '15.99 €'")
    confirmation_page.verificar_desglose_producto("15.99 €")

    print("and el iva '3.36 €'")
    confirmation_page.verificar_desglose_producto("3.36 €")
   
    print("and el envio '5.00 €'")
    confirmation_page.verificar_desglose_producto("5.00 €")

    print("and el total '24.35 €'")
    confirmation_page.verificar_desglose_producto("24.35 €")

    print("and hace clic el botón 'Ir al Inicio'")
    confirmation_page.ir_a_inicio()

    print("then debe estar la página de inicio 'https://web-qa.dev.adalab.es/'")
    # Comprobamos que la url de la página contiene la url 'https://web-qa.dev.adalab.es/'
    inicio_page.verificar_url()


def test_realizar_compra_con_tarjeta_invalida(page: Page):
    print("Given la usuaria esta en la página de productos 'https://web-qa.dev.adalab.es/products'")
    page.goto("https://web-qa.dev.adalab.es/products")

    print("and filtra por nombre 'Palas'")
    page.get_by_role("searchbox", name="Nombre").fill("palas")

    print("and añade el producto al carrito")
    page.get_by_role("button", name="Añadir Juego de Palas").click()

    print("and hace clic en 'Finalizar Compra'")
    page.get_by_role("link", name="Finalizar Compra").click()

    print("and hace clic en 'Proceder al Pago'")
    page.get_by_role("link", name="Proceder al Pago").click()

    print("When rellena el formulario con el nombre 'Elena Nito del Bosque'")
    page.get_by_role(
        "textbox", name="Nombre Completo *").fill("Elena Nito del Bosque")

    print("and rellena el email 'test@gmail.com'")
    page.get_by_role("textbox", name="Email *").fill("test@gmail.com")

    print("and rellena la dirección 'Calle del Árbol, 8, Burgos'")
    page.get_by_role(
        "textbox", name="Dirección *").fill("Calle del Árbol, 8, Burgos")

    print("and rellena la tarjeta inválida '1234'")
    page.get_by_role(
        "textbox", name="Número de Tarjeta de Crédito *").fill("1234")

    print("and hace clic en Completar Compra")
    page.get_by_role("button", name="Completar compra").click()

    print("then debe ver un mensaje de error numero de tarjeta invalido")
    expect(page.get_by_text("El número de tarjeta debe")).to_be_visible()


def test_realizar_compra_con_tarjeta_vacia(page: Page):
    print("Given la usuaria esta en la página de productos 'https://web-qa.dev.adalab.es/products'")
    page.goto("https://web-qa.dev.adalab.es/products")

    print("and filtra por nombre 'Palas'")
    page.get_by_role("searchbox", name="Nombre").fill("Palas")

    print("and añade el producto al carrito")
    page.get_by_role("button", name="Añadir juego de Palas al carrito").click()

    print("and hace clic en ‘Finalizar Compra’")
    page.get_by_role("link", name="Finalizar Compra").click()

    print("and hace clic en ‘Proceder al Pago’")
    page.get_by_role("link", name="Proceder al Pago").click()

    print("When rellena el formulario con el nombre ‘Elena Nito del Bosque’")
    page.get_by_role(
        "textbox", name="Nombre Completo *").fill("Elena nito del Bosque")

    print("and rellena el email ‘test@gmail.com’")
    page.get_by_role("textbox", name="Email *").fill("test@gamil.com")

    print("and rellena la dirección ‘Calle del Árbol., 8, Burgos’")
    page.get_by_role(
        "textbox", name="Dirección *").fill("Calle del Árbol., 8, Burgo")

    print("and hace clic en ‘Completar Compra’")
    page.get_by_role("button", name="Completar Compra").click()

    print("then NO debe ver el mensaje 'Compra realizada con éxito'")
    expect(page.get_by_text("Compra realizada con éxito")).not_to_be_visible()