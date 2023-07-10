/*Criação da base de dados*/
/*CREATE DATABASE qtop_db;*/

/*Garantindo as permissões do usuário 'postgres'*/
GRANT ALL PRIVILEGES ON DATABASE qtop_db TO postgres;

/*Trocando a conexão para o banco de dados criado*/
\c qtop_db

/*Criação da tabela de administradores do menu de pedidos*/
CREATE TABLE qtop_usuarios_admin (
    usuario_id SERIAL PRIMARY KEY,
    usuario_nome VARCHAR(50) NOT NULL,
    usuario_cpf VARCHAR(11) NOT NULL
);

/*Inserção de usuários administradores do menu de pedidos*/
INSERT INTO qtop_usuarios_admin (usuario_nome, usuario_cpf) VALUES
    ('Marcos', '11122233345'),
    ('admin', '01234567890');

/*Criação da tabela de clientes*/
CREATE TABLE qtop_clientes (
    cliente_id SERIAL,
    cliente_nome VARCHAR(50) NOT NULL,
    cliente_cpf VARCHAR(15) NOT NULL,
    cliente_email VARCHAR(150) NOT NULL
);

/*Inserção de cliente teste*/
INSERT INTO qtop_clientes (cliente_nome, cliente_cpf, cliente_email) VALUES
    ('Joao', '11111111111','joao-silva@outlook.com');

/*Criação da tabela de lanches*/
CREATE TABLE qtop_lanches (
    lanche_id SERIAL,
    lanche_nome VARCHAR(50) NOT NULL,
    lanche_descricao VARCHAR(250) NOT NULL,
    lanche_preco NUMERIC (10, 2) NOT NULL,
    lanche_foto VARCHAR(150) NOT NULL
);
/*Inserção de lanches*/
INSERT INTO qtop_lanches (lanche_nome, lanche_descricao, lanche_preco, lanche_foto) VALUES
('Hamburger', 'Uma carne, queijo, alface, picles, tomate e cebola', '20.00', 'hamburger.jpg');

INSERT INTO qtop_lanches (lanche_nome, lanche_descricao, lanche_preco, lanche_foto) VALUES
('Sanduíche', 'Pão de forma integral, alface, tomate, queijo e presunto', '15.00', 'sanduiche.jpg');

INSERT INTO qtop_lanches (lanche_nome, lanche_descricao, lanche_preco, lanche_foto) VALUES
('Hot Dog', 'Duas salsichas, batata palha, alface e vinagrete', '12.00', 'hotdog.jpg');

/*Criação da tabela de bebidas*/
CREATE TABLE qtop_bebidas (
    bebida_id SERIAL,
    bebida_nome VARCHAR(50) NOT NULL,
    bebida_descricao VARCHAR(250) NOT NULL,
    bebida_preco NUMERIC (10, 2) NOT NULL,
    bebida_foto VARCHAR(150) NOT NULL
);
/*Inserção de bebidas*/
INSERT INTO qtop_bebidas (bebida_nome, bebida_descricao, bebida_preco, bebida_foto) VALUES
('Sucos','Sucos naturais com 500ml: Laranja, acerola, abacaxi, com combinações de água, leite ou hortelã', '12.50','suco.jpg');

INSERT INTO qtop_bebidas (bebida_nome, bebida_descricao, bebida_preco, bebida_foto) VALUES
('Vitaminas','Vitaminas naturais com 500ml: Abacate, morango, banana com mamão, frutas vermelhas', '15.00','vitamina.jpeg');

INSERT INTO qtop_bebidas (bebida_nome, bebida_descricao, bebida_preco, bebida_foto) VALUES
('Refrigerantes','Coca-cola, Fanta laranja, Sprite 350ml: Bem geladinhos para refrescar o calor! Acompanha um limãozinho?', '8.00','refrigerantes.jpg');


/*Criação da tabela de acompanhamentos*/
CREATE TABLE qtop_acompanhamentos (
    acomp_id SERIAL,
    acomp_nome VARCHAR(150) NOT NULL,
    acomp_descricao VARCHAR(250) NOT NULL,
    acomp_preco NUMERIC (10, 2) NOT NULL,
    acomp_foto VARCHAR(150) NOT NULL
);
/*Inserção de itens de acompanhamento*/
INSERT INTO qtop_acompanhamentos (acomp_nome, acomp_descricao, acomp_preco, acomp_foto) VALUES
('Camarão Empanado', 'O melhor camarão da região! Fresquinhos, limpos, empanados e fritos na hora!!', '85.00', 'camarao.jpg');

INSERT INTO qtop_acompanhamentos (acomp_nome, acomp_descricao, acomp_preco, acomp_foto) VALUES
('Batata-Frita', 'As melhores batatas da região, não tem nada igual! Quer provar?!', '12.50', 'batata-frita.jpg');

INSERT INTO qtop_acompanhamentos (acomp_nome, acomp_descricao, acomp_preco, acomp_foto) VALUES
('Cebolas Empanadas', 'Cebolas fresquinhas empanadas e fritas na hora!', '18.50', 'onion-rings.jpg');

/*Criação da tabela de sobremesas*/
CREATE TABLE qtop_sobremesas (
    sobrem_id SERIAL,
    sobrem_nome VARCHAR(150) NOT NULL,
    sobrem_descricao VARCHAR(250) NOT NULL,
    sobrem_preco NUMERIC (10, 2) NOT NULL,
    sobrem_foto VARCHAR(150) NOT NULL
);
/*Inserção de sobremesas*/
INSERT INTO qtop_sobremesas (sobrem_nome, sobrem_descricao, sobrem_preco, sobrem_foto) VALUES
('Sorvetes', 'Sabore chocolate, limão, morango, maracujá e pistache! Ou faça sua combinação ;)', '12.50', 'sorvete.jpg');

INSERT INTO qtop_sobremesas (sobrem_nome, sobrem_descricao, sobrem_preco, sobrem_foto) VALUES
('Mousse', 'Que tal uma sobremesa gourmet? Experimente o nosso mousse de chocolate com limão', '15.00', 'mousse.jpg');

INSERT INTO qtop_sobremesas (sobrem_nome, sobrem_descricao, sobrem_preco, sobrem_foto) VALUES
('Bolo Floresta Negra', 'Pedaço de bolo com chocolate de alta qualidade e cerejas fresquinhas! Quer provar?', '10.00', 'bolo.jpg');
