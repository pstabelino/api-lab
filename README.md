# API Lab — HTTP Requests & Retry

Projeto educacional desenvolvido em Python para praticar o consumo de APIs HTTP, tratamento de erros e estratégias de novas tentativas de requisição.

## Tecnologias

- Python 3.10+
- Requests
- HTTP
- JSON

## Funcionalidades

- Realização de requisições HTTP GET
- Definição de timeout
- Tratamento de códigos de erro HTTP
- Tratamento de timeout
- Novas tentativas para falhas temporárias
- Exponential backoff
- Leitura do cabeçalho Retry-After
- Limite máximo de tentativas

## Estrutura

- `main.py`: exemplos de estudos e implementação das funções HTTP
- `requirements.txt`: dependências externas
- `.gitignore`: arquivos que não devem ser versionados

## Como executar

Clone o repositório:

    git clone https://github.com/pstabelino/api-lab.git
    cd api-lab

Crie e ative um ambiente virtual:

    python3 -m venv .venv
    source .venv/bin/activate

Instale as dependências:

    pip install -r requirements.txt

O projeto disponibiliza a função `buscar_com_retry(url)`,
que pode ser importada e utilizada em outros scripts Python.

Exemplo:

    from main import buscar_com_retry

    dados = buscar_com_retry("https://jsonplaceholder.typicode.com/todos/1")
    print(dados)

O exemplo requer conexão com a internet.

## Estratégia de retry

A aplicação realiza até três tentativas de requisição.

Em falhas temporárias, utiliza espera progressiva
(exponential backoff) entre as tentativas.

Quando recebe HTTP 429 com o cabeçalho Retry-After,
utiliza o intervalo informado pelo servidor.

## Objetivo educacional

Praticar integração com serviços externos, tratamento de
exceções, códigos HTTP, timeout e resiliência de aplicações.

## Autor

Paulo Henrique
