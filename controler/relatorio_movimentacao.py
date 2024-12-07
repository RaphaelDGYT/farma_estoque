import os
import sys
import pandas as pd
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from config import DB
from utils_model import converter_df

class RelatorioMovimentacao():
    def __init__(self):
        self.banco = DB()
        self.cursor = self.banco.conexao_db()
        self.cursor.execute("""SELECT movimentacao.id, medicamento.descricao, medicamento.quantidade, movimentacao.operacao, movimentacao.data 
                            FROM movimentacao
                            INNER JOIN medicamento ON movimentacao.id_medicamento = medicamento.id""")
        self.df = pd.DataFrame(self.cursor.fetchall())
        self.df.columns = ["Código Operação", "Descrição Medicamento", "Quantidade", "Operação", "Data"]

    def movimentacao_geral(self):
        return converter_df(self.df)
    
    def movimentacao_entrada(self):
        self.df = self.df[self.df["Operação"] == "adicionado"]
        return converter_df(self.df)

    def movimentacao_saida(self):
        self.df = self.df[self.df["Operação"] == "retirado"]
        return converter_df(self.df)

    def movimentacao_exclusao(self):
        self.df = self.df[self.df["Operação"] == "excluido"]
        return converter_df(self.df)