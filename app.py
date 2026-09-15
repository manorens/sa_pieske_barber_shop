# app.py
# Aplicacao web Flask da Pieske Barber Shop.

from flask import Flask, render_template
import agendamentos                      # Modulo com as funcoes do banco

app = Flask(__name__)                    # Cria a aplicacao Flask

NOME_BARBEARIA = "Pieske Barber Shop"    # Nome exibido nas paginas


@app.route("/")
def index():
    """Pagina inicial: nome da barbearia e total de agendamentos."""
    lista = agendamentos.listar_agendamentos()
    return render_template("index.html",
                           barbearia=NOME_BARBEARIA,
                           agendamentos=lista)


@app.route("/agendamentos")
def listar():
    """Tabela com todos os agendamentos."""
    lista = agendamentos.listar_agendamentos()
    return render_template("agendamentos.html",
                           barbearia=NOME_BARBEARIA,
                           agendamentos=lista,
                           filtro=None)


@app.route("/agendamentos/status/<status>")
def listar_status(status):
    """Tabela com os agendamentos filtrados por status."""
    lista = agendamentos.listar_por_status(status)
    return render_template("agendamentos.html",
                           barbearia=NOME_BARBEARIA,
                           agendamentos=lista,
                           filtro=status)


@app.route("/agendamento/<int:id>")
def detalhe(id):
    """Detalhe de um agendamento especifico."""
    agendamento = agendamentos.buscar_agendamento(id)
    return render_template("detalhe.html",
                           barbearia=NOME_BARBEARIA,
                           agendamento=agendamento)


# Executa o servidor apenas quando o arquivo e rodado diretamente
if __name__ == "__main__":
    app.run(debug=True)
