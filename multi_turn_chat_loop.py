from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2")

print("Chat with LLaMa (type 'exit' to quit):")

while True:
  user_input = input("You: ")
  if user_input.lower() == "exit":
    print("Exiting chat...")
    break 

  response = llm.invoke(user_input)
  print("LLaMa: ", response.content)


