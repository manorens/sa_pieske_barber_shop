# agendamentos.py
# Modulo com as funcoes que acessam a tabela "agendamentos".

import mysql.connector                 # Usado para tratar os erros do MySQL
from banco import conectar             # Funcao de conexao
from models import Agendamento         # Classe do modelo


def listar_agendamentos():
    """Retorna uma lista de objetos Agendamento ordenados por data e horario."""
    conexao = None
    lista = []
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            select id, cliente, telefone, servico, preco,
                   barbeiro, data, horario, status
            from agendamentos
            order by data, horario
        """)
        # Converte cada tupla retornada em um objeto Agendamento
        for linha in cursor.fetchall():
            lista.append(Agendamento.reverte_tupla(linha))
    except mysql.connector.Error as erro:
        print("Erro ao listar agendamentos:", erro)
    finally:
        # Fecha a conexao mesmo se ocorrer erro
        if conexao is not None and conexao.is_connected():
            conexao.close()
    return lista


def buscar_agendamento(id):
    """Retorna um objeto Agendamento pelo id, ou None se nao existir."""
    conexao = None
    agendamento = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            select id, cliente, telefone, servico, preco,
                   barbeiro, data, horario, status
            from agendamentos
            where id = %s
        """, (id,))
        linha = cursor.fetchone()
        if linha:                      # Só converte se encontrou o registro
            agendamento = Agendamento.reverte_tupla(linha)
    except mysql.connector.Error as erro:
        print("Erro ao buscar agendamento:", erro)
    finally:
        if conexao is not None and conexao.is_connected():
            conexao.close()
    return agendamento


def listar_por_status(status):
    """Retorna os agendamentos que possuem um status especifico."""
    conexao = None
    lista = []
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            select id, cliente, telefone, servico, preco,
                   barbeiro, data, horario, status
            from agendamentos
            where status = %s
            order by data, horario
        """, (status,))
        for linha in cursor.fetchall():
            lista.append(Agendamento.reverte_tupla(linha))
    except mysql.connector.Error as erro:
        print("Erro ao filtrar agendamentos por status:", erro)
    finally:
        if conexao is not None and conexao.is_connected():
            conexao.close()
    return lista
