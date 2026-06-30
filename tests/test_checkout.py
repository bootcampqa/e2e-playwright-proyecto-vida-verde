from playwright.sync_api import Page, expect


def test_realizar_compra_datos_validos(page: Page):
    print("Given la usuaria esta en la página de productos 'https://web-qa.dev.adalab.es/products'")
    page.goto("https://web-qa.dev.adalab.es/products")

    print("and filtra por nombre 'palas'")
    page.get_by_role("searchbox", name="Nombre").fill("palas")

    print("and añade el producto al carrito")
    page.get_by_role("button", name="Añadir Juego de Palas al").click()

    print("and hace clic en finalizar compra")
    page.get_by_role("link", name="Finalizar Compra").click()

    print("and hace clic en 'Proceder al pago'")
    page.get_by_role("link", name="Proceder al Pago").click()

    print("then debe ver en la página de checkout el resumen del pedido con el producto 'Juego de Palas'")
    expect(page.get_by_role("heading", name="Resumen del Pedido")).to_be_visible()

    print("and nombre del producto es 'Juego de Palas'")
    expect(page.get_by_role("listitem").filter(
        has_text="Juego de Palas")).to_be_visible()
    
    print("And el precio del producto es '15.99 €'")
    expect(page.get_by_role("listitem").filter(
        has_text="Juego de Palas15.99 €").locator("data")).to_be_visible()

    print("And el subtotal del producto es '15.99 €'")
    expect(page.get_by_role("definition").filter(
        has_text="15.99 €").locator("data")).to_be_visible()

    print("and el iva es '3.36 €'")
    expect(page.get_by_text("3.36 €")).to_be_visible()

    print("and el envio es '5.00 €'")
    expect(page.get_by_text("5.00 €")).to_be_visible()

    print("and el total es '24.35 €'")
    expect(page.get_by_text("24.35 €")).to_be_visible()

    print("When rellena el formulario con el nombre 'Elena Nito del Bosque'")
    page.get_by_role(
        "textbox", name="Nombre Completo *").fill("Elena Nito del Bosque")

    print("and rellena el email 'test@gmail.com'")
    page.get_by_role("textbox", name="Email *").fill("test@gmail.com")

    print("and rellena la dirección 'Calle del Árbol, 8, Burgos'")
    page.get_by_role(
        "textbox", name="Dirección *").fill("Calle del Árbol, 8, Burgos")

    print("and rellena la tarjeta válida '4242 4242 4242 4242'")
    page.get_by_role(
        "textbox", name="Número de Tarjeta de Crédito *").fill("4242 4242 4242 4242")

    print("and hace clic en el botón 'Completar compra'")
    page.get_by_role("button", name="Completar Compra").click()

    print("then debe ver el mensaje 'Compra Realizada con Éxito'")
    expect(page.get_by_role(
        "heading", name="¡Compra Realizada con Éxito!")).to_be_visible()

    print("and debe ver el resumen del pedido con el producto 'Juego de Palas'")
    expect(page.get_by_text("Juego de Palas")).to_be_visible()

    print("and el precio del producto '15.99 €'")
    expect(page.get_by_role("listitem").filter(
        has_text="Juego de Palas15.99 €").locator("data")).to_be_visible()

    print("and el subtotal '15.99 €'")
    expect(page.get_by_role("definition").filter(
        has_text="15.99 €").locator("data")).to_be_visible()

    print("and el iva '3.36 €'")
    expect(page.get_by_role("definition").filter(
        has_text="3.36 €").locator("data")).to_be_visible()
   
    print("and el envio '5.00 €'")
    expect(page.get_by_role("definition").filter(
        has_text="5.00 €").locator("data")).to_be_visible()

    print("and el total '24.35 €'")
    expect(page.get_by_role("definition").filter(
        has_text="24.35 €").locator("data")).to_be_visible()

    print("and hace clic el botón 'Ir al Inicio'")
    page.get_by_role("link", name="Ir al Inicio", exact=True).click()

    print("then debe estar la página de inicio 'https://web-qa.dev.adalab.es/'")
    # Comprobamos que la url de la página contiene la url 'https://web-qa.dev.adalab.es/'
    expect(page).to_have_url('https://web-qa.dev.adalab.es/')

    # Comprobamos que el título de la página sea 'Vida Verde'
    expect(page.get_by_role("heading", name="Vida Verde")).to_be_visible()

    # Comprobamos que el título de la página sea 'Inicio | Vida Verde'
    expect(page).to_have_title("Inicio | Vida Verde")

    # Comprobamos que en la página hay un botón 'Ver Productos'
    expect(page.get_by_role("link", name="Ver Productos")).to_be_visible()


def test_realizar_compra_con_tarjeta_invalida(page: Page):
    print("Given la usuaria esta en la página de productos 'https://web-qa.dev.adalab.es/products'")
    page.goto("https://web-qa.dev.adalab.es/products")

    print("and filtra por nombre 'Palas'")
    page.get_by_role("searchbox", name="Nombre").fill("palas")

    print("and añade el producto al carrito")
    page.get_by_role("button", name="Añadir Juego de Palas al").click()

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