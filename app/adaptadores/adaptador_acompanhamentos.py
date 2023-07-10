from flask import request

class recebe_info_acompanhamentos:
    @staticmethod
    def from_request():
        titulo = request.form.get('titulo')
        descricao = request.form.get('descricao')
        preco = float(request.form.get('preco'))
        foto = request.files.get('foto')
        # Processar a imagem e salvá-la em algum diretório

        return {
            'titulo': titulo,
            'descricao': descricao,
            'preco': preco,
            'foto': foto.filename  # Nome do arquivo da imagem
        }

