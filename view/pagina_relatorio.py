import flet as ft
from config import DB  # Importando a classe DB corretamente

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

    # Função para carregar os medicamentos para o relatório
    def carregar_medicamentos_relatorio():
        try:
            banco = DB()  # Instanciando a classe DB corretamente
            cursor = banco.conexao_db()
            cursor.execute("SELECT * FROM medicamento")  # Carrega todos os medicamentos
            resultados = cursor.fetchall()

            banco.fechar_conexao()

            # Limpa as linhas da tabela de medicamentos
            tabela.rows.clear()
            for resultado in resultados:
                # Preenche a tabela com os dados dos medicamentos
                tabela.rows.append(ft.DataRow(cells=[
                    ft.DataCell(ft.Text(str(resultado[5]), color="white")),  # Código de barras
                    ft.DataCell(ft.Text(resultado[1], color="white")),       # Nome do Medicamento
                    ft.DataCell(ft.Text(resultado[2], color="white")),       # Classe Terapêutica
                    ft.DataCell(ft.Text(resultado[3], color="white")),       # Lote
                    ft.DataCell(ft.Text(resultado[4], color="white")),       # Validade
                    ft.DataCell(ft.Text(str(resultado[8]), color="white")),  # Quantidade
                ]))

            page.update()  # Atualiza a página para refletir as mudanças na tabela

        except mysql.Error as e:
            print(f"Erro ao carregar medicamentos para o relatório: {e}")

    # Tabela para mostrar os medicamentos
    tabela = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Código de Barras", color="white")),
            ft.DataColumn(ft.Text("Nome do Medicamento", color="white")),
            ft.DataColumn(ft.Text("Classe Terapêutica", color="white")),
            ft.DataColumn(ft.Text("Lote", color="white")),
            ft.DataColumn(ft.Text("Validade", color="white")),
            ft.DataColumn(ft.Text("Quantidade", color="white")),
        ],
        rows=[],  # Inicialmente sem dados
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

    # Carregar medicamentos no relatório ao iniciar
    carregar_medicamentos_relatorio()

def exportar_pdf(page):
    print("Exportando PDF...")

def exportar_csv(page):
    print("Exportando CSV...")

def voltar(page, pagina_inicial, pagina_medicamento, pagina_estoque, pagina_relatorio):
    page.clean()
    pagina_inicial(page, pagina_medicamento, pagina_estoque, pagina_relatorio)  # Chama a página inicial após voltar
