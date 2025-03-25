create database bank;
use bank;

create table Clientes(
id_cliente int primary key,
numero_conta varchar(20) unique not null,
nome varchar(100) not null,
id_cidade int,
id_estado int,
id_genero int,
id_raca int,
id_religiao int,
id_agencia int,
saldo float default 0.00,
FOREIGN KEY (id_agencia) REFERENCES Agencias(id_agencia),

FOREIGN KEY (id_cidade) REFERENCES Cidade(id_cidade),
FOREIGN KEY (id_estado) REFERENCES Estado(id_estado),
FOREIGN KEY (id_genero) REFERENCES Genero(id_genero),
FOREIGN KEY (id_raca) REFERENCES Raca(id_raca),
FOREIGN KEY (id_religiao) REFERENCES Religiao(id_religiao)
    );

create table Agencias(
id_agencia int primary key,
numero_agencia varchar(10) not null,
endereco varchar(200) not null,
id_cidade int,
FOREIGN KEY (id_cidade) REFERENCES Cidade(id_cidade)
);

create table Cidade(
id_cidade int primary key,
nome varchar(100) not null,
id_estado int,
FOREIGN KEY (id_estado) REFERENCES Estado(id_estado)
);

create table Estado(
id_estado int primary key,
nome varchar(50) not null,
uf char(2) not null
);

create table Genero(
	id_genero int primary key,
    descricao varchar(50) not null
);

create table Raca (
id_raca int primary key,
descricao varchar(50) not null
);

create table Religiao (
id_religiao int primary key,
descricao varchar(100) not null
);

create table Saque(
id_operacao int primary key,
id_agencia int,
id_cliente int,
valor float not null,
foreign key (id_agencia) references Agencias(id_agencia),
foreign key (id_cliente) references Clientes(id_cliente)
);
create table Deposito(
id_operacao int primary key,
id_agencia int,
id_cliente int,
valor float NOT NULL,
FOREIGN KEY (id_agencia) REFERENCES Agencias(id_agencia),
FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente)
);
