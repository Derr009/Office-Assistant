from app.agents.router import route_question

questions = [
    "What is the leave policy?",
    "How many leaves do I have?",
    "What is the work from home policy?",
    "Show me my laptop details"
    "What is the leave policy and how many leaves do I have?"
]

for question in questions:
    print(question, "→", route_question(question))