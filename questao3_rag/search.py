import os

from pathlib import Path

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from build_vector_store import create_vector_store

# Buscar variaveis
BASE_DIR = Path(__file__).resolve().parent
VECTOR_STORE_DIR = BASE_DIR / "vector_store"
FAISS_INDEX = "vector_store/index.faiss"
FAISS_METADATA = "vector_store/index.pkl"

# Main
def main():
    """
    Realiza buscas semânticas utilizando a Vector Store criada anteriormente.
    """

    # TryCath
    try:

        print("Verificando se existe uma Vector Store...")

        # Verificar se existe vetores
        if not (os.path.exists(FAISS_INDEX) and os.path.exists(FAISS_METADATA)):
            print("Vector Store não encontrada.")
            print("Criando índice...")
            create_vector_store()
        else:
            print("Vector Store encontrada.")

        print("Carregando variáveis de ambiente...")

        # Criar embeddings
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

        # Buscar indices
        vector_store = FAISS.load_local(str(VECTOR_STORE_DIR), embeddings, allow_dangerous_deserialization=True)

        print("\nBusca Semântica iniciada.")
        print("Digite uma pergunta ou 'sair' para encerrar.\n")

        # Loop
        while True:
            query = input("Consulta: ").strip()

            # Sair
            if query.lower() in ["sair", "exit", "quit"]:
                print("Busca encerrada.")
                break

            # Resultado
            results = vector_store.similarity_search_with_score(query, k=3)
            if not results: print("\nNenhum documento encontrado.\n")
            else: print("\nResultados encontrados:\n")

            # Verificar
            for index, (document, score) in enumerate(results, start=1):
                filepath = document.metadata["source"]
                filename = os.path.basename(filepath)
                print(f"{index}. Documento: {filename}, Caminho: {filepath}")
                print(f"Score: {score:.4f}")
                print("Conteúdo:")
                print(document.page_content[:250])
                print("-" * 60)

    except Exception as e:
        print(f"Erro ao fazer a busca RAG:\n{e}")

if __name__ == "__main__":
    main()