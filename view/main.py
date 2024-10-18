import flet as ft
from pagina_login import login_page  # aqui ele puxa a pagina de login

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  # aqui centraliza na vertical
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # aqui ele centraliza na horizontal
    login_page(page)  # aqui ele vai iniciar a o programa


ft.app(target=main) # para tudo funfar
