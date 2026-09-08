from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_chroma import Chroma

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

llm = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0,
    num_predict=200
)


def ask_policy_question(question):
    results = db.similarity_search(question, k=3)

    context = "\n\n".join(
        result.page_content for result in results
    )

    prompt = f"""
You are DT's employee assistant.

Answer the employee's question using ONLY the policy information
provided below.

If the answer is not present in the policy, say:
"I couldn't find that information in the company policies."

Policy information:
{context}

Employee question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content