# Imagem base
FROM python:3.9

# Definir diretório de trabalho
WORKDIR /app

# Copiar os arquivos de código-fonte
COPY ./app /app

# Instalar as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta do aplicativo Flask
EXPOSE 5000

# Configurando variavel de ambiente
ENV PYTHONPATH "${PYTHONPATH}:/app"

# Comando para executar a aplicação Flask
CMD ["python", "app.py"]

