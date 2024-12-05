import os
import sys
import mysql.connector as mysql
from datetime import datetime
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from config import DB
from movimentacao import Movimentacao

def cadastrar_medicamento(descricao, laboratorio, lista_adendo, lote, reg_ms, validade, cod_barras, estoque=1):
    try:
        # Verifica se a validade já é string, caso contrário, converte para o formato correto
        if isinstance(validade, datetime):
            validade = validade.strftime('%Y-%m-%d')
        
        banco = DB()
        cursor = banco.conexao_db()
        cursor.execute("SELECT * FROM medicamento WHERE reg_ms = %s", [reg_ms])
        verifica = cursor.fetchall()

        if verifica:
            cursor.execute("UPDATE medicamento SET estoque = estoque + %s WHERE reg_ms = %s", (estoque, reg_ms))
            Movimentacao(reg_ms).registro_entrada(estoque)
            banco.conn.commit()
        else:
            cursor.execute("""INSERT INTO medicamento (descricao, laboratorio, lista_adendo, lote, reg_ms, validade, cod_barras, estoque)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                (descricao, laboratorio, lista_adendo, lote, reg_ms, validade, cod_barras, estoque))
            Movimentacao(reg_ms).registro_entrada(estoque)
            banco.conn.commit()
        return True
    except mysql.Error as err:
        print(f"Erro ao cadastrar medicamento!")
        return False
    finally:
        banco.fechar_conexao()
