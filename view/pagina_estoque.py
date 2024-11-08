import flet as ft

# Suponha que você tenha uma função que busca o medicamento pelo código
def buscar_medicamento(codigo):
    # Exemplo fictício de medicamentos cadastrados
    medicamentos = {
        "123456": {"nome": "Paracetamol", "quantidade": 50},
        "654321": {"nome": "Ibuprofeno", "quantidade": 30}
    }
    return medicamentos.get(codigo)

def pagina_estoque(page: ft.Page, pagina_inicial, pagina_medicamento, pagina_relatorio):
    page.title = "Gerenciamento de Estoque"
    page.bgcolor = "#ff3a3a"
    page.padding = 0

    # Função para voltar para a página inicial
    def voltar_para_inicial(e):
        page.clean()
        pagina_inicial(page, pagina_medicamento, pagina_estoque, pagina_relatorio)

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
        bgcolor="#2e3bc8",
        padding=ft.padding.all(10)
    )

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
