import os
import sys
import mysql.connector as mysql
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from config import DB
from model.movimentacao import Movimentacao

def retirar_medicamento(reg_ms=None, id=None, quantidade=1):
    if reg_ms is None and id is None:
        return False
    elif reg_ms is None:
        try:
            banco = DB()
            cursor = banco.conexao_db()
            cursor.execute("SELECT estoque FROM medicamento WHERE id = %s", [id])
            consulta = cursor.fetchone()
            if consulta:
                estoque = consulta[0]
                if estoque >= quantidade:
                    cursor.execute("UPDATE medicamento SET estoque = estoque - %s WHERE id = %s", (quantidade, id))
                    Movimentacao(id).registro_saida(quantidade)
                    banco.conn.commit()
                    return True
                else:
                    return 2 # 2 representa que a quantidade é maior que o próprio estoque
            else:
                return 1 # 1 representa que o medicamento não existe
        except mysql.Error:
            return False
        finally:
            banco.fechar_conexao()
    elif id is None:
        try:
            banco = DB()
            cursor = banco.conexao_db()
            cursor.execute("SELECT estoque FROM medicamento WHERE reg_ms = %s", [reg_ms])
            consulta = cursor.fetchone()

            if consulta:
                estoque = consulta[0]
                if estoque >= quantidade:
                    cursor.execute("UPDATE medicamento SET estoque = estoque - %s WHERE reg_ms = %s", (quantidade, reg_ms))
                    Movimentacao(reg_ms).registro_saida(quantidade)
                    banco.conn.commit()
                    return True
                else:
                    return 2 # 2 representa que a quantidade é maior que o próprio estoque
            else:
                return 1 # 1 representa que o medicamento não existe
        except mysql.Error:
            return False
        finally:
            banco.fechar_conexao()

def deletar_medicamento(reg_ms=None, id=None):
    if reg_ms is None and id is None:
        return False
    elif reg_ms is None:
        try:
            banco = DB()
            cursor = banco.conexao_db()
            cursor.execute("DELETE FROM medicamento WHERE id = %s", [id])
            Movimentacao(id).registro_exclusao()
            banco.conn.commit()
            return True
        except mysql.Error:
            return False
        finally:
            banco.fechar_conexao()
    elif id is None:
        try:
            banco = DB()
            cursor = banco.conexao_db()
            cursor.execute("DELETE FROM medicamento WHERE reg_ms = %s", [reg_ms])
            Movimentacao(reg_ms).registro_exclusao
            banco.conn.commit()
            return True
        except mysql.Error:
            return False
        finally:
            banco.fechar_conexao()