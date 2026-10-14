
import re

from langchain_ollama import ChatOllama

def calculator(expression: str) -> str:
    try:
        # Evaluate the expression safely        
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"

llm = ChatOllama(model="llama3.2")

#Prompt style for ReAct
prompt = """You are a helpful assistant who uses tools. 
Available tool: calculator[expression]

Respond using this format:
Thought: ...
Action: calculator[2 + 2]
Observation: ...
Final Answer: ...
"""

user_input = input("Ask a math question:")
response = llm.invoke(prompt + f"Question: {user_input}")
response_text = response.content

print("--- Raw Model Response ---")
print(response_text)

# Extract the action from the model's response
match = re.search(r"Action: calculator\[(.*?)\]", response_text)


if match:
    expression = match.group(1)
    result = calculator(expression)
    print("--- Tool Execution ---")
    print(f"calculator({expression}) = {result}")
else:
    print("No valid tool call found.")


    