from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage,SystemMessage,AIMessage
from dotenv import load_dotenv
import os

load_dotenv()

api = os.getenv("GEMINI_API_KEY")

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

messages = [
    SystemMessage("You are an expert poet"),
    HumanMessage("write a poem on AI")
]
response = model.invoke(messages)
print(response.content)