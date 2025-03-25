create database escola;
use escola;

create table dadosAluno(

	matricula int auto_increment,
    nome varchar (30) not null,
    email varchar (30) not null,
    primary key (matricula));
    
    insert into dadosAluno(matricula,nome,email) values(null,"bazz","bazz@gmail.com"),
    (null,"rogi","rogi@gmail.com"),
    (null,"MariaE","eaduardabaez9@gmail.com");
    
    
create table Estado(
	id int auto_increment,
    estado varchar (30)not null,
    sigla varchar (30)not null,
    primary key (id));


create table cidade(
	idcidade int auto_increment,
	nome varchar (30)not null,
    idestado int not null,
    regiao varchar (30)not null,
    foreign key (idestado) references Estado(id),
	primary key (idcidade));


insert into Estado(id,estado,sigla) values(null,"Acre","AC"),
(null,"Alagoas","AL"),
(null,"Amapá","AP"),
(null,"Amazonas","AM"),
(null,"Bahia","BA"),
(null,"Ceará","CE"),
(null,"Espírito Santo","ES"),
(null,"Goiás","GO"),
(null,"Maranhão","MA"),
(null,"Mato Grosso","MT"),
(null,"Mato Grosso do Sul","MS"),
(null,"Minas Gerais","MG"),
(null,"Pará","PA"),
(null,"Paraíba","PB"),
(null,"Paraná","PR"),
(null,"Pernambuco","PE"),
(null,"Piauí","PI"),
(null,"Rio de Janeiro","RJ"),
(null,"Rio Grande do Norte","RN"),
(null,"Rio Grande do Sul","RS"),
(null,"Rondônia","RO"),
(null,"Roraima","RR"),
(null,"Santa Catarina","SC"),
(null,"São Paulo","SP"),
(null,"Sergipe","SE"),
(null,"Tocantins","TO"),
(null,"Distrito Federal","DF");

insert into cidade(idcidade,nome,idestado,regiao) values
(null,"Campo Grande",11,"centro"),
(null,"São Paulo",24,"centro"),
(null,"Rio deJaneiro",17,"centro");



