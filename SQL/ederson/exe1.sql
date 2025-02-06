create database exe2;
use exe2;

create table faturamento (
    codFaturamento int auto_increment,
    nomeFaturamento varchar(30)not null,
    tipoFaturamento int default(1),
    dtaFaturamento varchar(30)not null,
    totalFaturamento varchar(30)not null,
    codLucro int not null,
	primary key(codFaturamento),
    foreign key (codLucro) references lucros(codLucro));

create table lucros (
    codLucro int auto_increment,
    nomeLucro varchar(30)not null,
    tipoLucro int default(1),
    dtaLucro varchar(30)not null,
    totalLucro varchar(30)not null,
    primary key(codLucro));
    
    
create table despesa (
    codDespesa int auto_increment,
    nomeDespesa varchar(30)not null,
    tipoDespesa int default(1),
    dtaDespesa varchar(30)not null,
    valorDespesa varchar(30)not null,
    descrDespesa varchar(30)not null,
    codLucro int not null,
	primary key(codDespesa),
    foreign key (codLucro) references lucros(codLucro));
     
describe faturamento;
describe lucros;
describe despesa;



    
    