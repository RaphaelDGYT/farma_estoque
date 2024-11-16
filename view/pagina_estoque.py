import sys
import os
import flet as ft
import mysql.connector as mysql

# Ajusta o caminho para o config.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import DB

def pagina_estoque(page: ft.Page, pagina_inicial, pagina_medicamento, pagina_relatorio):
    page.title = "Gerenciamento de Estoque"
    page.bgcolor = "#ff3a3a"
    page.padding = 0

    # Função para voltar para a página inicial
    def voltar_para_inicial(e):
        page.clean()
        pagina_inicial(page, pagina_medicamento, pagina_estoque, pagina_relatorio)

    # Função para buscar medicamento no banco de dados pelo "Registro MS"
    def buscar_medicamento(registro_ms):
        try:
            # Remove espaços extras no registro MS inserido
            registro_ms = registro_ms.strip()

            # Conectar ao banco de dados
            banco = DB()
            cursor = banco.conexao_db()

            # Garantir que a pesquisa seja feita corretamente no campo reg_ms
            cursor.execute("SELECT * FROM medicamento WHERE reg_ms = %s", [registro_ms])
            resultado = cursor.fetchone()  # Pega o primeiro resultado

            banco.fechar_conexao()

            if resultado:
                nome_medicamento.value = f"Medicamento encontrado: {resultado[1]}"  # Nome do medicamento
                # Atualizar a tabela de medicamentos
                medicamentos_tabela.rows.clear()  # Limpar a tabela
                medicamentos_tabela.rows.append(ft.DataRow(cells=[ft.DataCell(ft.Text(resultado[5])),  # Registro MS
                                                                  ft.DataCell(ft.Text(resultado[1])),  # Nome do medicamento
                                                                  ft.DataCell(ft.Text(str(resultado[8])))]))  # Quantidade
                page.update()
            else:
                nome_medicamento.value = f"Medicamento com Registro MS {registro_ms} não encontrado"
                page.update()

        except mysql.Error as e:
            print(f"Erro ao buscar medicamento: {e}")

    # Função para carregar todos os medicamentos no banco de dados
    def carregar_todos_medicamentos():
        try:
            banco = DB()
            cursor = banco.conexao_db()
            cursor.execute("SELECT * FROM medicamento")  # Pega todos os medicamentos
            resultados = cursor.fetchall()  # Pega todos os resultados

            banco.fechar_conexao()

            medicamentos_tabela.rows.clear()  # Limpa a tabela
            for resultado in resultados:
                medicamentos_tabela.rows.append(ft.DataRow(cells=[ft.DataCell(ft.Text(str(resultado[5]))),  # Registro MS
                                                                  ft.DataCell(ft.Text(resultado[1])),  # Nome do medicamento
                                                                  ft.DataCell(ft.Text(str(resultado[8])))]))  # Quantidade
            page.update()
        except mysql.Error as e:
            print(f"Erro ao carregar medicamentos: {e}")

    # Função para atualizar o estoque no banco de dados
    def atualizar_estoque(e):
        reg_ms = reg_ms_field.value
        quantidade = quantidade_field.value

        # Atualizar estoque no banco de dados (chamar função de atualização)
        if atualizar_estoque_no_banco(reg_ms, quantidade):
            print(f"Estoque alterado: Registro MS: {reg_ms}, Nova quantidade: {quantidade}")
        else:
            print(f"Erro ao alterar estoque do medicamento com Registro MS: {reg_ms}")

        # Reiniciar campos
        reg_ms_field.value = ""
        quantidade_field.value = ""
        page.update()

    # Função para excluir o medicamento do estoque
    def excluir_estoque(e):
        reg_ms = reg_ms_field.value
        if excluir_medicamento(reg_ms):
            print(f"Medicamento com Registro MS {reg_ms} excluído")
        else:
            print(f"Erro ao excluir medicamento com Registro MS: {reg_ms}")
        
        # Reiniciar campo
        reg_ms_field.value = ""
        quantidade_field.value = ""
        page.update()

    # Função para atualizar o estoque no banco de dados
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

    # Função para excluir o medicamento do banco de dados
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

    # Borda azul com o título
    title_container = ft.Container(
        content=ft.Text("Gerenciamento de Estoque", size=24, weight="bold", color="white"),
        bgcolor="#2e3bc8",
        padding=ft.padding.all(10)
    )

    # Campos para registro MS e quantidade
    reg_ms_field = ft.TextField(label="Registro MS", width=300, bgcolor="white")
    quantidade_field = ft.TextField(label="Quantidade", width=300, bgcolor="white")

    # Campo para mostrar o nome do medicamento
    nome_medicamento = ft.Text("", size=16, color="black")

    # Tabela com medicamentos cadastrados
    medicamentos_tabela = ft.DataTable(
        columns=[ft.DataColumn(ft.Text("Registro MS")),
                 ft.DataColumn(ft.Text("Nome do Medicamento")),
                 ft.DataColumn(ft.Text("Quantidade"))],
        rows=[],  # Inicialmente sem dados
        bgcolor="#f0f0f0",
    )

    # Botão para buscar o medicamento
    buscar_button = ft.ElevatedButton("Buscar Medicamento", on_click=lambda e: buscar_medicamento(reg_ms_field.value.strip()))

    # Formulário de gerenciamento de estoque
    formulario = ft.Column(
        controls=[reg_ms_field,
                  buscar_button,
                  nome_medicamento,
                  quantidade_field,
                  ft.ElevatedButton("Alterar Estoque", on_click=atualizar_estoque, bgcolor="#2e3bc8", color="white"),
                  ft.ElevatedButton("Excluir Estoque", on_click=excluir_estoque, bgcolor="#2e3bc8", color="white"),
                  ft.ElevatedButton("Voltar", on_click=voltar_para_inicial, bgcolor="#2e3bc8", color="white")],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    # Container para centralizar o formulário na página
    content_container = ft.Container(
        content=formulario,
        alignment=ft.Alignment(0, 0),
        padding=ft.padding.all(20),
        width=300
    )

    # Container para exibir a tabela de medicamentos ao lado
    tabela_container = ft.Container(
        content=medicamentos_tabela,
        alignment=ft.Alignment(0, 0),
        padding=ft.padding.all(20),
        width=500
    )

    # Organizando os containers lado a lado
    row_layout = ft.Row(
        controls=[tabela_container, content_container],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    # Adicionando o título e o layout do formulário e tabela
    page.add(title_container)
    page.add(row_layout)

    # Carregar todos os medicamentos ao iniciar
    carregar_todos_medicamentos()
