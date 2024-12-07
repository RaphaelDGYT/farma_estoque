import os
import sys
import mysql.connector as mysql
from datetime import datetime
from pytz import timezone
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from config import DB

class Movimentacao():
    def __init__(self, reg_ms=None, id=None):
        self.banco = DB()
        self.cursor = self.banco.conexao_db()

        self.fuso_horario = timezone("America/Sao_Paulo")
        self.data = datetime.now(self.fuso_horario).strftime("%Y/%m/%d %H:%M")
        if reg_ms is not None:
            self.reg_ms = reg_ms
            self.cursor.execute("SELECT id FROM medicamento WHERE reg_ms = %s", [reg_ms])
            self.consulta = self.cursor.fetchone()
            self.id_medicamento = self.consulta[0]
        else:
            self.id_medicamento = id

    def registro_entrada(self, quantidade=1):
        try:
            if self.id_medicamento:
                self.cursor.execute("INSERT INTO movimentacao (id_medicamento, quantidade, operacao, data) VALUES (%s, %s, %s, %s)",
                                    (self.id_medicamento, quantidade, "adicionado", self.data))
                self.banco.conn.commit()
                return True
            else:
                return False
        except mysql.Error:
            return print("Ocorreu um erro ao realizar a transação!")
        finally:
            self.banco.fechar_conexao()

    def registro_saida(self, quantidade=1):
        try:
            if self.id_medicamento:
                self.cursor.execute("INSERT INTO movimentacao (id_medicamento, quantidade, operacao, data) VALUES (%s, %s, %s, %s)",
                                    (self.id_medicamento, quantidade, "retirado", self.data))
                self.banco.conn.commit()
                return True
            else:
                return False
        except mysql.Error:
            return print("Ocorreu um erro ao realizar a transação!")
        finally:
            self.banco.fechar_conexao()

    def registro_exclusao(self):
        try:
            if self.id_medicamento:
                self.cursor.execute("INSERT INTO movimentacao (id_medicamento, quantidade, operacao, data) VALUES (%s, %s, %s, %s)",
                                    (self.id_medicamento, 0, "excluido", self.data))
                self.banco.conn.commit()
                return True
            else:
                return False
        except mysql.Error:
            return print("Ocorreu um erro ao realizar a transação!")
        finally:
            self.banco.fechar_conexao()