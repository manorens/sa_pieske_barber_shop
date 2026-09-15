create database if not exists pieskebs;
use pieskebs;

-- Tabela de agendamentos
create table agendamentos (
    id int auto_increment primary key,
    cliente varchar(100) not null,
    telefone varchar(20),
    servico varchar(100),
    preco decimal(10,2),
    barbeiro varchar(50),
    data date not null,
    horario varchar(5),
    status varchar(20) default 'Agendado'
);

-- Inserção de 8 agendamentos (2 Concluido, 1 Cancelado, 5 Agendado)
insert into agendamentos (cliente, telefone, servico, preco, barbeiro, data, horario, status)
values
('Lucas Almeida',    '(47) 99911-2233', 'Corte social',        35.00, 'João',   '2026-09-15', '09:00', 'Agendado'),
('Pedro Henrique',   '(47) 99822-3344', 'Corte + barba',       60.00, 'Marcos', '2026-09-15', '10:30', 'Concluído'),
('Gabriel Souza',    '(47) 99733-4455', 'Barba',               25.00, 'Rafael', '2026-09-16', '14:00', 'Agendado'),
('Matheus Oliveira', '(47) 99644-5566', 'Corte degradê',       45.00, 'João',   '2026-09-16', '15:30', 'Cancelado'),
('Felipe Santos',    '(47) 99555-6677', 'Corte + sobrancelha', 50.00, 'Carlos', '2026-09-17', '09:30', 'Agendado'),
('Bruno Martins',    '(47) 99466-7788', 'Corte tradicional',   35.00, 'Marcos', '2026-09-17', '11:00', 'Concluído'),
('Rafael Costa',     '(47) 99377-8899', 'Barba + pigmentação', 70.00, 'Rafael', '2026-09-18', '16:00', 'Agendado'),
('André Lima',       '(47) 99288-9900', 'Corte infantil',      30.00, 'Carlos', '2026-09-19', '13:00', 'Agendado');

select * from agendamentos;

drop database barbearia;