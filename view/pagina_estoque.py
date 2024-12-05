import sys
import os
import flet as ft
import mysql.connector as mysql
from model.estoque_filtro import Estoque
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import DB

def pagina_estoque(page: ft.Page, pagina_inicial, pagina_medicamento, pagina_relatorio):
    page.title = "Gerenciamento de Estoque"
    page.bgcolor = "#ff3a3a"
    page.padding = 0

    def voltar_para_inicial(e):
        page.clean()
        pagina_inicial(page, pagina_medicamento, pagina_estoque, pagina_relatorio)
        
    def buscar_medicamento_por_codigo(id):
        if not id.isdigit():
            nome_medicamento.value = "Informe Código de Barras válido."
            page.update()
            return
        try:
            banco = DB()
            cursor = banco.conexao_db()
            cursor.execute("SELECT * FROM medicamento WHERE cod_barras = %s", [id])
            resultado = cursor.fetchone()
            banco.fechar_conexao()
            if resultado:
                nome_medicamento.value = f"Medicamento encontrado: {resultado[1]}"
                medicamentos_tabela.rows.clear()
                medicamentos_tabela.rows.append(ft.DataRow(cells=[  # Preenche as linhas da tabela
                    criar_celula_conteudo(resultado[1]),
                    criar_celula_conteudo(resultado[2]),
                    criar_celula_conteudo(resultado[3]),
                    criar_celula_conteudo(resultado[4]),
                    criar_celula_conteudo(resultado[5]),
                    criar_celula_conteudo(resultado[6]),
                    criar_celula_conteudo(resultado[7]),
                    criar_celula_conteudo(resultado[8]),
                ]))
            else:
                nome_medicamento.value = "Medicamento não encontrado."
        except mysql.Error as e:
            nome_medicamento.value = f"Erro ao buscar medicamento: {e}"
        page.update()

    def carregar_todos_medicamentos():
        try:
            banco = DB()
            cursor = banco.conexao_db()
            cursor.execute("SELECT * FROM medicamento")
            resultados = cursor.fetchall()
            banco.fechar_conexao()
            medicamentos_tabela.rows.clear()
            for resultado in resultados:
                medicamentos_tabela.rows.append(ft.DataRow(cells=[  # Preenche as linhas da tabela
                    criar_celula_conteudo(resultado[1]),
                    criar_celula_conteudo(resultado[2]),
                    criar_celula_conteudo(resultado[3]),
                    criar_celula_conteudo(resultado[4]),
                    criar_celula_conteudo(resultado[5]),
                    criar_celula_conteudo(resultado[6]),
                    criar_celula_conteudo(resultado[7]),
                    criar_celula_conteudo(resultado[8]),
                ]))
        except mysql.Error as e:
            nome_medicamento.value = f"Erro ao carregar medicamentos: {e}"
        page.update()

    def alterar_estoque(id, quantidade, excluir=False):
        try:
            banco = DB()
            cursor = banco.conexao_db()
            if excluir:
                cursor.execute("DELETE FROM medicamento WHERE cod_barras = %s", [id])
            else:
                cursor.execute(
                    "UPDATE medicamento SET estoque = estoque + %s WHERE cod_barras = %s",
                    (quantidade, id)
                )
            banco.conn.commit()
            banco.fechar_conexao()
            return True
        except mysql.Error as e:
            nome_medicamento.value = f"Erro ao alterar estoque: {e}"
            page.update()
            return False

    def atualizar_estoque(e):
        cod_barras = pesquisa_field.value.strip()
        quantidade = quantidade_field.value.strip()
        if not quantidade.isdigit():
            nome_medicamento.value = "Quantidade inválida."
            page.update()
            return
        if alterar_estoque(cod_barras, int(quantidade)):
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

    def aplicar_filtro(e):
        if not pesquisa_field.value.isdigit():
            nome_medicamento.value = "Filtro não aplicado."
            page.update()
            return

        estoque = Estoque()
        filtro_selecionado = None
        for radio in formulario.controls[0].controls:
            if radio.value == "Maior quantidade de estoque" and radio.checked:
                filtro_selecionado = "maior"
            elif radio.value == "Menor quantidade de estoque" and radio.checked:
                filtro_selecionado = "menor"
            elif radio.value == "Mesma quantidade de estoque" and radio.checked:
                filtro_selecionado = "igual"

        if filtro_selecionado is None:
            nome_medicamento.value = "Selecione um filtro."
            page.update()
            return

        try:
            if filtro_selecionado == "maior":
                tabela_filtrada = estoque.estoque_maior_que(int(quantidade_field.value.strip()))
            elif filtro_selecionado == "menor":
                tabela_filtrada = estoque.estoque_menor_que(int(quantidade_field.value.strip()))
            elif filtro_selecionado == "igual":
                tabela_filtrada = estoque.estoque_igual(int(quantidade_field.value.strip()))

            medicamentos_tabela.rows.clear()
            if isinstance(tabela_filtrada, pd.DataFrame) and not tabela_filtrada.empty:
                for _, resultado in tabela_filtrada.iterrows():
                    medicamentos_tabela.rows.append(ft.DataRow(cells=[  # Preenche as linhas da tabela
                        criar_celula_conteudo(resultado['Nome']),
                        criar_celula_conteudo(resultado['Laboratório']),
                        criar_celula_conteudo(resultado['Lista Adendo']),
                        criar_celula_conteudo(resultado['Lote']),
                        criar_celula_conteudo(resultado['Registro MS']),
                        criar_celula_conteudo(resultado['Validade']),
                        criar_celula_conteudo(resultado['Código de Barras']),
                        criar_celula_conteudo(resultado['Estoque']),
                    ]))
            else:
                nome_medicamento.value = "Nenhum medicamento encontrado com os critérios selecionados."

            page.update()

        except Exception as e:
            nome_medicamento.value = f"Erro ao aplicar filtro: {e}"
            page.update()

    def criar_celula_conteudo(conteudo):
        return ft.DataCell(ft.Text(str(conteudo), size=12))  

    pesquisa_field = ft.TextField(label="Código de Barras", width=300, bgcolor="white")
    quantidade_field = ft.TextField(label="Quantidade", width=300, bgcolor="white")
    nome_medicamento = ft.Text("", size=16, color="white")

    medicamentos_tabela = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Nome", size=14)),
            ft.DataColumn(ft.Text("Laboratório", size=14)),
            ft.DataColumn(ft.Text("Lista Adendo", size=14)),
            ft.DataColumn(ft.Text("Lote", size=14)),
            ft.DataColumn(ft.Text("Registro MS", size=14)),
            ft.DataColumn(ft.Text("Validade", size=14)),
            ft.DataColumn(ft.Text("Código de Barras", size=14)),
            ft.DataColumn(ft.Text("Estoque", size=14)),
        ],
        rows=[],
        bgcolor="#f0f0f0",
        width=900,  
        column_spacing=10,  
    )

    formulario = ft.Column(
        controls=[
            ft.Text("Selecione uma Opção de filtragem:"),
            ft.RadioGroup(content=ft.Column([  # Corrigido: Agrupamento de filtros
                ft.Radio(value="Maior quantidade de estoque", label="Maior quantidade de estoque"),
                ft.Radio(value="Menor quantidade de estoque", label="Menor quantidade de estoque"),
                ft.Radio(value="Mesma quantidade de estoque", label="Mesma quantidade de estoque")
            ]), on_change=lambda e: nome_medicamento.update(f"O filtro escolhido é {e.control.value}")),
            pesquisa_field,
            ft.Row([
                ft.ElevatedButton("Buscar", on_click=lambda e: buscar_medicamento_por_codigo(pesquisa_field.value.strip())),
                ft.ElevatedButton("Filtrar", on_click=aplicar_filtro),
                ft.ElevatedButton("Voltar", on_click=voltar_para_inicial)
            ]),
            nome_medicamento,
            quantidade_field,
            ft.ElevatedButton("Adicionar Estoque", on_click=atualizar_estoque),
            ft.ElevatedButton("Excluir Estoque", on_click=excluir_estoque),
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
