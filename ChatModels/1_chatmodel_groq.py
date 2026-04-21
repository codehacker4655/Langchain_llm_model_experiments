from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()


model=ChatGroq(model="qwen/qwen3-32b",temperature=1.5,max_completion_tokens = 300)
#max_completion_tokens means it defines how many output tokens will generate

result= model.invoke("write a 5 line poem on cricket")

print(result.content)#it will only gives answer