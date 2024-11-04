from dotenv import load_dotenv
import mysql.connector as mysql
import os

load_dotenv()  # Carrega as variáveis do arquivo .env

# Acessando as variáveis
host = os.getenv("MYSQLHOST")
user = os.getenv("MYSQLUSER")
password = os.getenv("MYSQLPASSWORD")
database = os.getenv("MYSQLDATABASE")
port = os.getenv("MYSQLPORT")

class DB():
    def __init__(self):
        try:
            self.conn = mysql.connect(
                host = host,
                user = user,
                password = password,
                database = database,
                port = port)
            self.cursor = self.conn.cursor()
        except mysql.Error as error:
            return "Erro ao conectar ao banco de dados", error
        
    def conexao_db(self):
        return self.cursor
    
    def fechar_conexao(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()