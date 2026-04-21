from langchain_cohere import CohereEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()


embeddings = CohereEmbeddings(
    model="embed-english-v3.0",
   )

documents = [
    "Delhi is capital of india",
    "Kolkata is the capital of west bengal",
    "paris is the capital of france"
]

result = embeddings.embed_documents(documents)

print(str(result))