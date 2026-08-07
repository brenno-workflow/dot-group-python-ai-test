import os

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# Carregar o .env
load_dotenv()

# Buscar variaveis
API_KEY = os.getenv("GOOGLE_API_KEY")
AI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.6-flash")

# Main
def main():
    """
    Executa o chatbot no terminal.
    A execução é encerrada quando o usuário digita 'sair', 'exit' ou 'quit'.
    """

    # TryCath
    try:

        # Criar chatbot
        chatbot = create_chatbot()
        print("Chatbot Python iniciado.")
        print("Digite uma pergunta sobre Python ou 'sair' para encerrar.\n")

        # Loop
        while True:
            question = input("Você: ")

            # Encerrar pelo terminal
            if question.lower().strip() in ["sair", "exit", "quit"]:
                print("Chatbot encerrado.")
                break

            # Envia a pergunta
            response = chatbot.invoke({"question": question})

            # Buscar conteudo
            content = response.content

            # Arrumar resposta em linhas corretas
            if isinstance(content, list):
                text = "".join(item["text"] for item in content if isinstance(item, dict) and item.get("type") == "text")
            else: text = content

            # Respota
            print(f"\nChatbot:\n{text}\n")

    # Exception
    except Exception as e:
        print(f"\nErro: {str(e)}\n")

# Criar chatbot
def create_chatbot():
    """
    Cria e configura o fluxo principal do chatbot.
    """

    # TryCath
    try:

        # Instancia o Gemini
        llm = ChatGoogleGenerativeAI(model=AI_MODEL, google_api_key=API_KEY)

        # Comortamento do chat
        system = "Você é um assistente especialista em programação Python. Responda de forma clara, didática e objetiva. Sempre que fizer sentido, inclua exemplos de código."
        prompt = ChatPromptTemplate.from_messages([("system", system), ("human", "{question}"),])

        # Criar chain
        return prompt | llm

    # Exception
    except Exception as e:
        raise RuntimeError(f"Erro ao criar o chatbot: {e}")

# Iniciar chatbobt
if __name__ == "__main__":
    main()