import os
import sys  
import pandas as pd
import datetime as datetime
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from config import DB
from .relatorio import Relatorio
from relatorio import Relatorio
from controler.utils_model import converter_df


class Estoque(Relatorio):
    def __init__(self):
        super().__init__()

    def estoque_intervalo(self, ini, fim):
        tabela = super().relatorio()
        tabela_filtrada = tabela[(tabela["Estoque"] >= ini) & (tabela["Estoque"] <= fim)]
        if tabela_filtrada.empty:
            return print("Nenhum medicamento encontrado!")
        else:
            return converter_df(tabela_filtrada)
        
    def estoque_menor_que(self, quantidade):
        tabela = super().relatorio()
        tabela_filtrada = tabela[tabela["Estoque"] < quantidade]
        if tabela_filtrada.empty:
            return print("Medicamento não encontrado!")
        else:
            return converter_df(tabela_filtrada)

    def estoque_maior_que(self, quantidade):
        tabela = super().relatorio()
        tabela_filtrada = tabela[tabela["Estoque"] > quantidade]
        if tabela_filtrada.empty:
            return print("Medicamento não encontrado!")
        else:
            return converter_df(tabela_filtrada)
        
    def estoque_igual(self, quantidade):
        tabela = super().relatorio()
        tabela_filtrada = tabela[tabela["Estoque"] == quantidade]
        if tabela_filtrada.empty:
            return print("Medicamento não encontrado!")
        else:
            return converter_df(tabela_filtrada)