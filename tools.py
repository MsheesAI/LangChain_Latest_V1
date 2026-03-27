from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from dotenv import load_dotenv
import os

load_dotenv()

api = os.getenv("GEMINI_API_KEY")

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)
response = model.invoke("why do parrots talk")
print(response.content)

@tool
def get_weather(location:str)->str:
    """Get weather at a location"""
    return f"Its sunny in {location}"

model_tool = model.bind_tools([get_weather])

response = model_tool.invoke("whats the weather in location:boston")
for tool_call in response.tool_calls:
    print(f"Tool:{tool_call["name"]}")
    print(f"Args:{tool_call["args"]}")