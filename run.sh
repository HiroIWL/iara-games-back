#!/bin/bash

# Verifica se o Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "Python não está instalado. Por favor, instale o Python para continuar."
    exit 1
fi

# Verifica se o ambiente virtual já existe
if [ -d "venv" ]; then
    echo "O ambiente virtual já existe."
    echo "Ativando o ambiente virtual..."
    source venv/bin/activate
else
    echo "Criando ambiente virtual na pasta venv..."
    python3 -m venv venv

    echo "Ativando o ambiente virtual..."
    source venv/bin/activate

    echo "Instalando dependências..."
    pip install -r requirements.txt
fi

echo "Rodando a aplicação..."
uvicorn main:app --reload
