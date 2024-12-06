import sys
import os
import flet as ft
import mysql.connector as mysql

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importando a classe RelatorioExcel do controller
from controler.download_planilha import RelatorioExcel as excel
from model.relatorio import Relatorio

def pagina_relatorio(page: ft.Page, pagina_inicial, pagina_medicamento, pagina_estoque):
    page.title = "Relatório - Controle de Medicamentos"
    page.bgcolor = "#ff3a3a"
    page.padding = 0

    def voltar_para_inicial(e):
        page.clean()
        pagina_inicial(page, pagina_medicamento, pagina_estoque, pagina_relatorio)

    def criar_celula_conteudo(conteudo):
        return ft.DataCell(ft.Text(str(conteudo), size=12))
    
    def carregar_todos_medicamentos():
        try:
            resultados = Relatorio.relatorio()
            medicamentos_tabela.rows.clear()
            for resultado in resultados:
                medicamentos_tabela.rows.append(ft.DataRow(cells=[
                    criar_celula_conteudo(resultado[1]),
                    criar_celula_conteudo(resultado[2]),
                    criar_celula_conteudo(resultado[3]),
                    criar_celula_conteudo(resultado[4]),
                    criar_celula_conteudo(resultado[5]),
                    criar_celula_conteudo(resultado[6]),
                    criar_celula_conteudo(resultado[7]),
                    criar_celula_conteudo(resultado[8]),
                ]))
                
        except:
            status_mensagem.content.value = f"Erro ao carregar medicamentos!"
        page.update()

    # Função para exportar o relatório
    def exportar_relatorio(e):
        try:
            relatorio = excel()
            sucesso = relatorio.salvar_planilha()
            if sucesso:
                status_mensagem.content.value = "Excel exportado com sucesso!"
                status_mensagem.bgcolor = "#28a745"
            else:
                status_mensagem.content.value = "Erro ao exportar para Excel."
                status_mensagem.bgcolor = "#dc3545"
        except Exception as erro:
            status_mensagem.content.value = f"Erro: {erro}"
            status_mensagem.bgcolor = "#dc3545"
        status_mensagem.visible = True
        page.update()

    # Mensagem de status do relatório
    status_mensagem = ft.Container(
        content=ft.Text("", size=16, color="white"),
        bgcolor="transparent",
        padding=10,
        width=400,
        border_radius=5,
        visible=False
    )

    # Botões de controle
    voltar_button = ft.ElevatedButton("Voltar", on_click=voltar_para_inicial, bgcolor="#2e3bc8", color="white")
    exportar_button = ft.ElevatedButton("Exportar para Excel", on_click=exportar_relatorio, bgcolor="#2e3bc8", color="white")

    botoes_row = ft.Row(
        controls=[voltar_button, exportar_button],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    # Tabela para exibir os medicamentos com largura ajustada
    medicamentos_tabela = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Nome")),
            ft.DataColumn(ft.Text("Laboratorio")),
            ft.DataColumn(ft.Text("Lista Adendo")),
            ft.DataColumn(ft.Text("Lote")),
            ft.DataColumn(ft.Text("Registro MS")),
            ft.DataColumn(ft.Text("Validade")),
            ft.DataColumn(ft.Text("Codigo de Barras")),
            ft.DataColumn(ft.Text("Estoque")),
        ],
        rows=[],
        bgcolor="#f0f0f0",
        width=1200
        # Aumentando a largura para 1200
    )

    # Layout principal
    layout_principal = ft.Column(
        controls=[
            ft.Text("Relatório - Controle de Medicamentos", size=24, weight="bold", color="white"),
            botoes_row,
            medicamentos_tabela,
            status_mensagem
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20
    )
    carregar_todos_medicamentos()
    page.add(layout_principal)
    
