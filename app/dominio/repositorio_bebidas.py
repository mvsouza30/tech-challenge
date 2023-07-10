from repositorios import repositorio_bebidas

class servico_bebidas:
    def __init__(self, repository):
        self.repository = repository

    def adicionar_acompanhamento(self, dados_acompanhamento):
        # Validar os dados, aplicar regras de negócio, etc.

        # Salvar o acompanhamento no banco de dados
        self.repository.adicionar_bebida(dados_bebida)

