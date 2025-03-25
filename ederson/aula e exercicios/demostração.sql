CREATE DATABASE Universidade;
USE Universidade;

-- Tabela de Departamentos
CREATE TABLE Departamento (
    codigo INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(15),
    centro VARCHAR(100) NOT NULL
);

-- Tabela de Alunos
CREATE TABLE Aluno (
    matricula INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    cpf CHAR(11) UNIQUE NOT NULL,
    rua VARCHAR(100),
    cidade VARCHAR(50),
    cep CHAR(8),
    data_nascimento DATE NOT NULL,
    sexo ENUM('M', 'F') NOT NULL,
    departamento INT,
    curso INT,
    FOREIGN KEY (departamento) REFERENCES Departamento(codigo),
    FOREIGN KEY (curso) REFERENCES Curso(id)
);

-- Tabela de Telefones dos Alunos
CREATE TABLE Telefone_Aluno (
    matricula INT,
    telefone VARCHAR(15),
    PRIMARY KEY (matricula, telefone),
    FOREIGN KEY (matricula) REFERENCES Aluno(matricula)
);

-- Tabela de Cursos
CREATE TABLE Curso (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    tipo ENUM('Técnico', 'Graduação', 'Mestrado', 'Doutorado') NOT NULL,
    departamento INT,
    coordenador INT,
    vice_coordenador INT,
    FOREIGN KEY (departamento) REFERENCES Departamento(codigo),
    FOREIGN KEY (coordenador) REFERENCES Professor(id),
    FOREIGN KEY (vice_coordenador) REFERENCES Professor(id)
);

-- Tabela de Professores
CREATE TABLE Professor (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    cpf CHAR(11) UNIQUE NOT NULL,
    departamento INT,
    telefone VARCHAR(15),
    FOREIGN KEY (departamento) REFERENCES Departamento(codigo)
);

-- Tabela de Disciplinas
CREATE TABLE Disciplina (
    codigo INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    creditos INT NOT NULL,
    departamento INT,
    FOREIGN KEY (departamento) REFERENCES Departamento(codigo)
);

-- Tabela de Ofertas de Disciplinas
CREATE TABLE Oferta (
    id INT PRIMARY KEY AUTO_INCREMENT,
    disciplina INT,
    professor INT,
    horario VARCHAR(50) NOT NULL,
    FOREIGN KEY (disciplina) REFERENCES Disciplina(codigo),
    FOREIGN KEY (professor) REFERENCES Professor(id)
);

-- Tabela de Matrículas de Alunos em Disciplinas
CREATE TABLE Matricula (
    aluno INT,
    oferta INT,
    PRIMARY KEY (aluno, oferta),
    FOREIGN KEY (aluno) REFERENCES Aluno(matricula),
    FOREIGN KEY (oferta) REFERENCES Oferta(id)
);

-- Inserção de Departamentos
INSERT INTO Departamento (nome, telefone, centro) VALUES
('Ciência da Computação', '1111-1111', 'Tecnologia'),
('Engenharia Elétrica', '2222-2222', 'Tecnologia'),
('Matemática', '3333-3333', 'Ciências Exatas'),
('Física', '4444-4444', 'Ciências Exatas'),
('Biologia', '5555-5555', 'Ciências Naturais'),
('Química', '6666-6666', 'Ciências Naturais'),
('História', '7777-7777', 'Ciências Humanas'),
('Geografia', '8888-8888', 'Ciências Humanas'),
('Letras', '9999-9999', 'Ciências Humanas'),
('Filosofia', '1010-1010', 'Ciências Humanas');

-- Inserção de Professores
INSERT INTO Professor (nome, cpf, departamento, telefone) VALUES
('Carlos Silva', '12345678901', 1, '4002-8922'),
('Ana Oliveira', '23456789012', 2, '4003-8923'),
('João Souza', '34567890123', 3, '4004-8924'),
('Mariana Lima', '45678901234', 4, '4005-8925'),
('Pedro Rocha', '56789012345', 5, '4006-8926'),
('Fernanda Alves', '67890123456', 6, '4007-8927'),
('Roberto Mendes', '78901234567', 7, '4008-8928'),
('Carla Torres', '89012345678', 8, '4009-8929'),
('Gustavo Nunes', '90123456789', 9, '4010-8930'),
('Juliana Castro', '01234567890', 10, '4011-8931');

-- Inserção de Cursos
INSERT INTO Curso (nome, tipo, departamento, coordenador, vice_coordenador) VALUES
('Engenharia de Software', 'Graduação', 1, 1, 2),
('Engenharia Elétrica', 'Graduação', 2, 2, 3),
('Matemática Aplicada', 'Mestrado', 3, 3, 4),
('Física Nuclear', 'Doutorado', 4, 4, 5),
('Biotecnologia', 'Graduação', 5, 5, 6),
('Química Industrial', 'Mestrado', 6, 6, 7),
('História da Arte', 'Graduação', 7, 7, 8),
('Geografia Ambiental', 'Mestrado', 8, 8, 9),
('Letras Português', 'Graduação', 9, 9, 10),
('Filosofia Política', 'Doutorado', 10, 10, 1);


-- Inserção de Alunos
INSERT INTO Aluno (nome, cpf, rua, cidade, cep, data_nascimento, sexo, departamento, curso) VALUES
('Lucas Santos', '12312312312', 'Rua A', 'Cidade X', '11111111', '2000-01-01', 'M', 1, 1),
('Mariana Souza', '23423423423', 'Rua B', 'Cidade Y', '22222222', '1999-02-02', 'F', 2, 2),
('Pedro Lima', '34534534534', 'Rua C', 'Cidade Z', '33333333', '2001-03-03', 'M', 3, 3),
('Ana Clara', '45645645645', 'Rua D', 'Cidade X', '44444444', '1998-04-04', 'F', 4, 4),
('João Pedro', '56756756756', 'Rua E', 'Cidade Y', '55555555', '2002-05-05', 'M', 5, 5),
('Fernanda Rocha', '67867867867', 'Rua F', 'Cidade Z', '66666666', '1997-06-06', 'F', 6, 6),
('Guilherme Nunes', '78978978978', 'Rua G', 'Cidade X', '77777777', '2003-07-07', 'M', 7, 7),
('Camila Torres', '89089089089', 'Rua H', 'Cidade Y', '88888888', '1996-08-08', 'F', 8, 8),
('Gustavo Almeida', '90190190190', 'Rua I', 'Cidade Z', '99999999', '2004-09-09', 'M', 9, 9),
('Juliana Mendes', '01201201201', 'Rua J', 'Cidade X', '10101010', '1995-10-10', 'F', 10, 10);

-- Inserção de Disciplinas
INSERT INTO Disciplina (nome, descricao, creditos, departamento) VALUES
('Banco de Dados', 'Estudo de bancos de dados relacionais', 4, 1),
('Sistemas Operacionais', 'Funcionamento de SOs', 4, 1),
('Circuitos Elétricos', 'Conceitos de circuitos', 4, 2);
