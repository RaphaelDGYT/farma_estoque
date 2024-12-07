import os
import sys
import mysql.connector as mysql
from datetime import datetime
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from config import DB
from model.movimentacao import Movimentacao

def cadastrar_medicamento(descricao, laboratorio, lista_adendo, lote, reg_ms, validade, cod_barras, estoque=1):
    try:
        validade = validade.strftime('%Y-%m-%d')
        banco = DB()
        cursor = banco.conexao_db()
        cursor.execute("SELECT * FROM medicamento WHERE reg_ms = %s", [reg_ms])
        verifica = cursor.fetchall()

        if verifica:
            cursor.execute("UPDATE medicamento SET estoque = estoque + %s WHERE reg_ms = %s", (estoque, reg_ms))
            banco.conn.commit()
            Movimentacao(reg_ms).registro_entrada(estoque)
            banco.conn.commit()
        else:
            cursor.execute("""INSERT INTO medicamento (descricao, laboratorio, lista_adendo, lote, reg_ms, validade, cod_barras, estoque)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                (descricao, laboratorio, lista_adendo, lote, reg_ms, validade, cod_barras, estoque))
            banco.conn.commit()
            Movimentacao(reg_ms).registro_entrada(estoque)
            banco.conn.commit()
        return True
    except mysql.Error:
        print("Erro ao cadastrar medicamento!")
        return False
    finally:
        banco.fechar_conexao()
