from app.agents.agent import ask_agent


print(ask_agent(
    "What is the leave policy?"
))

print(ask_agent(
    "How many leaves do I have?",
    "EMP001"
))

print(ask_agent(
    "What is the leave policy and how many leaves do I have?",
    "EMP001"
))