# Instala dependências
install:
	pip install -r requirements.txt

# Executa a aplicação
run:
	python app.py

# Limpa arquivos temporários
clean:
	rm -rf __pycache__
