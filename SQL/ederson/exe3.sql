create database BD;
use BD;

create table DEPARTAMENTO (
idcódigo int auto_increment,
nome varchar(30) not null,
telefone varchar(30) not null,
centro varchar(30) not null,
primary key(idcódigo)
);

create table ALUNO(

nome varchar(30) not null,
telefone varchar(30) not null,
matricula int(30) not null,
CPF int(30) not null,
endereço varchar(30) not null,
datanascimento int(30) not null,
sexo varchar(30) not null,

);














