from langchain.agents import create_agent
from dotenv import load_dotenv
import os
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langgraph.checkpoint.memory import InMemorySaver
from langchain.messages import HumanMessage
from langgraph.types import Command

load_dotenv()

os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")

def read_email(email_id:str)->str:
    """Read an email by its ID and return its content."""
    return f"Email content for {email_id} "

def send_email(recipant:str,subject:str,body:str)->str:
    """Send an email to a recipient with a subject and body."""
    return f"Emai sent to {recipant} with subject {subject}"


agent = create_agent(
    model="gpt-4o-mini",
    tools = [read_email,send_email],
    checkpointer=InMemorySaver(),
    middleware=[HumanInTheLoopMiddleware(
        interrupt_on={
            "send_email":{
                "allowed_decisions":["approve","edit","reject"]
            },
            "read_email_tool":False
        }
    )]
)

config = {"configurable":{"thread_id":"test-approve"}}

result = agent.invoke(
    {"messages":[HumanMessage(content="send email to johntest@example.com with subject: Hello how are you")]},config=config
)


if  '__interrupt__' in result :
    print("paused approving🥱")

    result = agent.invoke(
        Command(
            resume={"decisions":[{"type":"approve"}]}
        ),config=config
    )

    print(f"result✅🫡{result["messages"][-1].content}")