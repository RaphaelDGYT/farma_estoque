import os
import sys  
import pandas as pd
import datetime as datetime
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from config import DB
from controler.utils_model import tratamento_data, converter_df

class Relatorio():
    def __init__(self):
        self.banco = DB()
        self.cursor = self.banco.conexao_db()
        self.cursor.execute("SELECT * FROM medicamento")
        self.df = pd.DataFrame(self.cursor.fetchall())
        self.df.columns = ["Código Produto", "Descrição Produto", "Laboratório", "Lista/Adendo", "Lote", "Registro MS", "Validade", "Código de barras", "Estoque"]
        
    def relatorio(self, condicao=True):
        self.df["Validade"] = tratamento_data(self.df["Validade"])
        if condicao:
            return converter_df(self.df)
        else:
            return self.df
    
    def relatorio_filtrado(self, filtro, dado):
        coluna = ["Código Produto", "Descrição Produto", "Laboratório", "Lista/Adendo", "Lote", "Registro MS", "Validade", "Código de barras", "Estoque"]
        if filtro not in coluna:
            return print("Coluna não encontrada!")
        else:
            tabela_dados = [i for i in self.df[filtro]]
            if dado in tabela_dados:
                self.df["Validade"] = tratamento_data(self.df["Validade"])
                tabela_filtrada = self.df[self.df[filtro] == dado]
                return converter_df(tabela_filtrada)
            else:
                return print("Dado não encontrado!")