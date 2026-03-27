from dotenv import load_dotenv
import os
from langchain.agents import create_agent
load_dotenv()

api = os.environ["OPENAI_API_KEY"]

def get_weather(city:str)->str:
    """Get the weather for a city"""
    return f"the weather in {city} is sunny , 49c degree"

agent = create_agent(model="gpt-4o-mini",tools=[get_weather],system_prompt="you are an helpful assistant")

result = agent.invoke({"messages":[{"role":"user","content":"What is the weather in karachi"}]})
print(result["messages"][-1].content)

