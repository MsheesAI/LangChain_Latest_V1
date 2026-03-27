import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware
from langgraph.checkpoint.memory import InMemorySaver  
from langchain_core.messages import HumanMessage

load_dotenv()

os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")


#summarization middleware

agent = create_agent(
    model="gpt-4o-mini",
    checkpointer=InMemorySaver(),
    middleware=[SummarizationMiddleware(
        model="gpt-4o-mini",
        trigger=("messages",10),
        keep=("messages",4)
    )]
)

#run with thread id

config ={"configurable":{"thread_id":"test-1"}}

question = [
    "what is 2+2 ",
    "what is 5*100",
    "what is 6*100",
    "what is 7/100",
    "what is 5100 +1",
    "what is 8*100",
]

for q in question:
    response = agent.invoke({"messages":[HumanMessage(content=q)]},config)
    print(f"Messages:{response["messages"][-1].content}")
    print(f"Messages:{len(response["messages"])}")
