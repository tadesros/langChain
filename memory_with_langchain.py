from langchain_ollama import ChatOllama  
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

#Step1: Load local LLaMa Model
llm = ChatOllama(model="llama3.2", temperature=0)

#Step2: Prompt with placeholder for chat history
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{input}")
])

#Step3: Create a chat history object
base_chain = prompt | llm

#Step4: Session based message history manager
session_store = {}

def get_session_history(session_id: str):
    if session_id not in session_store:
        session_store[session_id] = InMemoryChatMessageHistory()
    return session_store[session_id]

#5 Wrap the base chain with memory login
chat_chain = RunnableWithMessageHistory(
    base_chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
)

# 6 Simple Terminal Loop
print("Chat with LLaMa (with memory). Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Exiting chat...")
        break


    result = chat_chain.invoke(
        {"input": user_input}, 
        config={"configurable" : {"session_id": "local_user"}}
    )
    
    print("LLaMa: ", result.content)

