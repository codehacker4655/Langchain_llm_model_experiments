from langchain_huggingface import ChatHuggingFace , HuggingFacePipeline
#huggingface pipeline is used when we want to run our model locally

llm = HuggingFacePipeline.from_model_id(
    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )

)

model = ChatHuggingFace(llm=llm)
model.invoke("what is capital of india?")
