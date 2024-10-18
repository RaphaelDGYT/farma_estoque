import flet as ft  # para o flet funcionar

# Função da página principal
def pagina_inicial(page: ft.Page):
    page.title = "Página Inicial - Controle de Medicamentos"
    page.bgcolor = "#ff3a3a"  # cor vermelha
    page.padding = 0
    page.scroll = "adaptive"
    
    # centralizar
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Barra azul
    navbar = ft.Container(
        content=ft.Row(
            controls=[
                ft.Icon(ft.icons.HOME, color="white"),
                ft.Text("ESTOQUE", style=ft.TextStyle(color="white")),
                ft.Text("MEDICAMENTO", style=ft.TextStyle(color="white")),
                ft.Text("RELATÓRIO", style=ft.TextStyle(color="white")),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            height=50
        ),
        bgcolor="#2e3bc8",
        padding=0
    )

    # os AVISOS
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

    # RESUMO DIARIO
    resumo_diario = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("RESUMO DIÁRIO", size=20, weight="bold", color="white"),
                ft.ElevatedButton(" NOVOS MEDICAMENTOS", width=300),
                ft.ElevatedButton(" RETIRADA DE MEDICAMENTOS", width=300),
                ft.ElevatedButton(" NOVOS LOTES", width=300)
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

    # Adicionar elementos à página
    page.add(navbar)
    page.add(layout_principal)
