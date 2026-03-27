from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel,Field
from dotenv import load_dotenv
import os

load_dotenv()

api = os.getenv("GEMINI_API_KEY")

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

class Movie(BaseModel):
    title:str = Field(description="The title of the Movie")
    year:int = Field(description="this is the Year in which movie was released")
    director:str = Field(description="the director of the following movie")
    rating:float = Field(description="the movies ratings out of 5")
    character:str = Field(description="Main character who is protagnist in this movie")

model_structure = model.with_structured_output(Movie)
result = model_structure.invoke("provide details about the movie Ironman1")
print(result)