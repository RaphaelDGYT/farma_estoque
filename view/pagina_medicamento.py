import flet as ft
import sys
import os
from datetime import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.medicamento import cadastrar_medicamento

def pagina_medicamento(page: ft.Page, pagina_inicial, pagina_estoque, pagina_relatorio):
    page.title = "Cadastro de Medicamentos"
    page.bgcolor = "#ff3a3a"
    page.padding = 0
    page.scroll = "adaptive"

    def voltar_para_inicial(e):
        page.clean()
        pagina_inicial(page, pagina_medicamento, pagina_estoque, pagina_relatorio)

    def cadastrar(e):
        # Obtém os valores do formulário
        descricao = nome_medicamento.value
        laboratorio = laboratorio_medicamento.value
        lista_adendo = lista_adendo_medicamento.value
        lote = lote_medicamento.value
        reg_ms = reg_ms_medicamento.value
        validade = validade_medicamento.value
        cod_barras = cod_barras_medicamento.value
        estoque = quantidade_medicamento.value or 1  # Define 1 como valor padrão se vazio

        # Valida o tamanho do código de barras
        if len(cod_barras) > 20:  # Substitua '20' pelo limite definido no banco de dados
            mensagem.text = "Erro: O código de barras não pode exceder 20 caracteres."
            mensagem.color = "red"
            page.update()
            return

        # Valida a data de validade no formato DD/MM/YYYY
        try:
            validade = datetime.strptime(validade, "%d/%m/%Y")  # Aceita DD/MM/YYYY
        except ValueError:
            mensagem.text = "Erro: Data de validade deve estar no formato DD/MM/YYYY."
            mensagem.color = "red"
            page.update()
            return

        # Tenta cadastrar
        try:
            # Chama a função de cadastro
            sucesso = cadastrar_medicamento(descricao, laboratorio, lista_adendo, lote, reg_ms, validade, cod_barras, estoque)
            if sucesso:
                # Exibir apenas a mensagem de sucesso
                mensagem.text = "Medicamento cadastrado com sucesso!"
                mensagem.color = "green"
                page.update()  # Atualiza a página para exibir a mensagem de sucesso
                
                # Limpar os campos do formulário após o cadastro
                nome_medicamento.value = ""
                laboratorio_medicamento.value = ""
                lista_adendo_medicamento.value = ""
                lote_medicamento.value = ""
                reg_ms_medicamento.value = ""
                validade_medicamento.value = ""
                cod_barras_medicamento.value = ""
                quantidade_medicamento.value = ""
                page.update()  # Atualiza a página novamente após limpar os campos
            else:
                # Caso o cadastro falhe
                mensagem.Text = "Erro ao cadastrar medicamento."
                mensagem.color = "red"
                page.update()
        except Exception as ex:
            # Atualizar a mensagem de erro com a exceção
            mensagem.text = f"Erro ao cadastrar medicamento: {str(ex)}"
            mensagem.color = "red"
            page.update()  # Atualiza a página para exibir a mensagem de erro

    # Mensagem de feedback
    mensagem = ft.Text("", size=14, weight="bold", color="black")

    # Campos do formulário
    nome_medicamento = ft.TextField(label="Nome do Medicamento", width=300, bgcolor="white")
    laboratorio_medicamento = ft.TextField(label="Laboratório", width=300, bgcolor="white")
    lista_adendo_medicamento = ft.TextField(label="Lista Adendo", width=300, bgcolor="white")
    lote_medicamento = ft.TextField(label="Lote", width=300, bgcolor="white")
    reg_ms_medicamento = ft.TextField(label="Registro MS", width=300, bgcolor="white")
    validade_medicamento = ft.TextField(label="Validade (DD/MM/YYYY)", width=300, bgcolor="white")
    cod_barras_medicamento = ft.TextField(label="Código de Barras", width=300, bgcolor="white")
    quantidade_medicamento = ft.TextField(label="Quantidade", width=300, bgcolor="white")

    # Botões
    botao_cadastrar = ft.ElevatedButton("Cadastrar", bgcolor="#2e3bc8", color="white", on_click=cadastrar)
    botao_voltar = ft.ElevatedButton("Voltar", on_click=voltar_para_inicial, bgcolor="#2e3bc8", color="white")

    # Layout
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
            mensagem,  # Mensagem já está no layout inicial
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )

    content_container = ft.Container(
        content=formulario,
        alignment=ft.Alignment(0, 0),
        padding=ft.padding.all(20)
    )

    title_container = ft.Container(
        content=ft.Text("Cadastro de Medicamentos", size=24, weight="bold", color="white"),
        bgcolor="#2e3bc8",
        padding=ft.padding.all(10)
    )

    page.add(title_container, content_container)
    page.update()  # Garante que a página seja atualizada logo após a adição do conteúdo
