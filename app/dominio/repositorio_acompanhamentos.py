from repositorios import repositorio_acompanhamentos

class servico_acompanhamentos:
    def __init__(self, repository):
        self.repository = repository

    def adicionar_acompanhamento(self, dados_acompanhamento):
        # Validar os dados, aplicar regras de negócio, etc.

        # Salvar o acompanhamento no banco de dados
        self.repository.adicionar_acompanhamento(dados_acompanhamento)

