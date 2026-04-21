from langchain_openai import OpenAI
import os
#loading the llm from langchain_openai 
from dotenv import load_dotenv
#we should must enable load_dotenv, first we will understand meaning of it load_dotenv() = "Read my .env file and load its values into my program"
#it means Go to the .env file, read everything, make it available to my code
load_dotenv()
#create object of openai
llm = OpenAI(model='gpt-3.5-turbo-instruct')

#invoke means run this component with input and get output
#run thiscomponent with input and get output
result=llm.invoke("what is the capital of india?")

print(result)