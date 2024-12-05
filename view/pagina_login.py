import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import flet as ft
from controler.control_login import valida_usuario  # Import ajustado após path

def login_page(page: ft.Page, pagina_inicial, pagina_medicamento, pagina_estoque, pagina_relatorio):
    page.title = "Login - Controle de Medicamentos"
    page.bgcolor = "#ff3a3a"

    # Campos de entrada
    usuario_field = ft.TextField(label="Usuário", width=300, bgcolor="white")
    senha_field = ft.TextField(label="Senha", password=True, width=300, bgcolor="white")

    # Mensagem de erro
    mensagem_erro = ft.Container(
        content=ft.Text("Usuário ou Senha inválidos", size=16, color="black"),
        bgcolor="white",
        padding=10,
        width=300,
        border_radius=5,
        visible=False
    )

    # Layout do formulário
    login_container = ft.Column(
        controls=[
            ft.Text("Login", size=30, weight="bold", color="white"),
            usuario_field,
            senha_field,
            ft.ElevatedButton(
                "Entrar",
                on_click=lambda e: entrar_clicked(
                    e,
                    page,
                    [usuario_field.value, senha_field.value],
                    mensagem_erro,
                    pagina_inicial,
                    pagina_medicamento,
                    pagina_estoque,
                    pagina_relatorio
                )
            ),
            mensagem_erro
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10
    )

    page.add(ft.Container(
        content=login_container,
        alignment=ft.Alignment(0, 0),
        padding=20,
        height=page.window_height,
        width=page.window_width
    ))

def entrar_clicked(e, page, solicitacao, mensagem_erro, pagina_inicial, pagina_medicamento, pagina_estoque, pagina_relatorio):
    mensagem_erro.visible = False  # Redefine a visibilidade da mensagem
    if valida_usuario(solicitacao):
        page.clean()
        pagina_inicial(page, pagina_medicamento, pagina_estoque, pagina_relatorio)
    else:
        mensagem_erro.visible = True
        page.update()
