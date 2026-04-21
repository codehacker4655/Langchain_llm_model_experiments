from langchain_cohere import CohereEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()


embeddings = CohereEmbeddings(
    model="embed-english-v3.0",
   )

result = embeddings.embed_query("delhi is capital of india")

print(str(result))