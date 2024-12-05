import flet as ft
from pagina_login import login_page
from pagina_inicial import pagina_inicial
from pagina_medicamento import pagina_medicamento
from pagina_estoque import pagina_estoque
from pagina_relatorio import pagina_relatorio  # Importa a função de página de relatório

def main(page: ft.Page):
    # Chama a função login_page com todas as páginas necessárias
    login_page(page, pagina_inicial, pagina_medicamento, pagina_estoque, pagina_relatorio)  # Adiciona 'pagina_relatorio'

ft.app(target=main) 
