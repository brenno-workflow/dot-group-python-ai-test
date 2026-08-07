# Questão 2 - Chatbot com IA Generativa

Esta pasta contém a implementação da Questão 2 da avaliação técnica da Dot Group para a vaga de Desenvolvedor Backend Python com foco em IA.

O objetivo desta questão é desenvolver um chatbot capaz de responder perguntas relacionadas à programação em Python utilizando um Modelo de Linguagem (LLM) integrado através do LangChain.

A solução foi implementada utilizando LangChain e o modelo Gemini da Google.

## Tecnologias Utilizadas

* Python 3.12
* LangChain
* LangChain Google Generative AI
* Google Gemini
* Python Dotenv

## Funcionalidades

* Recebe perguntas do usuário via terminal.
* Utiliza o LangChain para gerenciamento do fluxo de conversação.
* Integração com o modelo Gemini através da API do Google AI Studio.
* Respostas especializadas sobre programação em Python.
* Prompt personalizado para orientar o comportamento do assistente.
* Encerramento da conversa através dos comandos `sair`, `exit` ou `quit`.

## Estrutura

```text
questao2_chatbot/
│
├── chatbot.py
├── .env
├── .env.example
└── README.md
```

## Funcionamento

O chatbot utiliza uma cadeia (`Chain`) composta por:

* Um **System Prompt**, responsável por definir o comportamento do assistente.
* Um **Human Prompt**, que recebe a pergunta informada pelo usuário.
* O modelo **Gemini**, responsável por gerar a resposta.

Fluxo simplificado:

```text
Usuário
    │
    ▼
Pergunta via terminal
    │
    ▼
ChatPromptTemplate
    │
    ▼
Google Gemini
    │
    ▼
Resposta ao usuário
```

## Prompt do Assistente

O chatbot foi configurado para atuar como um especialista em programação Python.

As respostas seguem as seguintes diretrizes:

* Explicações claras e objetivas.
* Linguagem didática.
* Inclusão de exemplos de código quando apropriado.

## Como Executar

A partir da raiz do repositório, entre na pasta da questão:

```bash
cd questao2_chatbot
```

Certifique-se de que o ambiente virtual esteja ativado e instale as dependências caso ainda não tenha feito:

```bash
pip install -r ../requirements.txt
```

Crie um arquivo `.env` utilizando o `.env.example` como referência.

Exemplo:

```text
GOOGLE_API_KEY=sua_chave_da_api
GEMINI_MODEL=gemini-2.5-flash
```

Execute o chatbot:

```bash
python chatbot.py
```

## Exemplo de Utilização

Ao iniciar a aplicação será exibido:

```text
Chatbot Python iniciado.
Digite uma pergunta sobre Python ou 'sair' para encerrar.
```

Pergunta:

```text
Você: Como criar uma lista em Python?
```

Resposta esperada:

```text
Chatbot:

Em Python, listas são coleções ordenadas e mutáveis utilizadas para armazenar múltiplos valores.

Exemplo:

numeros = [1, 2, 3, 4]

Você pode acessar elementos utilizando índices:

print(numeros[0])

Também é possível adicionar novos elementos utilizando o método append():

numeros.append(5)
```

Para encerrar a aplicação:

```text
Você: sair
```

## Variáveis de Ambiente

As credenciais da API não são armazenadas diretamente no código.

O projeto utiliza um arquivo `.env` para configuração das variáveis de ambiente.

Variáveis utilizadas:

| Variável         | Descrição                                  |
| ---------------- | ------------------------------------------ |
| `GOOGLE_API_KEY` | Chave de acesso da API do Google AI Studio |
| `GEMINI_MODEL`   | Modelo Gemini utilizado pelo chatbot       |

## Decisões Técnicas

Foi utilizada a biblioteca LangChain para abstrair a comunicação com o modelo de linguagem, simplificando a criação do fluxo conversacional.

O prompt foi separado da pergunta do usuário através do `ChatPromptTemplate`, permitindo definir previamente o comportamento esperado do assistente.

As configurações sensíveis, como a chave da API e o modelo utilizado, são carregadas por meio de variáveis de ambiente utilizando a biblioteca `python-dotenv`.

O chatbot foi desenvolvido para execução em terminal, conforme solicitado na avaliação técnica, mantendo uma implementação simples, objetiva e de fácil utilização.

## Observações

O modelo Gemini utilizado pode possuir configurações internas de geração de texto. Em alguns modelos, parâmetros como `temperature` podem ser ignorados por utilizarem configurações de amostragem fixas, comportamento informado pela própria biblioteca durante a execução.

Para utilizar outro modelo Gemini, basta alterar a variável `GEMINI_MODEL` no arquivo `.env`, sem necessidade de modificar o código-fonte.
