from config import cursor

def valida_usuario(solicitacao=list()):
    try:
        cursor.execute("SELECT * FROM usuarios WHERE nome = %s AND senha = %s", (solicitacao[0], solicitacao[1]))
        dados = cursor.fetchall()

        if not dados:
            return True
        else:
            return False
    except sqlite3.Error as error:
        print("Erro ao conectar ao banco de dados", error)
    
