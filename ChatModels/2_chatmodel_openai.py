#open ai chatmodel
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
print(os.getenv("OPENAI_API_KEY"))

model = ChatOpenAI(
    model = 'gpt-5-nano',
    temperature= 1.5,
    max_completion_tokens= 50
)

result = model.invoke("what is the capital of india?")
print(result.content)