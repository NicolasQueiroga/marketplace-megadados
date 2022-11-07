# Marketplace - MEGADADOS

## Versão 2.0.0 utilizando FastAPI

<img src="https://img.shields.io/static/v1?label=Code&message=Python&color=important&style=plastic&labelColor=black&logo=python"/>
<img src="https://img.shields.io/static/v1?label=Code&message=FastAPI&color=important&style=plastic&labelColor=black&logo=FastAPI"/>
<img src="https://img.shields.io/static/v1?label=Container&message=Docker&color=important&style=plastic&labelColor=black&logo=Docker"/>

### Integrantes

- Davi Reis Vieira
- Guilherme Dantas Rameh
- Nicolas Maciel Queiroga

---

### Instruções para ativar a API localmente

1. Clone o repositório com um dos comandos abaixo:

- `git clone git@github.com:NicolasQueiroga/marketplace-megadados.git`
- `git clone https://github.com/NicolasQueiroga/marketplace-megadados.git`

2. Copie o arquivo `.env.sample` para um novo arquivo chamado `.env`:

- `cp .env.sample .env`

3. Inicie um novo `Virtual Environment` da seguinte forma:

- `python -m venv venv`
- `docker-compose up`

4. Ative o `Virtual Environment`

5. Instale as dependências do projeto:

- `pip install -r requirements.txt`

6. Execute o comando abaixo para iniciar a API:

- `uvicorn api.src.main:app --host 0.0.0.0`

7. E, por último, acesse a url `http://localhost:8008/docs` para ter acesso às rotas disponíveis. (OBS: Versão alternativa: `http://localhost:8008/redoc`)

---
