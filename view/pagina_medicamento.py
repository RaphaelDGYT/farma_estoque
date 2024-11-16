import flet as ft
import sys
import os
# Adiciona o diretório raiz (farma_estoque) ao sys.path para que o Python possa encontrar o módulo model
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import DB
from model.medicamento import cadastrar_medicamento

def pagina_medicamento(page: ft.Page, pagina_inicial, pagina_estoque, pagina_relatorio):
    page.title = "Cadastro de Medicamentos"
    page.bgcolor = "#ff3a3a"
    page.padding = 0
    page.scroll = "adaptive"

    # Função para voltar à página inicial
    def voltar_para_inicial(e):
        page.clean()
        pagina_inicial(page, pagina_medicamento, pagina_estoque, pagina_relatorio)

    # Função para cadastrar medicamento
    def cadastrar(e):
        # Obtém os valores dos campos
        descricao = nome_medicamento.value
        laboratorio = laboratorio_medicamento.value
        lista_adendo = lista_adendo_medicamento.value
        lote = lote_medicamento.value
        reg_ms = reg_ms_medicamento.value
        validade = validade_medicamento.value
        cod_barras = cod_barras_medicamento.value
        estoque = quantidade_medicamento.value

        # Chama a função de cadastro do model
        sucesso = cadastrar_medicamento(descricao, laboratorio, lista_adendo, lote, reg_ms, validade, cod_barras, estoque)

        if sucesso:
            page.add(ft.Text("Medicamento cadastrado com sucesso!", color="green"))
        else:
            page.add(ft.Text("Erro ao cadastrar medicamento", color="red"))

    # Borda azul com o título
    title_container = ft.Container(
        content=ft.Text("Cadastro de Medicamentos", size=24, weight="bold", color="white"),
        bgcolor="#2e3bc8",
        padding=ft.padding.all(10)
    )

    # Definição dos campos do formulário
    nome_medicamento = ft.TextField(label="Nome do Medicamento", width=300, bgcolor="white")
    laboratorio_medicamento = ft.TextField(label="Laboratório", width=300, bgcolor="white")
    lista_adendo_medicamento = ft.TextField(label="Lista Adendo", width=300, bgcolor="white")
    lote_medicamento = ft.TextField(label="Lote", width=300, bgcolor="white")
    reg_ms_medicamento = ft.TextField(label="Registro MS", width=300, bgcolor="white")
    validade_medicamento = ft.TextField(label="Validade", width=300, bgcolor="white")
    cod_barras_medicamento = ft.TextField(label="Código de Barras", width=300, bgcolor="white")
    quantidade_medicamento = ft.TextField(label="Quantidade", width=300, bgcolor="white")

    # Botões de ação
    botao_cadastrar = ft.ElevatedButton("Cadastrar", bgcolor="#2e3bc8", color="white", on_click=cadastrar_medicamento)
    botao_voltar = ft.ElevatedButton("Voltar", on_click=voltar_para_inicial, bgcolor="#2e3bc8", color="white")

    # Formulário de cadastro
    formulario = ft.Column(
        controls=[
            nome_medicamento,
            laboratorio_medicamento,
            lista_adendo_medicamento,
            lote_medicamento,
            reg_ms_medicamento,
            validade_medicamento,
            cod_barras_medicamento,
            quantidade_medicamento,
            botao_cadastrar,
            botao_voltar,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    # Container para centralizar o conteúdo
    content_container = ft.Container(
        content=formulario,
        alignment=ft.Alignment(0, 0),
        padding=ft.padding.all(20)
    )

    # Adicionando a borda e o conteúdo
    page.add(title_container)  # Adiciona o título
    page.add(content_container)  # Adiciona o formulário
