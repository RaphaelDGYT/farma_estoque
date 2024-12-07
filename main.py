import flet as ft
from view.pagina_login import login_page
from view.pagina_inicial import pagina_inicial
from view.pagina_medicamento import pagina_medicamento
from view.pagina_estoque import pagina_estoque
from view.pagina_relatorio import pagina_relatorio  # Importa a função de página de relatório

def main(page: ft.Page):
    # Chama a função login_page com todas as páginas necessárias
    login_page(page, pagina_inicial, pagina_medicamento, pagina_estoque, pagina_relatorio)  # Adiciona 'pagina_relatorio'

ft.app(target=main) 
