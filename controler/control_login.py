import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from config import DB

def valida_usuario(solicitacao=list()):
    banco = DB()
    cursor = banco.conexao_db()
    cursor.execute("SELECT * FROM usuario WHERE nome = %s AND senha = %s", (solicitacao[0], solicitacao[1]))
    dados = cursor.fetchall()

    if dados:
        return True
    else:
        return False