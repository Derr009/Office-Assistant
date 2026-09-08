from pathlib import Path

from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma


DATA_PATH = Path("data/knowledge")
CHROMA_PATH = "chroma_db"


def ingest_documents():
    # 1. Load PDFs
    loader = PyPDFDirectoryLoader(str(DATA_PATH))
    documents = loader.load()

    print(f"Loaded {len(documents)} pages")

    # 2. Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    # 3. Create embeddings
    embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

    # 4. Store vectors in ChromaDB
    Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_PATH
    )

    print("Documents successfully stored in ChromaDB")


if __name__ == "__main__":
    ingest_documents()