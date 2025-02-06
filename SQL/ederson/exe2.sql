create database exe1;
use exe1;

create table dependent (
    matricula int auto_increment,
    nome varchar(30)not null,
    fone varchar(30)not null,
    dep int not null,
    primary key(matricula),
    foreign key (dep) references parent(dep));
    
create table parent(
	dep int auto_increment,
    descr varchar(30)not null,
    primary key(dep));
describe dependent;
