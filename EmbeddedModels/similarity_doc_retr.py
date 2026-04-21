from langchain_cohere import CohereEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise  import cosine_similarity
import numpy as np

load_dotenv()

embeddings = CohereEmbeddings(
    model="embed-english-v3.0",
   )

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query='tell me about ricky ponting'

vector = embeddings.embed_query(query)
docs_vector = embeddings.embed_documents(documents)

scores = cosine_similarity([vector], docs_vector)[0]

index, score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("similarity score is:", score)