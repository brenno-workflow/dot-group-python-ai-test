# Questão 3 - Busca Semântica com Embeddings e FAISS

Esta pasta contém a implementação da Questão 3 da avaliação técnica da Dot Group para a vaga de Desenvolvedor Backend Python com foco em IA.

O objetivo desta questão é implementar um sistema de busca semântica utilizando embeddings e uma Vector Store.

A solução foi desenvolvida utilizando LangChain, Sentence Transformers e FAISS.

## Tecnologias Utilizadas

- Python 3.12
- LangChain
- Sentence Transformers
- FAISS
- python-dotenv

## Funcionalidades

- Leitura automática de documentos `.txt`.
- Divisão dos documentos em chunks.
- Geração de embeddings utilizando Sentence Transformers.
- Armazenamento dos embeddings em uma Vector Store FAISS.
- Criação automática do índice caso ele ainda não exista.
- Busca semântica baseada em similaridade entre embeddings.
- Exibição dos documentos mais relevantes para a consulta realizada.

## Estrutura

```text
questao3_rag/
│
├── build_vector_store.py
├── search.py
│
├── documents/
│   ├── django.txt
│   ├── faiss.txt
│   ├── fastapi.txt
│   ├── langchain.txt
│   └── python.txt
│
└── vector_store/
    ├── index.faiss
    └── index.pkl
```

## Funcionamento

A aplicação segue o seguinte fluxo:

1. Carrega todos os arquivos `.txt` presentes na pasta `documents`.
2. Divide os documentos em pequenos trechos (chunks).
3. Gera embeddings para cada chunk utilizando o modelo `sentence-transformers/all-MiniLM-L6-v2`.
4. Armazena os embeddings em uma Vector Store utilizando FAISS.
5. Recebe consultas do usuário.
6. Converte a consulta em embedding.
7. Recupera os documentos mais semelhantes utilizando busca vetorial.

Caso o índice ainda não exista, ele é criado automaticamente antes da primeira consulta.

## Como Executar

A partir da raiz do repositório:

```bash
cd questao3_rag
```

Caso deseje gerar manualmente a Vector Store:

```bash
python build_vector_store.py
```

Para iniciar a busca semântica:

```bash
python search.py
```

## Como Testar

Ao executar o sistema será exibido:

```text
Busca Semântica iniciada.
Digite uma pergunta ou 'sair' para encerrar.
```

Exemplos de consultas:

```text
Como criar APIs em Python?

Como armazenar vetores?

Qual framework possui documentação automática?

O que é LangChain?

Para que serve o Django?
```

Exemplo de saída:

```text
Resultados encontrados:

1. Documento: fastapi.txt
Distância: 0.8746

Conteúdo:
FastAPI é um framework moderno para criação de APIs REST.
É baseado em type hints.
Possui documentação automática.
É muito utilizado em aplicações de IA.
```

## Processo de Geração dos Embeddings

Os documentos são carregados utilizando o `DirectoryLoader` do LangChain.

Após o carregamento, o `RecursiveCharacterTextSplitter` divide cada documento em pequenos blocos para melhorar a qualidade da indexação.

Os embeddings são gerados utilizando o modelo:

```text
sentence-transformers/all-MiniLM-L6-v2
```

Esse modelo produz vetores numéricos capazes de representar o significado semântico do texto.

Os vetores são então armazenados utilizando a biblioteca FAISS, permitindo buscas extremamente rápidas por similaridade.

## Decisões Técnicas

A solução foi dividida em dois módulos principais:

- `build_vector_store.py`: responsável pela criação da Vector Store.
- `search.py`: responsável por realizar as buscas semânticas.

Durante a execução da busca, a aplicação verifica automaticamente se o índice FAISS já existe.

Caso não exista, ele é criado automaticamente a partir dos documentos presentes na pasta `documents`.

Essa abordagem simplifica a execução da aplicação e evita que o usuário precise executar etapas adicionais antes da primeira utilização.

## Observações

A busca implementada é semântica, ou seja, os resultados são recuperados com base na similaridade de significado entre a consulta e os documentos armazenados.

Dessa forma, não é necessário que a pesquisa contenha exatamente as mesmas palavras presentes nos documentos para que resultados relevantes sejam encontrados.

Os documentos utilizados nesta implementação possuem caráter demonstrativo e abordam conceitos relacionados ao ecossistema Python e Inteligência Artificial.