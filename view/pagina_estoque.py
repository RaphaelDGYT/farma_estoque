import sys
import os
import flet as ft
import mysql.connector as mysql

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import DB

def pagina_estoque(page: ft.Page, pagina_inicial, pagina_medicamento, pagina_relatorio):
    page.title = "Gerenciamento de Estoque"
    page.bgcolor = "#ff3a3a"
    page.padding = 0

    def voltar_para_inicial(e):
        page.clean()
        pagina_inicial(page, pagina_medicamento, pagina_estoque, pagina_relatorio)

    def buscar_medicamento(registro_ms):
        try:
            registro_ms = registro_ms.strip()

            banco = DB()
            cursor = banco.conexao_db()

            cursor.execute("SELECT * FROM medicamento WHERE reg_ms = %s", [registro_ms])
            resultado = cursor.fetchone()

            banco.fechar_conexao()

            if resultado:
                nome_medicamento.value = f"Medicamento encontrado: {resultado[1]}"
                medicamentos_tabela.rows.clear()
                medicamentos_tabela.rows.append(ft.DataRow(cells=[ft.DataCell(ft.Text(resultado[5])),
                                                                  ft.DataCell(ft.Text(resultado[1])),
                                                                  ft.DataCell(ft.Text(str(resultado[8])))]))
                page.update()
            else:
                nome_medicamento.value = f"Medicamento com Registro MS {registro_ms} não encontrado"
                page.update()

        except mysql.Error as e:
            print(f"Erro ao buscar medicamento: {e}")

    def carregar_todos_medicamentos():
        try:
            banco = DB()
            cursor = banco.conexao_db()
            cursor.execute("SELECT * FROM medicamento")
            resultados = cursor.fetchall()

            banco.fechar_conexao()

            medicamentos_tabela.rows.clear()
            for resultado in resultados:
                medicamentos_tabela.rows.append(ft.DataRow(cells=[ft.DataCell(ft.Text(str(resultado[5]))),
                                                                  ft.DataCell(ft.Text(resultado[1])),
                                                                  ft.DataCell(ft.Text(str(resultado[8])))]))
            page.update()
        except mysql.Error as e:
            print(f"Erro ao carregar medicamentos: {e}")

    def atualizar_estoque(e):
        reg_ms = reg_ms_field.value
        quantidade = quantidade_field.value

        if quantidade.isdigit():
            quantidade = int(quantidade)
            if atualizar_estoque_no_banco(reg_ms, quantidade):
                nome_medicamento.value = f"Estoque alterado para: {quantidade} unidades."
            else:
                nome_medicamento.value = "Erro ao alterar o estoque."
        else:
            nome_medicamento.value = "Quantidade inválida."

        reg_ms_field.value = ""
        quantidade_field.value = ""
        page.update()

    def excluir_estoque(e):
        reg_ms = reg_ms_field.value
        if excluir_medicamento(reg_ms):
            nome_medicamento.value = f"Medicamento com Registro MS {reg_ms} excluído."
        else:
            nome_medicamento.value = "Erro ao excluir medicamento."

        reg_ms_field.value = ""
        quantidade_field.value = ""
        page.update()

    def atualizar_estoque_no_banco(reg_ms, quantidade):
        try:
            banco = DB()
            cursor = banco.conexao_db()
            cursor.execute("UPDATE medicamento SET estoque = estoque + %s WHERE reg_ms = %s", (quantidade, reg_ms))
            banco.conn.commit()
            banco.fechar_conexao()
            return True
        except mysql.Error as e:
            print(f"Erro ao atualizar estoque: {e}")
            return False

    def excluir_medicamento(reg_ms):
        try:
            banco = DB()
            cursor = banco.conexao_db()
            cursor.execute("DELETE FROM medicamento WHERE reg_ms = %s", [reg_ms])
            banco.conn.commit()
            banco.fechar_conexao()
            return True
        except mysql.Error as e:
            print(f"Erro ao excluir medicamento: {e}")
            return False

    title_container = ft.Container(
        content=ft.Text("Gerenciamento de Estoque", size=24, weight="bold", color="white"),
        bgcolor="#2e3bc8",
        padding=ft.padding.all(10),
        alignment=ft.Alignment(0, 0)
    )

    reg_ms_field = ft.TextField(label="Registro MS", width=300, bgcolor="white")
    quantidade_field = ft.TextField(label="Quantidade", width=300, bgcolor="white")
    nome_medicamento = ft.Text("", size=16, color="white")

    medicamentos_tabela = ft.DataTable(
        columns=[ft.DataColumn(ft.Text("Registro MS")),
                 ft.DataColumn(ft.Text("Nome do Medicamento")),
                 ft.DataColumn(ft.Text("Quantidade"))],
        rows=[],
        bgcolor="#f0f0f0",
        width=800
    )

    buscar_button = ft.ElevatedButton("Buscar Medicamento", on_click=lambda e: buscar_medicamento(reg_ms_field.value.strip()))

    formulario = ft.Column(
        controls=[reg_ms_field,
                  buscar_button,
                  nome_medicamento,
                  quantidade_field,
                  ft.ElevatedButton("Alterar Estoque", on_click=atualizar_estoque, bgcolor="#2e3bc8", color="white"),
                  ft.ElevatedButton("Excluir Estoque", on_click=excluir_estoque, bgcolor="#2e3bc8", color="white"),
                  ft.ElevatedButton("Voltar", on_click=voltar_para_inicial, bgcolor="#2e3bc8", color="white")],
        alignment=ft.MainAxisAlignment.START,
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    content_container = ft.Container(
        content=formulario,
        alignment=ft.Alignment(0, 0),
        padding=ft.padding.all(20),
        width=300
    )

    tabela_container = ft.Container(
        content=medicamentos_tabela,
        alignment=ft.Alignment(-1, 0),  # Alinha para a extrema esquerda
        padding=ft.padding.all(0),      # Sem padding
        margin=ft.margin.only(left=0),  # Sem margem
        width=600
    )

    row_layout = ft.Row(
        controls=[tabela_container, content_container],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=30
    )

    page.add(title_container)
    page.add(row_layout)

    carregar_todos_medicamentos()
