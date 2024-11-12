import os
import sys
import mysql.connector as mysql
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from config import DB

def retirar_medicamento(reg_ms=None, cod_barras=None, quantidade=1):
    if reg_ms is None and cod_barras is None:
        return False
    elif reg_ms is None:
        try:
            banco = DB()
            cursor = banco.conexao_db()
            cursor.execute("SELECT estoque FROM medicamento WHERE cod_barras = %s", [cod_barras])
            consulta = cursor.fetchone()
            if consulta:
                estoque = consulta[0]
                if estoque >= quantidade:
                    cursor.execute("UPDATE medicamento SET estoque = estoque - %s WHERE cod_barras = %s", (quantidade, cod_barras))
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
    elif cod_barras is None:
        try:
            banco = DB()
            cursor = banco.conexao_db()
            cursor.execute("SELECT estoque FROM medicamento WHERE reg_ms = %s", [reg_ms])
            consulta = cursor.fetchone()

            if consulta:
                estoque = consulta[0]
                if estoque >= quantidade:
                    cursor.execute("UPDATE medicamento SET estoque = estoque - %s WHERE reg_ms = %s", (quantidade, reg_ms))
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

def deletar_medicamento(reg_ms=None, cod_barras=None):
    if reg_ms is None and cod_barras is None:
        return False
    elif reg_ms is None:
        try:
            banco = DB()
            cursor = banco.conexao_db()
            cursor.execute("DELETE FROM medicamento WHERE cod_barras = %s", [cod_barras])
            banco.conn.commit()
            return True
        except mysql.Error:
            return False
        finally:
            banco.fechar_conexao()
    elif cod_barras is None:
        try:
            banco = DB()
            cursor = banco.conexao_db()
            cursor.execute("DELETE FROM medicamento WHERE reg_ms = %s", [reg_ms])
            banco.conn.commit()
            return True
        except mysql.Error:
            return False
        finally:
            banco.fechar_conexao()