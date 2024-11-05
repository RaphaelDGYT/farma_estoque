import flet as ft

# Exemplo fictício de medicamentos cadastrados
medicamentos_cadastrados = {
    "123456": {"nome": "Paracetamol", "quantidade": 50},
    "654321": {"nome": "Ibuprofeno", "quantidade": 30},
    "789012": {"nome": "Amoxicilina", "quantidade": 20},
}

def buscar_medicamento(codigo):
    return medicamentos_cadastrados.get(codigo)

def pagina_estoque(page: ft.Page, pagina_inicial, pagina_medicamento, pagina_relatorio):
    page.title = "Gerenciamento de Estoque"
    page.bgcolor = "#ff3a3a"
    page.padding = 0
    page.scroll = "adaptive"

    def voltar_para_inicial(e):
        page.clean()
        pagina_inicial(page, pagina_medicamento, pagina_estoque, pagina_relatorio)

    def atualizar_estoque(e):
        codigo = campo_codigo.value
        quantidade = campo_quantidade.value
        if codigo in medicamentos_cadastrados:
            medicamentos_cadastrados[codigo]["quantidade"] = int(quantidade)
            atualizar_tabela()
        campo_codigo.value = ""
        campo_quantidade.value = ""
        page.update()

    def excluir_estoque(e):
        codigo = campo_codigo.value
        if codigo in medicamentos_cadastrados:
            del medicamentos_cadastrados[codigo]
            atualizar_tabela()
        campo_codigo.value = ""
        campo_quantidade.value = ""
        page.update()

    def atualizar_tabela():
        tabela_medicamentos.rows = [
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(codigo, color="white")),  # Texto em branco
                    ft.DataCell(ft.Text(dados["nome"], color="white")),
                    ft.DataCell(ft.Text(str(dados["quantidade"]), color="white"))
                ]
            ) for codigo, dados in medicamentos_cadastrados.items()
        ]
        tabela_medicamentos.update()

    # Borda azul com título
    titulo_pagina = ft.Text("Gerenciamento de Estoque", size=24, weight="bold", color="white")
    title_container = ft.Container(
        content=titulo_pagina,
        bgcolor="#2e3bc8",
        padding=ft.padding.all(10)
    )

    # Campos de entrada e botões
    campo_codigo = ft.TextField(label="Código do Medicamento", width=300, bgcolor="white")
    campo_quantidade = ft.TextField(label="Quantidade", width=300, bgcolor="white")
    botao_buscar = ft.ElevatedButton("Buscar Medicamento", on_click=lambda e: buscar_medicamento(campo_codigo.value), bgcolor="#2e3bc8", color="white")
    botao_alterar = ft.ElevatedButton("Alterar Estoque", on_click=atualizar_estoque, bgcolor="#2e3bc8", color="white")
    botao_excluir = ft.ElevatedButton("Excluir Estoque", on_click=excluir_estoque, bgcolor="#2e3bc8", color="white")
    botao_voltar = ft.ElevatedButton("Voltar", on_click=voltar_para_inicial, bgcolor="#2e3bc8", color="white")

    # Tabela de medicamentos em branco
    tabela_medicamentos = ft.DataTable(
        columns=[
            ft.DataColumn(label=ft.Text("Código", color="white")),  # Texto das colunas em branco
            ft.DataColumn(label=ft.Text("Nome", color="white")),
            ft.DataColumn(label=ft.Text("Quantidade", color="white"))
        ],
        rows=[],  # Inicialmente sem dados para mostrar em branco
    )

    # Contêiner da tabela
    tabela_container = ft.Container(
        content=tabela_medicamentos,
        width=400,
        alignment=ft.Alignment(-1, 0)
    )

    # Formulário com campos e botões
    formulario = ft.Column(
        controls=[
            campo_codigo,
            botao_buscar,
            ft.Text("Nome do Medicamento:", size=16, color="white"),  # Texto em branco
            campo_quantidade,
            botao_alterar,
            botao_excluir,
            botao_voltar,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=15,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # Layout principal com linha para organizar a tabela e o formulário
    layout_principal = ft.Row(
        controls=[
            tabela_container,
            formulario
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50,
    )

    # Adiciona todos os elementos na página
    page.add(title_container)
    page.add(layout_principal)

    # Atualiza a tabela ao abrir a página para preencher os dados
    atualizar_tabela()
