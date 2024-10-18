# Makefile

# Regra para instalar as dependências
install:
    pip install -r requirements.txt

# Regra para rodar os testes
test:
    pytest

# Regra para rodar a aplicação
run:
    python app.py
