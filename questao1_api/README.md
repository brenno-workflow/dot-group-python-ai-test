# Questão 1 - API REST para Biblioteca Virtual

Esta pasta contém a implementação da Questão 1 da avaliação técnica da Dot Group para a vaga de Desenvolvedor Backend Python com foco em IA.

O objetivo desta questão é desenvolver uma API simples que permita cadastrar e consultar livros em uma biblioteca virtual.

A solução foi implementada com Django, Django REST Framework e SQLite.

## Tecnologias Utilizadas

- Python 3.12
- Django 5.2
- Django REST Framework
- SQLite

## Funcionalidades

- Cadastro de livros.
- Consulta de livros cadastrados.
- Pesquisa por título.
- Pesquisa por autor.
- Pesquisa por data de publicação.
- Pesquisa por resumo.
- Retorno das consultas sempre em formato de lista.
- Campos de controle para criação, atualização e status ativo do registro.

## Estrutura

```text
questao1_api/
│
├── manage.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── library/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── tests.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    └── services/
        └── serializers.py
```

## Modelo de Dados

O modelo `Book` representa um livro cadastrado na biblioteca virtual.

Campos:

- `id`: identificador único do livro.
- `title`: título do livro.
- `author`: autor do livro.
- `publication_date`: data de publicação.
- `summary`: resumo do livro.
- `created_at`: data e hora em que o registro foi criado.
- `updated_at`: data e hora da última atualização.
- `is_active`: indica se o livro está ativo para consulta.

## Endpoints

### Criar Livro

```http
POST /api/books/create/
```

Endpoint responsável pelo cadastro de livros.

Exemplo de requisição:

```json
{
  "title": "Python Fluente",
  "author": "Luciano Ramalho",
  "publication_date": "2023-01-01",
  "summary": "Livro sobre recursos avançados da linguagem Python."
}
```

Exemplo de resposta:

```json
{
  "id": 1,
  "title": "Python Fluente",
  "author": "Luciano Ramalho",
  "publication_date": "2023-01-01",
  "summary": "Livro sobre recursos avançados da linguagem Python.",
  "created_at": "2026-08-07T00:22:19.059853Z",
  "updated_at": "2026-08-07T00:22:19.059853Z"
}
```

### Pesquisar Livros

```http
GET /api/books/search/
```

Endpoint responsável pela consulta de livros cadastrados.

A busca pode ser feita sem filtros, retornando todos os livros ativos:

```http
GET /api/books/search/
```

Também é possível filtrar por campos específicos:

```http
GET /api/books/search/?author=Luciano
GET /api/books/search/?title=Python
GET /api/books/search/?publication_date=2023-01-01
GET /api/books/search/?summary=avançados
```

Exemplo de resposta com múltiplos resultados:

```json
[
  {
    "id": 1,
    "title": "Python Fluente",
    "author": "Luciano Ramalho",
    "publication_date": "2023-01-01",
    "summary": "Livro sobre recursos avançados da linguagem Python.",
    "created_at": "2026-08-07T00:22:19.059853Z",
    "updated_at": "2026-08-07T00:22:19.059853Z"
  },
  {
    "id": 2,
    "title": "Python para Desenvolvedores",
    "author": "Luciano Ramalho",
    "publication_date": "2024-02-10",
    "summary": "Livro introdutório sobre desenvolvimento com Python.",
    "created_at": "2026-08-07T00:23:02.237238Z",
    "updated_at": "2026-08-07T00:23:02.237238Z"
  }
]
```

Caso nenhum livro seja encontrado, a API retorna uma lista vazia:

```json
[]
```

## Como Executar

A partir da raiz do repositório, entre na pasta da questão:

```bash
cd questao1_api
```

Execute as migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Inicie o servidor:

```bash
python manage.py runserver
```

A aplicação estará disponível em:

```text
http://127.0.0.1:8000/
```

## Como Testar Manualmente

### Criar um livro

Acesse no navegador ou em uma ferramenta como Postman/Insomnia:

```text
http://127.0.0.1:8000/api/books/create/
```

Envie uma requisição `POST` com o seguinte JSON:

```json
{
  "title": "Python Fluente",
  "author": "Luciano Ramalho",
  "publication_date": "2023-01-01",
  "summary": "Livro sobre recursos avançados da linguagem Python."
}
```

### Pesquisar livros

Acesse:

```text
http://127.0.0.1:8000/api/books/search/
```

Ou utilize filtros:

```text
http://127.0.0.1:8000/api/books/search/?author=Luciano
http://127.0.0.1:8000/api/books/search/?title=Python
```

## Exemplo com PowerShell

Criar livro:

```powershell
Invoke-RestMethod `
  -Uri "http://127.0.0.1:8000/api/books/create/" `
  -Method Post `
  -ContentType "application/json" `
  -Body '{
    "title": "Python Fluente",
    "author": "Luciano Ramalho",
    "publication_date": "2023-01-01",
    "summary": "Livro sobre recursos avançados da linguagem Python."
  }'
```

Pesquisar por autor:

```powershell
Invoke-RestMethod `
  -Uri "http://127.0.0.1:8000/api/books/search/?author=Luciano" `
  -Method Get
```

## Decisões Técnicas

A API foi dividida em dois endpoints principais:

- `PostBookView`: responsável exclusivamente pelo cadastro de livros.
- `GetBookView`: responsável pela consulta e filtragem de livros.

A criação utiliza `CreateAPIView` do Django REST Framework, enquanto a pesquisa utiliza `ListAPIView`.

A pesquisa foi implementada com um dicionário de filtros permitidos, evitando repetição excessiva de condicionais e facilitando manutenção futura.

O retorno da consulta é sempre uma lista, mesmo quando apenas um livro é encontrado.

O campo `is_active` permite consultar apenas livros ativos, possibilitando uma estratégia futura de exclusão lógica sem remover registros do banco de dados.

## Banco de Dados

O projeto utiliza SQLite, configurado pelo próprio Django.

Após executar as migrations, o banco é criado automaticamente no arquivo:

```text
questao1_api/db.sqlite3
```

Esse arquivo não precisa ser versionado no GitHub.

## Observações

A interface navegável do Django REST Framework pode ser usada para testar os endpoints diretamente pelo navegador.

No endpoint de criação, o método aceito é `POST`. Ao acessar a URL diretamente pelo navegador com `GET`, a API pode retornar `405 Method Not Allowed`, o que é esperado para esse endpoint.