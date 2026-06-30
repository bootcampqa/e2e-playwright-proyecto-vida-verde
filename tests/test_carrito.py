from playwright.sync_api import Page, expect

def test_carrito(page: Page):
    print("Given el usuario abre la página de productos")
    page.goto("https://web-qa.dev.adalab.es/products")

    print("When filtra por producto 'Regadera'")
    page.get_by_role("searchbox", name="Nombre").fill("regadera")

    print("And agrega el producto al carrito")
    page.get_by_role("button", name="Añadir Regadera Metálica").click()

    print("And filtra por producto 'Tijeras'")
    page.get_by_role("searchbox", name="Nombre").fill("tijeras")
   

    print("And agrega el producto al carrito")
    page.get_by_role("button", name="Añadir Tijeras de Podar").click()

    print("When visita el carrito")
    page.get_by_role("link", name="Carrito de compra").click()

    print("Then debe ver el producto Regadera y su precio")
    expect(page.get_by_role("heading", name="Regadera Metálica")).to_be_visible()
    expect(page.get_by_text("24.00 €")).to_be_visible()

    print("And debe ver el producto Tijeras y su precio")
    expect(page.get_by_role("heading", name="Tijeras de Podar")).to_be_visible()
    expect(page.get_by_text("18.50 €")).to_be_visible()

    print("And debe ver el resumen del pedido:")
    print("Subtotal:")
    expect(page.get_by_text("42.50 €")).to_be_visible()
    print("IVA 21%")
    expect(page.get_by_text("8.92 €")).to_be_visible()
    print("Envío")
    expect(page.get_by_text("5.00 €")).to_be_visible()
    print("Total")
    expect(page.get_by_text("56.42 €")).to_be_visible()

    print("When elimina el producto Regadera")
    page.get_by_role("button", name="Eliminar Regadera Metálica").click()

    print("Then no debe ver el producto Regadera")
    expect(page.get_by_role("heading", name="Regadera Metálica")).not_to_be_visible()


    print("And ve resumen del pedido actualizado")
    print("Subtotal")
    expect(page.get_by_label("Resumen del Pedido").get_by_text("18.50 €")).to_be_visible()
    print("IVA 21%")
    expect(page.get_by_text("3.88 €")).to_be_visible()
    print("Envío")
    expect(page.get_by_text("5.00 €")).to_be_visible()
    print("total")
    expect(page.get_by_text("27.38 €")).to_be_visible()

    print("When vacía el carrito")
    page.get_by_role("button", name="Vaciar Carrito").click()

    print("Then debe ver mensaje carrito vacío")
    expect(page.get_by_text("Tu carrito está vacío")).to_be_visible()

    print("And hace clic en Ver Productos")
    page.get_by_role("link", name="Ver Productos").click()

    print("Then debe ver la página de productos")
    expect(page.get_by_role("heading", name="Catálogo de Productos")).to_be_visible()