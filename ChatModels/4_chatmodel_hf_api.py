from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
#chathuggingface is used when we need to build chat_models and huggingfaceendpoint is used when we want to use the models through api's from huggingface
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-0528",#ADDRES OF THE MODEL
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,#FOR RANDOMNESS IF FALSE IT WILL TAKE MOST PROBABLE WORDS AND IF IT IS TRUE , IT WILL TAKE EVEN LESS PROBABLITLTY WORDS TO ALLOW RANDOMNESS AND CREATIVENESS

    repetition_penalty=1.03,#DISCOURAGES THE MODEL FROM REPEATING THE SAME WORDS AGAIN AND AGAIN
    provider="auto",  # let Hugging Face choose the best provider for you
)

model = ChatHuggingFace(llm=llm)
result= model.invoke("what is capital of india?")
print(result.content)