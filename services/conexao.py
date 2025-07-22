import mysql.connector
from dotenv import load_dotenv
import os

# Carrega as variáveis do arquivo .env automaticamente
load_dotenv()

def conectar():
    # Cria e retorna a conexão com o banco usando dados do .env
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),       # endereço do banco (ex: localhost)
        user=os.getenv("DB_USER"),       # usuário do banco
        password=os.getenv("DB_PASSWORD"), # senha do banco
        database=os.getenv("DB_NAME")    # nome do banco
    )
