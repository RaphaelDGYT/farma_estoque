import sys
import os
import flet as ft
import mysql.connector as mysql
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.relatorio import Relatorio
from model.estoque_filtro import Estoque
from controler.remove_model import retirar_medicamento, deletar_medicamento

def pagina_estoque(page: ft.Page, pagina_inicial, pagina_medicamento, pagina_relatorio):
    page.title = "Gerenciamento de Estoque"
    page.bgcolor = "#ff3a3a"
    page.padding = 0

    def voltar_para_inicial(e):
        page.clean()
        pagina_inicial(page, pagina_medicamento, pagina_estoque, pagina_relatorio)
        
    def buscar_medicamento_por_codigo(id):
        if not id.isdigit():
            nome_medicamento.value = "Informe um valor válido."
            page.update()
            return
        try:
            resultado = Relatorio().relatorio_filtrado("Código Produto", id)
            if resultado:
                nome_medicamento.value = f"Medicamento encontrado: {resultado[1]}"
                medicamentos_tabela.rows.clear()
                medicamentos_tabela.rows.append(ft.DataRow(cells=[  # Preenche as linhas da tabela
                    criar_celula_conteudo(resultado[0]),
                    criar_celula_conteudo(resultado[1]),
                    criar_celula_conteudo(resultado[2]),
                    criar_celula_conteudo(resultado[3]),
                    criar_celula_conteudo(resultado[4]),
                    criar_celula_conteudo(resultado[5]),
                    criar_celula_conteudo(resultado[6]),
                    criar_celula_conteudo(resultado[8]),
                ]))
            else:
                nome_medicamento.value = "Medicamento não encontrado."
        except mysql.Error as e:
            nome_medicamento.value = f"Erro ao buscar medicamento: {e}"
        page.update()

    def carregar_todos_medicamentos():
        try:
            resultados = Relatorio().relatorio()
            medicamentos_tabela.rows.clear()
            for resultado in resultados:
                medicamentos_tabela.rows.append(ft.DataRow(cells=[  # Preenche as linhas da tabela
                    criar_celula_conteudo(resultado[0]),
                    criar_celula_conteudo(resultado[1]),
                    criar_celula_conteudo(resultado[2]),
                    criar_celula_conteudo(resultado[3]),
                    criar_celula_conteudo(resultado[4]),
                    criar_celula_conteudo(resultado[5]),
                    criar_celula_conteudo(resultado[6]),
                    criar_celula_conteudo(resultado[8]),
                ]))
        except:
            nome_medicamento.value = f"Erro ao carregar medicamento!"
        page.update()

    def alterar_estoque(id, quantidade, excluir=False):
        try:
            if excluir:
                deletar_medicamento(id=id)
            else:
                retirar_medicamento(id=id, quantidade=quantidade)
            return True
        except:
            nome_medicamento.value = f"Erro ao alterar estoque!"
            page.update()
            return False

    def atualizar_estoque(e):
        id = pesquisa_field.value.strip()
        quantidade = quantidade_field.value.strip()
        if not quantidade.isdigit():
            nome_medicamento.value = "Quantidade inválida."
            page.update()
            return
        if alterar_estoque(id, int(quantidade)):
            nome_medicamento.value = f"Estoque atualizado: +{quantidade} unidades."
        pesquisa_field.value = ""
        quantidade_field.value = ""
        carregar_todos_medicamentos()

    def excluir_estoque(e):
        id = pesquisa_field.value.strip()
        if alterar_estoque(id, 0, excluir=True):
            nome_medicamento.value = f"Medicamento com Código de Barras {id} excluído."
        pesquisa_field.value = ""
        carregar_todos_medicamentos()


    def criar_celula_conteudo(conteudo):
        return ft.DataCell(ft.Text(str(conteudo), size=12))  

    pesquisa_field = ft.TextField(label="Código Produto", width=300, bgcolor="white")
    quantidade_field = ft.TextField(label="Quantidade", width=300, bgcolor="white")
    nome_medicamento = ft.Text("", size=16, color="white")

    medicamentos_tabela = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Código Produto", size=14)),
            ft.DataColumn(ft.Text("Descrição", size=14)),
            ft.DataColumn(ft.Text("Laboratório", size=14)),
            ft.DataColumn(ft.Text("Lista Adendo", size=14)),
            ft.DataColumn(ft.Text("Lote", size=14)),
            ft.DataColumn(ft.Text("Registro MS", size=14)),
            ft.DataColumn(ft.Text("Validade", size=14)),
            ft.DataColumn(ft.Text("Estoque", size=14)),
        ],
        rows=[],
        bgcolor="#f0f0f0",
        width=900,  
        column_spacing=10,  
    )

    formulario = ft.Column(
        controls=[
            pesquisa_field,
            nome_medicamento,
            quantidade_field,
            ft.ElevatedButton("Adicionar", on_click=atualizar_estoque),
            ft.ElevatedButton("Excluir", on_click=excluir_estoque),
            ft.ElevatedButton("Retirar", on_click=atualizar_estoque),
            ft.ElevatedButton("Buscar", on_click=buscar_medicamento_por_codigo(pesquisa_field.value)),
            ft.ElevatedButton("Voltar", on_click=voltar_para_inicial)
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=10
    )

    page.add(
        ft.Container(
            content=ft.Row(
                controls=[medicamentos_tabela, formulario],
                alignment=ft.MainAxisAlignment.START,
                spacing=20,
            ),
            padding=10,
            width=page.width,
            height=page.height
        )
    )

    carregar_todos_medicamentos()
