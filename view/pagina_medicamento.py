import flet as ft

def pagina_medicamento(page: ft.Page, pagina_inicial, pagina_estoque, pagina_relatorio):
    page.title = "Cadastro de Medicamentos"
    page.bgcolor = "#ff3a3a"
    page.padding = 0
    page.scroll = "adaptive"

    def voltar_para_inicial(e):
        page.clean()
        pagina_inicial(page, pagina_medicamento, pagina_estoque, pagina_relatorio)  # Passa todas as páginas incluindo 'pagina_relatorio'

    # Borda azul com o título
    title_container = ft.Container(
        content=ft.Text("Cadastro de Medicamentos", size=24, weight="bold", color="white"),
        bgcolor="#2e3bc8",
        padding=ft.padding.all(10)
    )

    # Formulário de cadastro
    formulario = ft.Column(
        controls=[
            ft.TextField(label="Nome do Medicamento", width=300, bgcolor="white"),
            ft.TextField(label="Lote", width=300, bgcolor="white"),
            ft.TextField(label="Validade", width=300, bgcolor="white"),
            ft.TextField(label="Código de Barras", width=300, bgcolor="white"),
            ft.TextField(label="Laboratório", width=300, bgcolor="white"),
            ft.TextField(label="Quantidade", width=300, bgcolor="white"),
            ft.ElevatedButton("Cadastrar", bgcolor="#2e3bc8", color="white"),
            ft.ElevatedButton("Voltar", on_click=voltar_para_inicial, bgcolor="#2e3bc8", color="white"),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    # Container para centralizar o formulário na página
    content_container = ft.Container(
        content=formulario,
        alignment=ft.Alignment(0, 0),
        padding=ft.padding.all(20)
    )

    # Adicionando a borda e o conteúdo
    page.add(title_container)  # Adiciona o título
    page.add(content_container)  # Adiciona o layout centralizado
