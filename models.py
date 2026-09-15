# models.py
# Modulo de modelos: contem a classe que representa um agendamento.


class Agendamento:

    def __init__(self, cliente, telefone, servico, preco,
                 barbeiro, data, horario, status="Agendado", id=None):
        # Atributos do agendamento
        self.id = id                 # Chave primaria (vem do banco)
        self.cliente = cliente       # Nome do cliente
        self.telefone = telefone     # Telefone de contato
        self.servico = servico       # Servico contratado
        self.preco = preco           # Valor do servico
        self.barbeiro = barbeiro     # Barbeiro responsavel
        self.data = data             # Data do atendimento
        self.horario = horario       # Horario no formato HH:MM
        self.status = status          # Agendado / Concluido / Cancelado

    def exibir(self):
        """Retorna os dados do agendamento formatados em uma unica linha."""
        return (f"#{self.id} | {self.cliente} | {self.telefone} | "
                f"{self.servico} | R$ {self.preco} | {self.barbeiro} | "
                f"{self.data} {self.horario} | {self.status}")

    def converte_tupla(self):
        """Converte o objeto em uma tupla, na ordem das colunas da tabela."""
        return (self.cliente, self.telefone, self.servico, self.preco,
                self.barbeiro, self.data, self.horario, self.status)

    @staticmethod
    def reverte_tupla(tupla):
        """Recebe uma tupla vinda do banco e devolve um objeto Agendamento.

        Ordem esperada da tupla:
        (id, cliente, telefone, servico, preco, barbeiro, data, horario, status)
        """
        return Agendamento(
            id=tupla[0],
            cliente=tupla[1],
            telefone=tupla[2],
            servico=tupla[3],
            preco=tupla[4],
            barbeiro=tupla[5],
            data=tupla[6],
            horario=tupla[7],
            status=tupla[8]
        )
