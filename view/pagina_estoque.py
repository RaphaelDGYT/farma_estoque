import flet as ft

<<<<<<< HEAD
# Suponha que você tenha uma função que busca o medicamento pelo código
def buscar_medicamento(codigo):
    # Exemplo fictício de medicamentos cadastrados
    medicamentos = {
        "123456": {"nome": "Paracetamol", "quantidade": 50},
        "654321": {"nome": "Ibuprofeno", "quantidade": 30}
    }
    return medicamentos.get(codigo)
=======
# Exemplo fictício de medicamentos cadastrados
medicamentos_cadastrados = {
    "123456": {"nome": "Paracetamol", "quantidade": 50},
    "654321": {"nome": "Ibuprofeno", "quantidade": 30},
    "789012": {"nome": "Amoxicilina", "quantidade": 20},
}

def buscar_medicamento(codigo):
    return medicamentos_cadastrados.get(codigo)
>>>>>>> task-atualizacao-interface

def pagina_estoque(page: ft.Page, pagina_inicial, pagina_medicamento, pagina_relatorio):
    page.title = "Gerenciamento de Estoque"
    page.bgcolor = "#ff3a3a"
    page.padding = 0
    page.scroll = "adaptive"

<<<<<<< HEAD
    # Função para voltar para a página inicial
=======
>>>>>>> task-atualizacao-interface
    def voltar_para_inicial(e):
        page.clean()
        pagina_inicial(page, pagina_medicamento, pagina_estoque, pagina_relatorio)

<<<<<<< HEAD
    # Função para atualizar os dados do medicamento
    def atualizar_estoque(e):
        codigo = codigo_field.value
        quantidade = quantidade_field.value

        # Aqui você implementa a lógica para atualizar o estoque no banco de dados ou lista
        print(f"Estoque alterado: Código: {codigo}, Nova quantidade: {quantidade}")
        # Reiniciar campos
        codigo_field.value = ""
        quantidade_field.value = ""
        page.update()

    # Função para excluir o medicamento
    def excluir_estoque(e):
        codigo = codigo_field.value
        # Aqui você implementa a lógica para excluir o medicamento do banco de dados ou lista
        print(f"Medicamento com código {codigo} excluído")
        # Reiniciar campo
        codigo_field.value = ""
        quantidade_field.value = ""
        page.update()

    # Borda azul com o título
    title_container = ft.Container(
        content=ft.Text("Gerenciamento de Estoque", size=24, weight="bold", color="white"),
=======
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
>>>>>>> task-atualizacao-interface
        bgcolor="#2e3bc8",
        padding=ft.padding.all(10)
    )

<<<<<<< HEAD
    # Campos para código do medicamento e quantidade
    codigo_field = ft.TextField(label="Código do Medicamento", width=300, bgcolor="white")
    quantidade_field = ft.TextField(label="Quantidade", width=300, bgcolor="white")

    # Botão para buscar o medicamento
    buscar_button = ft.ElevatedButton("Buscar Medicamento", on_click=lambda e: buscar_medicamento(codigo_field.value))

    # Formulário de gerenciamento de estoque
    formulario = ft.Column(
        controls=[
            codigo_field,
            buscar_button,
            ft.Text("Nome do Medicamento: ", size=16, color="black"),  # Aqui você pode adicionar o nome do medicamento
            quantidade_field,
            ft.ElevatedButton("Alterar Estoque", on_click=atualizar_estoque, bgcolor="#2e3bc8", color="white"),
            ft.ElevatedButton("Excluir Estoque", on_click=excluir_estoque, bgcolor="#2e3bc8", color="white"),
            ft.ElevatedButton("Voltar", on_click=voltar_para_inicial, bgcolor="#2e3bc8", color="white"),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    # Container para centralizar o formulário na página
    content_container = ft.Container(
        content=formulario,
        alignment=ft.Alignment(0, 0),
        padding=ft.padding.all(20)
    )

    # Adicionando a borda e o conteúdo
    page.add(title_container)
    page.add(content_container)
=======
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
>>>>>>> task-atualizacao-interface
