from config import DB
import mysql.connector as mysql
from datetime import datetime

def cadastrar_medicamento(descricao, laboratorio, lista_adendo, lote, reg_ms, validade, cod_barras, estoque=1):
    try:
        validade = validade.strftime('%Y-%m-%d')
        banco = DB()
        cursor = banco.conexao_db()

        cursor.execute("SELECT * FROM medicamento WHERE reg_ms = %s AND cod_barras = %s", (reg_ms, cod_barras))
        verifica = cursor.fetchall()

        if verifica:
            cursor.execute("UPDATE medicamento SET estoque = estoque + %s WHERE reg_ms = %s", (estoque, reg_ms))
            banco.conn.commit()
        else:
            cursor.execute("""INSERT INTO medicamento (descricao, laboratorio, lista_adendo, lote, reg_ms, validade, cod_barras, estoque)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                (descricao, laboratorio, lista_adendo, lote, reg_ms, validade, cod_barras, estoque))
            banco.conn.commit()
        return True
    except mysql.Error:
        return False
    finally:
        banco.fechar_conexao()