import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from config import DB

def valida_usuario(usuario, senha):
    banco = DB()
    cursor = banco.conexao_db()
    cursor.execute("SELECT * FROM usuario WHERE nome = %s AND senha = %s", (usuario, senha))
    dados = cursor.fetchall()

    if dados:
        return True
    else:
        return False


import flet as ft
from valida_usuario import valida_usuario  # Importa a função de validação

def login_page(page: ft.Page, pagina_inicial, pagina_medicamento, pagina_estoque, pagina_relatorio):
    page.title = "Login - Controle de Medicamentos"
    page.bgcolor = "#ff3a3a"

    # Criação dos campos de entrada e armazenamento em variáveis
    usuario_field = ft.TextField(label="Usuário", width=300, bgcolor="white")
    senha_field = ft.TextField(label="Senha", password=True, width=300, bgcolor="white")

    # Criação do campo de mensagem para exibir erros de login
    mensagem_erro = ft.Container(
        content=ft.Text("Usuário ou Senha inválidos", size=16, color="black"),
        bgcolor="white",  # Cor de fundo da caixa de erro
        padding=10,
        width=300,
        border_radius=5,
        visible=False  # Inicialmente escondido
    )

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
                    usuario_field.value,  # Passa diretamente o valor do usuário
                    senha_field.value,  # Passa diretamente o valor da senha
                    mensagem_erro,  # Passa a caixa de erro para atualização
                    pagina_inicial,
                    pagina_medicamento,
                    pagina_estoque,
                    pagina_relatorio
                )
            ),
            mensagem_erro  # Adiciona a caixa de mensagem ao container
        ],
        alignment=ft.MainAxisAlignment.CENTER,  # Centraliza os itens dentro do contêiner
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

def entrar_clicked(e, page, usuario, senha, mensagem_erro, pagina_inicial, pagina_medicamento, pagina_estoque, pagina_relatorio):
    # Verifica se o login é válido usando a função 'valida_usuario'
    if valida_usuario(usuario, senha):
        page.clean()
        pagina_inicial(page, pagina_medicamento, pagina_estoque, pagina_relatorio)
    else:
        # Exibe a mensagem de erro se o login falhar
        mensagem_erro.visible = True  # Torna a caixa de erro visível
        page.update()
