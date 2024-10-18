import flet as ft
from pagina_inicial import pagina_inicial  # Importando a função corretamente

def login_page(page: ft.Page):
    page.title = "Login - Controle de Medicamentos"
    page.bgcolor = "#ff3a3a"  # Define a cor de fundo da página como vermelho

    # Cria um contêiner para centralizar o conteúdo
    login_container = ft.Column(
        controls=[
            ft.Text("Login", size=30, weight="bold", color="white"),  # Título da página
            ft.TextField(label="Usuário", width=300),  # Campo do usuário
            ft.TextField(label="Senha", password=True, width=300),  # senha
            ft.ElevatedButton("Entrar", on_click=lambda e: entrar_clicked(e, page))  # botão entrar
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10,  # Espaçamento entre os controles
    )

    # Adiciona o contêiner à página
    page.add(login_container)

def entrar_clicked(e, page):
    # Aqui é pra adicionar a lógica do login para verificar se vai logar ou não
    page.clean()  # Limpa a página de login
    pagina_inicial(page)  # Direciona para a página principal após o login
