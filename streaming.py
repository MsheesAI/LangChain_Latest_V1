from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model("gpt-4o-mini")

stream = model.stream("Write me a 100 words aragraph on AI")
for chunck in stream:
    print(chunck.text)

#Batch

"""Batch is a collection of independent req to a modelcan significally improve performance and reduce costs,
as the processing can be done in parallel"""

responses = model.batch([
    "why do parrots have colorful feathers?",
    "why do airplanes fly",
    "what is quantum computing"
])
for response in responses:
    print(response.content)