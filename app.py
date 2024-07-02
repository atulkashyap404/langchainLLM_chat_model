from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()



model = ChatOpenAI(model="gpt-4o")


result = model.invoke("what is 81 divided by 9?")
print("Full result:")
print(result)
print("Content only:")
print(result.content)  