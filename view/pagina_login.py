import flet as ft

def login_page(page: ft.Page, pagina_inicial, pagina_medicamento, pagina_estoque, pagina_relatorio):  # Adiciona 'pagina_relatorio'
    page.title = "Login - Controle de Medicamentos"
    page.bgcolor = "#ff3a3a"

    login_container = ft.Column(
        controls=[
            ft.Text("Login", size=30, weight="bold", color="white"),
            ft.TextField(label="Usuário", width=300),
            ft.TextField(label="Senha", password=True, width=300),
            ft.ElevatedButton("Entrar", on_click=lambda e: entrar_clicked(e, page, pagina_inicial, pagina_medicamento, pagina_estoque, pagina_relatorio))  # Passa 'pagina_relatorio'
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

def entrar_clicked(e, page, pagina_inicial, pagina_medicamento, pagina_estoque, pagina_relatorio):  # Adiciona 'pagina_relatorio'
    # Aqui você pode adicionar a lógica de verificação do login
    page.clean()
<<<<<<< HEAD
    pagina_inicial(page, pagina_medicamento, pagina_estoque, pagina_relatorio)  # Passa 'pagina_relatorio'
=======
    pagina_inicial(page, pagina_medicamento, pagina_estoque, pagina_relatorio)  # Passa 'pagina_relatorio'
>>>>>>> task-atualizacao-interface
