# banco.py
# Modulo responsavel unicamente pela conexao com o banco de dados.

import mysql.connector          # Driver de conexao do MySQL com Python
import config                   # Importa as credenciais do arquivo config.py


def conectar():
    """Cria e retorna uma conexao com o banco de dados MySQL."""
    conexao = mysql.connector.connect(
        host=config.HOST,
        user=config.USUARIO,
        password=config.SENHA,
        database=config.BANCO
    )
    return conexao
