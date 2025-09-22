from langgraph.prebuilt import create_react_agent

from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.mongodb import MongoDBSaver
from pymongo import MongoClient

llm = ChatGoogleGenerativeAI(
    api_key="AIzaSyDbTBJAWFB3xxSLIZ6o09ll7nZ47pvtDD8",
    model="gemini-2.5-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
)

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


# Create an agent with Checkpointer Memory
MONGODB_URI="mongodb+srv://agent123:7Lv1SXXddCJGGmgg@cluster0.4wpe5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGODB_URI)
checkpointer = MongoDBSaver(client)

memory_agent = create_react_agent(
    model=llm,
    tools=[get_weather],
    prompt="You are a helpful assistant",
    checkpointer=checkpointer
)