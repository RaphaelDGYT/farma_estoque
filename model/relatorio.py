import os
import sys  
import pandas as pd
import datetime as datetime
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from config import DB

# Formatando a data para devolver apenas ano e mês
def tratamento_data(data=list()):
    data_formatada = []
    for i in data:
        i = i.strftime("%Y/%m/%d")
        i = i[:7]
        data_formatada.append(i)
    return data_formatada

class Relatorio():
    def __init__(self):
        self.banco = DB()
        self.cursor = self.banco.conexao_db()
        self.cursor.execute("SELECT * FROM medicamento")
        self.df = pd.DataFrame(self.cursor.fetchall())
        self.df.columns = ["Código Produto", "Descrição Produto", "Laboratório", "Lista/Adendo", "Lote", "Registro MS", "Validade", "Código de barras", "Estoque"]
        
    def relatorio(self):
        self.df["Validade"] = tratamento_data(self.df["Validade"])
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
                return tabela_filtrada
            else:
                return print("Dado não encontrado!")