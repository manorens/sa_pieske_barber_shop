==============================================================
PIESKE BARBER SHOP - Sistema Web de Agendamentos
==============================================================
SENAI Santa Catarina
Curso Técnico em Desenvolvimento de Sistemas
Unidade Curricular: Programação de Aplicativos
Docente: Lucas Grandeaux

--------------------------------------------------------------
INTEGRANTES
--------------------------------------------------------------
1) Renan Kahl - Papel: banco de dados (banco.sql, config.py, banco.py)
2) Lucas Ruan - Papel: modelos e funções (models.py, agendamentos.py)
3) Igor Lipinski - Papel: aplicação e templates (app.py, templates/)

--------------------------------------------------------------
SOBRE O PROJETO
--------------------------------------------------------------
Sistema web para a Pieske Barber Shop substituir o caderno de
agendamentos do balcão. Permite ver o total de agendamentos,
listar todos em uma tabela, filtrar por status (Agendado,
Concluído, Cancelado) e abrir o detalhe de cada um.

Tecnologias: Python 3, Flask, Jinja2 e MySQL
(biblioteca mysql-connector-python).

--------------------------------------------------------------
REQUISITOS
--------------------------------------------------------------
- Python 3 instalado
- MySQL Server e MySQL Workbench instalados
- PyCharm (ou outra IDE)

--------------------------------------------------------------
COMO RODAR O PROGRAMA
--------------------------------------------------------------
1) Instalar as bibliotecas
   Abrir o terminal do PyCharm (aba "Terminal") e executar:

       pip install flask mysql-connector-python

2) Criar o banco de dados
   - Abrir o MySQL Workbench e conectar no servidor local
   - Abrir o arquivo banco.sql (File > Open SQL Script)
   - Executar o script inteiro (ícone do raio)
   - Isso cria o banco "barbearia", a tabela "agendamentos"
     e insere 8 agendamentos de exemplo

3) Configurar as credenciais
   - Abrir o arquivo config.py
   - Ajustar USUARIO e SENHA conforme o MySQL da sua máquina

4) Iniciar o servidor
   - Executar o arquivo app.py (botão direito > Run 'app')
   - ATENÇÃO: o arquivo a executar é o app.py, e não o agendamentos.py

5) Abrir no navegador
   http://127.0.0.1:5000

--------------------------------------------------------------
PÁGINAS DO SISTEMA
--------------------------------------------------------------
/                                -> Início: nome da barbearia e total de agendamentos
/agendamentos                    -> Tabela com todos os agendamentos
/agendamentos/status/<status>    -> Agendamentos filtrados por status
                                    (Agendado, Concluído ou Cancelado)
/agendamento/<id>                -> Detalhe de um agendamento

Na tabela, a linha fica verde para "Concluído", vermelha para
"Cancelado" e sem cor para "Agendado".

--------------------------------------------------------------
ESTRUTURA DE ARQUIVOS
--------------------------------------------------------------
barbearia/
  config.py          - credenciais do banco
  banco.py           - função conectar()
  models.py          - classe Agendamento
  agendamentos.py    - funções da tabela agendamentos
  app.py             - aplicação Flask (rotas)
  banco.sql          - criação do banco e inserção dos dados
  README.txt         - este arquivo
  templates/
    index.html
    agendamentos.html
    detalhe.html

--------------------------------------------------------------
PROBLEMAS COMUNS
--------------------------------------------------------------
- "No module named 'flask'" ou "'mysql.connector'"
  -> faltou instalar as bibliotecas (passo 1).

- "Access denied for user 'root'@'localhost'"
  -> usuário ou senha incorretos em config.py.

- "Unknown database 'barbearia'"
  -> o banco.sql ainda não foi executado no Workbench (passo 2).

- "TemplateNotFound"
  -> os arquivos .html precisam estar dentro da pasta templates,
     ao lado do app.py.

- Tabela vazia ou filtros sem resultado
  -> o status deve estar escrito exatamente como
     "Agendado", "Concluído" ou "Cancelado" (com acento).
