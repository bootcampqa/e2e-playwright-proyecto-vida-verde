from playwright.sync_api import Page, expect

from pages.components.menu import MenuComponent
from pages.contacto_page import ContactoPage
from pages.inicio_page import InicioPage
from pages.productos_page import ProductosPage
from pages.quienes_somos_page import QuienesSomosPage

def test_visit(page: Page):
    inicio_page = InicioPage(page)
    menu_component = MenuComponent(page)
    quienes_somos_page = QuienesSomosPage(page)
    productos_page = ProductosPage(page)
    contacto_page = ContactoPage(page)
    

    print("Given the user opens the home page")
    inicio_page.visitar_inicio()

    print("When they visit the menu “About us”")
    menu_component.clic_menu("Quiénes Somos")
   
    print("And they should see the title “About Us”")
    quienes_somos_page.verificar_titulo()
    print("Then they should see the URL “[https://web-qa.dev.adalab.es/about”](https://web-qa.dev.adalab.es/about”)")
    quienes_somos_page.verificar_url()

    print("When they visit the menu “Products”")
    menu_component.clic_menu("Productos")

    print("And they should see the title “Product Catalog”")
    productos_page.verificar_titulo()
   
    expect(page.get_by_role("heading", name="Catálogo de Productos")).to_be_visible()
    print("Then they should see the URL “[https://web-qa.dev.adalab.es/products”](https://web-qa.dev.adalab.es/products”")
    productos_page.verificar_url()

    print("When they visit the menu “Contact”")
    menu_component.clic_menu("Contacto")
  
    print("And they should see the title “Contact Us”")
    contacto_page.verificar_titulo()
    print("Then they should see the URL “[https://web-qa.dev.adalab.es/products”](https://web-qa.dev.adalab.es/products”")
    contacto_page.verificar_url()
  

    print("When they visit the menu “Home”")
    menu_component.clic_menu("Inicio")

    print("And they should see the title “Vida Verde”")
    inicio_page.verificar_titulo()
    print("Then they should see the URL “[https://web-qa.dev.adalab.es/”](https://web-qa.dev.adalab.es/”)")
    inicio_page.verificar_url()