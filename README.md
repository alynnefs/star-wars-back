[![Build Status](https://app.travis-ci.com/alynnefs/star-wars-back.svg?branch=main)](https://app.travis-ci.com/alynnefs/star-wars-back)

# Star Wars API (back)

O projeto consiste em buscar um elemento e três recomendações de acordo com a pesquisa feita. Caso mais de um elemento seja encontrado, terá três recomendações para cada um deles.

## Executando com Docker

Para criar a imagem do docker, execute o seguinte comando na raiz do projeto:

```
docker image build -t sw_back .
```

O resultado deverá ser

![](https://i.imgur.com/GrkIcFN.png)


Após criada, execute o container com:

```
docker container run -d -p 5000:5000 sw_back
```

Para ver se o container está sendo executado, basta usar o comando `docker container ls`. A saída deverá ser parecida com essa:

![](https://i.imgur.com/YVIE04R.png)


## Executando localmente

### Especificações usadas no desenvolvimento

- Sistema operacional: Ubuntu 20.04.5 LTS
- Docker: 20.10.21, build baeda1f
- Python: 3.9
- NPM: 9.2.0
- Vue/cli: 5.0.8


### Como executar

Para criar o ambiente virtual, execute:

```
virtualenv --python=python3.9 .venv
```

Para ativá-lo:

```
source .venv/bin/activate
```

Para instalar as dependências:

```
pip install -r requirements.txt
```

Com tudo instalado, basta executar o projeto na pasta raiz:

```
flask --app app/main run
```

### Usando o front

> O front-end deste projeto e como executá-lo pode ser visto [neste link](https://github.com/alynnefs/star-wars-front).

No navegador, entre no link http://127.0.0.1:8080. O último número do IP pode mudar.

Você pode pesquisar pelo nome de um personagem, planeta, nave ou filme e selecionar se quer fazer uma pesquisa específica, por exemplo "Leia" e "people".

![image](https://user-images.githubusercontent.com/17454743/215167527-ae3e047d-c348-411d-a116-985db73193b6.png)

> O tempo de resposta está alto, tem uma sugestão de melhoria no fim do documento.

O retorno deverá ser:

![image](https://user-images.githubusercontent.com/17454743/215167656-32f8b63c-b089-4d22-8a4e-e28432786df6.png)



Caso você não saiba em qual categoria sua pesquisa se encaixa, você pode pesquisar em todas. Por exemplo, "R2-D2" e "all".

![image](https://user-images.githubusercontent.com/17454743/215167787-6dd5afb5-ba5b-461b-816b-f062a855c9cb.png)

O retorno deverá ser:

![image](https://user-images.githubusercontent.com/17454743/215167907-75025675-9334-4de9-ba00-6602bd7bc059.png)


### Usando o cURL

Exemplos de requisições a serem feitas no terminal, com o container executando:

```
curl 127.0.0.1:5000/people/luke
curl 127.0.0.1:5000/films/A%20New%20Hope # %20 é por causa do espaço entre palavras
curl 127.0.0.1:5000/planets/tatooine
curl 127.0.0.1:5000/starships/CR90%20corvette
curl 127.0.0.1:5000/all/naboo
```

## Testes

### Testes no Travis CI

Para ver os testes que foram executados no Travis, basta clicar [neste link](https://app.travis-ci.com/alynnefs/star-wars-back) ou no botão que está no topo deste arquivo. Sempre que um commit for adicionado na branch main, o Travis irá rodar os testes novamente. Nele é possível ver o histórico da execução dos testes:

![](https://i.imgur.com/qrCNrZs.png)

Caso ocorra algum erro, ele informa qual é. Por exemplo, quando mudei do poetry para o pip, esqueci de mudar o `.travis.yml`. O resultado foi esse:

![](https://i.imgur.com/qK0vQu4.png)


### Rodando os testes localmente

Considerando que você está no ambiente virtual e com as dependências instaladas, basta executar:

```
pytest tests/*
```

O resultado será:

![](https://i.imgur.com/VL0mMIO.png)

> Lembrando que, por causa das requisições, os testes irão demorar um pouco

Este comando irá executar todos os testes de todos os arquivos que estão dentro desta pasta. Por fazer requisições ao SWAPI, vai demorar mais do que o desejado. Sendo assim, caso queira executar apenas um dos testes, você pode usar este comando como exemplo:

```
pytest tests/tests_films.py::test_get_films
```

O resultado será:

![](https://i.imgur.com/Smff2sU.png)

### Cobertura de testes

Para verificar a cobertura de testes, basta executar o comando `coverage run -m pytest tests/*` na raiz do projeto. Ele criará uma pasta chamada `htmlcov` e, dentro dela, você só precisa abrir o arquivo `index.html`. A página estará assim:

![](https://i.imgur.com/8QFhwOO.png)

Se você clicar em qualquer um dos arquivos, poderá ver as linhas que estão cobertas.

![](https://i.imgur.com/8YGK11I.png)


## Pontos de melhoria

### Sobre performance

Como cada pesquisa consulta mais três elementos, a resposta está demorando muito. Uma possível solução é armazenar os dados em cache, já que as recomendações não mudam muito. E por falar em recomendações, o sistema desenvolvido obtém os mesmos 3 itens relacionados, não havendo nenhum tipo de inteligência artificial por trás.

### Sobre os testes

Idealmente os testes unitários devem funcionar sem internet, e não se comunicar com uma API. Entretanto, como o desafio era sobre usar o [SWAPI](https://swapi.dev/), era necessário confirmar que esta comunicação estava funcionando.
