# Usa a imagem base do Python 3.9
FROM python:3.9

# Define o diretório de trabalho no container
WORKDIR /app

# Copia os arquivos da aplicação para o diretório de trabalho
COPY . .

# Instala as dependências da aplicação
RUN pip install -r requirements.txt

# Expõe a porta 5000 para acessar a aplicação
EXPOSE 5000

# Define o comando para iniciar a aplicação
CMD ["python", "app.py"]
