import flet as ft

def pagina_inicial(page: ft.Page, pagina_medicamento, pagina_estoque, pagina_relatorio):  # Adiciona 'pagina_relatorio'
    page.title = "Página Inicial - Controle de Medicamentos"
    page.bgcolor = "#ff3a3a"
    page.padding = 0
    page.scroll = "adaptive"

    # Função para ir à página de estoque
    def ir_para_estoque(e):
        page.clean()
        pagina_estoque(page, pagina_inicial, pagina_medicamento, pagina_relatorio)  # Passa 'pagina_relatorio'

    # Função para ir à página de medicamentos
    def ir_para_medicamento(e):
        page.clean()
        pagina_medicamento(page, pagina_inicial, pagina_estoque, pagina_relatorio)  # Passa 'pagina_relatorio'

    # Função para ir à página de relatório
    def ir_para_relatorio(e):
        page.clean()
        pagina_relatorio(page, pagina_inicial, pagina_medicamento, pagina_estoque)  # Passa as páginas necessárias

    # Função para desligar o sistema
    def desligar_sistema(e, page):
        # Lógica de desligamento do sistema, se necessário
        page.window_close()  # Fechar a janela da aplicação corretamente

    # Navbar com botões de navegação
    navbar = ft.Container(
        content=ft.Row(
            controls=[
                ft.ElevatedButton("ESTOQUE", on_click=ir_para_estoque, bgcolor="#2e3bc8", color="white"),
                ft.ElevatedButton("MEDICAMENTO", on_click=ir_para_medicamento, bgcolor="#2e3bc8", color="white"),
                ft.ElevatedButton("RELATÓRIO", on_click=ir_para_relatorio, bgcolor="#2e3bc8", color="white"),
                ft.ElevatedButton("SAIR", on_click=lambda e: desligar_sistema(e, page), bgcolor="#ff0000", color="white"),  # Botão para sair
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            height=50
        ),
        bgcolor="#2e3bc8",
        padding=0
    )

    # Avisos
    avisos = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("AVISOS", size=20, weight="bold", color="white"),
                ft.ElevatedButton("SEU MEDICAMENTO ESTÁ ACABANDO", width=300),
                ft.ElevatedButton("SEU MEDICAMENTO ESTÁ VENCENDO", width=300),
                ft.ElevatedButton("SEU MEDICAMENTO ESTÁ SEM ESTOQUE", width=300)
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=5
        ),
        padding=ft.padding.all(200)
    )

    # Resumo diário
    resumo_diario = ft.Container(
        content=ft.Column(
            controls=[ 
                ft.Text("RESUMO DIÁRIO", size=20, weight="bold", color="white"),
                ft.ElevatedButton("NOVOS MEDICAMENTOS", width=300),
                ft.ElevatedButton("RETIRADA DE MEDICAMENTOS", width=300),
                ft.ElevatedButton("NOVOS LOTES", width=300)
            ],
            alignment=ft.MainAxisAlignment.END,
            spacing=5
        ),
        padding=ft.padding.all(200)
    )

    # Layout principal
    layout_principal = ft.Row(
        controls=[avisos, resumo_diario],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True
    )

    # Adiciona navbar e layout principal à página
    page.add(navbar)
    page.add(layout_principal)
