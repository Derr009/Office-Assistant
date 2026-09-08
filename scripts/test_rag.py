from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

query = "How many casual leaves can an employee take?"

results = db.similarity_search(query, k=3)

for i, result in enumerate(results, 1):
    print(f"\n--- Result {i} ---")
    print(result.page_content)