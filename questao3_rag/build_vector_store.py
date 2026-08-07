import os

from pathlib import Path

from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Buscar variaveis
BASE_DIR = Path(__file__).resolve().parent
DOCUMENTS_DIR = BASE_DIR / "documents"
VECTOR_STORE_DIR = BASE_DIR / "vector_store"

# Criar vetores
def create_vector_store():
    """
    Lê os documentos da pasta documents, gera os embeddings
    e salva a Vector Store utilizando FAISS.
    """

    # TryCath
    try:

        print("Carregando documentos...")

        # Ler documentos
        loader = DirectoryLoader(str(DOCUMENTS_DIR), glob="*.txt", loader_cls=TextLoader, loader_kwargs={"encoding": "utf-8"})
        documents = loader.load()

        print(f"{len(documents)} documentos encontrados.")
        print("Dividindo documentos em chunks...")

        # Dividisao recursiva
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_documents(documents)

        print(f"{len(chunks)} chunks gerados.")
        print("Gerando embeddings...")

        # Criar embeddings
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

        print("Criando índice FAISS...")

        # Criar indices
        vector_store = FAISS.from_documents(chunks, embeddings)

        print("Salvando índice...")

        # Salvar 
        os.makedirs(VECTOR_STORE_DIR, exist_ok=True)
        vector_store.save_local(str(VECTOR_STORE_DIR))

        print("\nVector Store criada com sucesso!")

    except Exception as e:
        print(f"Erro ao criar os vetores:\n{e}")

# Main
def main():
    create_vector_store()

if __name__ == "__main__":
    main()