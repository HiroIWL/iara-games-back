# Iaragames

Este é o repositório do projeto **iaragames**, desenvolvido como parte do curso da FIAP. O objetivo deste projeto é criar uma loja de jogos nacionais, oferecendo uma plataforma onde usuários podem descobrir e adquirir jogos desenvolvidos no Brasil.

## Estrutura do Projeto

O projeto utiliza as seguintes tecnologias e bibliotecas principais:

- **FastAPI** para o desenvolvimento da API.
- **SQLModel** para gerenciamento do banco de dados.
- **SQLite** como banco de dados local.
- **bcrypt** para hashing de senhas e autenticação segura.
- **PyJWT** para geração e validação de tokens de autenticação.

## Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina. O projeto utiliza um ambiente virtual para gerenciar dependências.

## Configuração e Execução

1. Clone o repositório do projeto:

   ```bash
   git clone https://github.com/HiroIWL/iara-games-back
   cd iara-games-back
   ```

2. Execute o script `setup.bat` (Windows) ou configure o ambiente virtual manualmente para instalar as dependências e iniciar o servidor.

   - No Windows, utilize o comando:
     ```cmd
     ./run.bat
     ```
   - Este script verifica a instalação do Python, cria e ativa o ambiente virtual, instala as dependências e inicia o servidor.

3. Acesse a aplicação no navegador em `http://127.0.0.1:8000`.

## Endpoints Principais

- **/register/**: Cadastro de usuários
- **/login/**: Autenticação e geração de token JWT
- **/users/**: Listagem de usuários cadastrados (para uso administrativo)
- **/**: Endpoint básico para verificação da execução da API

## Observações

- O projeto utiliza `CORSMiddleware` para permitir o acesso da API a partir de qualquer origem. No ambiente de produção, recomenda-se limitar as origens permitidas.
- Tokens JWT são gerados durante a autenticação do usuário e devem ser incluídos nas requisições autenticadas.

## Estrutura do Banco de Dados

O banco de dados é inicializado automaticamente ao iniciar a aplicação, criando as tabelas necessárias para armazenar informações dos usuários e dos jogos.
