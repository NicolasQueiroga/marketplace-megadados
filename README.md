# Marketplace - MEGADADOS
## Versão em FastAPI

### Integrantes
- Davi Reis Vieira
- Guilherme Dantas Rameh
- Nicolas Maciel Queiroga

---
### Instruções para ativar a API localmente

1. Clone o repositório com um dos comandos abaixo:
  - ```git clone git@github.com:NicolasQueiroga/marketplace-megadados.git```
  - ```git clone https://github.com/NicolasQueiroga/marketplace-megadados.git```
 
2. Inicie o docker-desktop entrando em seu aplicativo e insira os seguintes comandos:
  - ```docker-compose build```
  - ```docker-compose up```
  
3. E, por último, acesse a url ```http://localhost:8008/docs``` para ter acesso às rotas disponíveis.


---
*Para testar as rotas, basta executar o seguinte comando na raiz do projeto:*
```bash
docker-compose run api pytest
```
