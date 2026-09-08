from app.rag.rag_chain import llm, db


question = "How many casual leaves can an employee take?"

results = db.similarity_search(question, k=3)

context = "\n\n".join(
    result.page_content for result in results
)

prompt = f"""
You are DT's employee assistant.

Answer the question using ONLY the policy information below.

Policy information:
{context}

Question:
{question}
"""

response = llm.invoke(prompt)

print("\nRAW RESPONSE:")
print(response)

print("\nCONTENT:")
print(response.content)

print("\nADDITIONAL KWARGS:")
print(response.additional_kwargs)