# Dot Group - Backend Python & AI Technical Challenge

Este repositório contém minha solução para a avaliação técnica da Dot Group para a vaga de **Desenvolvedor Backend Python com foco em IA**.

A solução foi desenvolvida utilizando boas práticas de desenvolvimento, organização de código e documentação. Cada questão foi implementada de forma independente para facilitar a execução, manutenção e avaliação do projeto.

```md
## Índice

- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Estrutura do Projeto](#estrutura-parcial-do-projeto)
- [Questão 1 — API REST](#questão-1--api-rest-com-django)
- [Questão 2 — Chatbot com IA](#questão-2--chatbot-com-ia)
- [Questão 3 — Busca Semântica](#questão-3--busca-semântica)
- [Como Executar](#como-executar)
- [Objetivo](#objetivo)
```

## Tecnologias Utilizadas

- Python 3.12
- Django 5.2
- Django REST Framework
- SQLite
- LangChain
- Google Gemini API
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
* Google Gemini
* Prompt Templates
* Python Dotenv

O chatbot responde perguntas sobre programação em Python utilizando um Large Language Model (LLM) integrado ao LangChain.

**Observação:** Embora o enunciado utilize o GPT-4 da OpenAI como exemplo de LLM, a solução foi implementada utilizando o Google Gemini, integrado ao LangChain, mantendo a mesma arquitetura e atendendo aos requisitos propostos para integração com um modelo de linguagem.

---

# Questão 3 — Busca Semântica

Implementação de um sistema de busca semântica utilizando:

* LangChain
* Embeddings
* FAISS

Os documentos são convertidos em embeddings, armazenados em uma Vector Store e recuperados com base na similaridade semântica entre a consulta do usuário e os documentos indexados.

---

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

## 4. Configurar as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto utilizando o `.env.example` como referência.

Exemplo:

```env
GOOGLE_API_KEY=sua_chave_da_api
GEMINI_MODEL=gemini-3.6-flash
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
