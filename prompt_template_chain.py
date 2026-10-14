from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

# 1 Create a dynamic prompt with a variable
prompt = PromptTemplate.from_template("Write a short story about a person named {name} who loves {hobby}.")

llm = ChatOllama(model="llama3.2")

parser = StrOutputParser()

chain = prompt | llm | parser

result = chain.invoke({"name": "Lena", "hobby": "skydiving"})

print(result)