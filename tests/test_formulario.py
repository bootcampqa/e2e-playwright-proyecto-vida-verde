from playwright.sync_api import Page, expect

from pages.contacto_page import ContactoPage

def test_enviar_formulario_email_invalido(page: Page):

    contacto_page = ContactoPage(page)

    print("Given el usuario abre la página de contacto")
    contacto_page.visitar_contacto()
    
    print("When rellena el campo nombre")
    contacto_page.rellenar_nombre("Reyes Cuesta")

    print("And rellena el campo email inválido")
    contacto_page.rellenar_email("test")
   
    print("And rellena el campo mensaje")
    contacto_page.rellenar_mensaje("Mensaje de prueba")

    print("And envia el mensaje")
    contacto_page.enviar_mensaje()
    
    print("Then debe ver un mensaje de error")
    contacto_page.verificar_mensaje_error_email()



def test_enviar_mensaje_campos_obligatorios(page: Page):
    contacto_page = ContactoPage(page)
    print("\nGiven user visits the Contact page")
    contacto_page.visitar_contacto()

    print ("When they fill the form filed Name with “Reyes Cuesta”")
    contacto_page.rellenar_nombre("Reyes Cuesta")

    print ("And fill the field Email with “test@gmail.com”")
    contacto_page.rellenar_email("test@gmail.com")
    

    print ("And fill the field Message with “Test message”")
    contacto_page.rellenar_mensaje("Test message")
    

    print ("And clicks on Send message")
    contacto_page.enviar_mensaje()
    

    print ("Then the user must see a success message")
    contacto_page.verificar_mensaje_exito_contacto()

def test_enviar_formulario_email_vacio(page: Page):
    contacto_page = ContactoPage(page)
    print("Given el usuario abre la página de contacto")
    contacto_page.visitar_contacto()

    print("When rellena el campo nombre")
    contacto_page.rellenar_nombre("Lluvia aguilar")
  
    
    print("And deja el campo email vacío")
   

    print("And rellena el campo mensaje")
    contacto_page.rellenar_mensaje("Mensaje de Prueba")
   

    print("And envia el mesaje")
    contacto_page.enviar_mensaje()

    print("Then debe ver un mensaje de error")
    contacto_page.verificar_mensaje_error_email_obligatorio()
    