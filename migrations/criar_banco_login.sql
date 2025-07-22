-- Criação do banco de dados
CREATE DATABASE IF NOT EXISTS login_sistema;

-- Seleciona o banco de dados
USE login_sistema;

-- Criação da tabela de usuários
CREATE TABLE IF NOT EXISTS usuarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    senha VARCHAR(100) NOT NULL
);
