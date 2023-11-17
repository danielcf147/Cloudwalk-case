# Integando Django a etherium blockchain

Para inciar este projeto, é necessário instalar as dependências, que serão utilizadas nos testes. Portanto utilize o comando abaixo para instalar tais dependências:

````
pip install -r requirements.txt
````
Antes de rodar a API é necessario configurar o arquivo no diretorio site-packages/parsimonious/expressions.py e mudar a linha que diz from inspect import getargspec para from inspect import getfullargspec
````
````
Para rodar a api deve se digitar:

````
python manage.py runserver
````

A blockchain privada usada foi Ganache Etherium - https://trufflesuite.com/ganache/


# **Sobre as rotas**


````
Rotas Transaction:
POST: /api/transaction/ - {Parametros: sender(tipo string), newName(tipo string), address(tipo string)}
GET: /api/transaction/
````
````
Rotas Smart Contract:
POST: /api/smart-contract/ - {Parametros: sender(tipo string), registration(tipo string), age(tipo number), isAdm(tipo boolean), password(tipo string)}
GET: /api/smart-contract/
````
