# Dot Group - Backend Python & AI Technical Challenge

Este repositório contém minha solução para a avaliação técnica de Desenvolvedor Backend Python com foco em IA da Dot Group.

O projeto está organizado por questão, separando a API, o chatbot com IA generativa e a busca semântica com embeddings/vector store.

## Tecnologias Utilizadas

- Python 3.12
- Django 5.2
- Django REST Framework
- SQLite
- LangChain
- OpenAI API
- FAISS

## Estrutura Parcial do Projeto

```text
dot-group-python-ai-test/
│
├── README.md
├── requirements.txt
├── .env.example
│
├── questao1_api/
├── questao2_chatbot/
└── questao3_rag/
```

Cada questão possui sua própria estrutura para facilitar a leitura, execução e manutenção.

---

# Questão 1 — API REST com Django

Implementação de uma API REST para gerenciamento de livros utilizando:

* Django
* Django REST Framework
* SQLite

Funcionalidades implementadas:

* Cadastro de livros
* Consulta de livros
* Busca por título
* Busca por autor
* Testes automatizados dos endpoints

A documentação da API é disponibilizada utilizando os recursos do Django REST Framework.

---

# Questão 2 — Chatbot com IA

Implementação de um chatbot utilizando:

* LangChain
* OpenAI
* Prompt Templates

O chatbot responde perguntas sobre programação em Python utilizando um modelo de linguagem (LLM).

---

# Questão 3 — Busca Semântica

Implementação de um sistema de busca semântica utilizando:

* Embeddings
* FAISS
* LangChain

Os documentos são convertidos em embeddings, armazenados em uma Vector Store e recuperados por similaridade semântica.

# Como Executar

## 1. Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd dot-group-python-ai-test
```

## 2. Criar o ambiente virtual

### Windows

```powershell
python -m venv .venv
```

Ativar o ambiente:

```powershell
.venv\Scripts\Activate.ps1
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

---

# Objetivo

Este projeto foi desenvolvido exclusivamente para fins de avaliação técnica, demonstrando conhecimentos em:

* Desenvolvimento Backend com Python
* Django e Django REST Framework
* APIs REST
* Testes automatizados
* Integração com modelos de linguagem (LLMs)
* LangChain
* Embeddings
* Vector Stores
* Organização de projetos e boas práticas de desenvolvimento
