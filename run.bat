@echo off
python --version >nul 2>&1
if errorlevel 1 (
    echo Python não está instalado. Por favor instale o python para continuar.
    exit /b
)

if exist venv (
    echo O ambiente virtual já existe.
    echo Ativando o ambiente virtual...
    call venv\Scripts\activate
) else (
    echo Criando ambiente virtual na pasta venv...
    python -m venv venv


    echo Ativando o ambiente virtual...
    call venv\Scripts\activate

    echo Instalando dependencias...
    pip install -r requirements.txt
)

echo Rodando a aplicação...
uvicorn main:app --reload