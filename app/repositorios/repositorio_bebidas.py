class repositorio_bebidas:
    def adicionar_bebida(self, nome, descricao, preco, foto):
        # Lógica para adicionar o acompanhamento no banco de dados
        # Aqui você pode usar uma biblioteca de acesso ao banco de dados, como SQLAlchemy
        # ou executar consultas SQL diretamente

        # Exemplo de código para adicionar o acompanhamento no banco de dados
        acompanhamento = Acompanhamento(nome=nome, descricao=descricao, preco=preco, foto=foto)
        db.session.add(acompanhamento)
        db.session.commit()

