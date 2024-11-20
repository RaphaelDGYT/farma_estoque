import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from config import DB  

def valida_usuario(usuario: str, senha: str) -> bool:
 
    banco = DB()  
    cursor = banco.conexao_db()  

    # Consulta SQL para verificar se o usuário e a senha existem no banco de dados
    cursor.execute("SELECT * FROM usuario WHERE nome = %s AND senha = %s", (usuario, senha))
    dados = cursor.fetchall()  # Obtém os dados da consulta

   
    if dados:
        return True
    else:
        return False
