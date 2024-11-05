import flet as ft

def pagina_relatorio(page: ft.Page, pagina_inicial, pagina_medicamento, pagina_estoque):
    page.title = "Relatório"
    page.bgcolor = "#ff3a3a"

    # Título da página
    header = ft.Row(
        controls=[
            ft.Text("Relatório de Medicamentos", size=30, weight="bold", color="white"),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

<<<<<<< HEAD
    # Adicione elementos de relatório aqui, como gráficos e tabelas
    tabela = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Código de Barras")),
            ft.DataColumn(ft.Text("Nome do Medicamento")),  # Nova coluna para o nome do medicamento
            ft.DataColumn(ft.Text("Classe Terapêutica")),
            ft.DataColumn(ft.Text("Lote")),
            ft.DataColumn(ft.Text("Validade")),
            ft.DataColumn(ft.Text("Quantidade")),
        ],
        rows=[
            ft.DataRow(cells=[
                ft.DataCell(ft.Text("1234567890123")),
                ft.DataCell(ft.Text("Amoxicilina")),  # Exemplo de nome do medicamento
                ft.DataCell(ft.Text("Antibiótico")),
                ft.DataCell(ft.Text("ABC123")),
                ft.DataCell(ft.Text("2025-12-31")),
                ft.DataCell(ft.Text("50")),
=======
    # Tabela com texto das células em branco
    tabela = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Código de Barras", color="white")),
            ft.DataColumn(ft.Text("Nome do Medicamento", color="white")),  # Nova coluna para o nome do medicamento
            ft.DataColumn(ft.Text("Classe Terapêutica", color="white")),
            ft.DataColumn(ft.Text("Lote", color="white")),
            ft.DataColumn(ft.Text("Validade", color="white")),
            ft.DataColumn(ft.Text("Quantidade", color="white")),
        ],
        rows=[
            ft.DataRow(cells=[
                ft.DataCell(ft.Text("1234567890123", color="white")),
                ft.DataCell(ft.Text("Amoxicilina", color="white")),  # Exemplo de nome do medicamento
                ft.DataCell(ft.Text("Antibiótico", color="white")),
                ft.DataCell(ft.Text("ABC123", color="white")),
                ft.DataCell(ft.Text("2025-12-31", color="white")),
                ft.DataCell(ft.Text("50", color="white")),
>>>>>>> task-atualizacao-interface
            ]),
            # Adicione mais linhas conforme necessário
        ],
    )

    # Botões para exportar e voltar
    controls = ft.Row(
        controls=[
            ft.ElevatedButton("Exportar PDF", on_click=lambda e: exportar_pdf(page)),
            ft.ElevatedButton("Exportar CSV", on_click=lambda e: exportar_csv(page)),
            ft.ElevatedButton("Voltar", on_click=lambda e: voltar(page, pagina_inicial, pagina_medicamento, pagina_estoque, pagina_relatorio)),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )

    # Adicionando todos os elementos à página
    page.add(header, tabela, controls)

def exportar_pdf(page):
    print("Exportando PDF...")

def exportar_csv(page):
    print("Exportando CSV...")

def voltar(page, pagina_inicial, pagina_medicamento, pagina_estoque, pagina_relatorio):
    page.clean()
    pagina_inicial(page, pagina_medicamento, pagina_estoque, pagina_relatorio)  # Chama a página inicial após voltar
