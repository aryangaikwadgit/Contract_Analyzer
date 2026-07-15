import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from src.token_tracker import TokenTracker

load_dotenv()

client = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"), model=os.getenv("MODEL_NAME"), temperature=0
)



tracker = TokenTracker()


# TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")


# import os
# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI
# load_dotenv()

# client = ChatGoogleGenerativeAI(
#     model=os.getenv("MODEL_NAME_GEMINI"),
#     google_api_key=os.getenv("OPEN_ROUTER_API_KEY"),
#     temperature=0,
# )

# from langchain_openai import ChatOpenAI

# load_dotenv()

# client = ChatOpenAI(
#     api_key=os.getenv("OPEN_ROUTER_API_KEY"),
#     base_url="https://openrouter.ai/api/v1",
#     model=os.getenv("MODEL_NAME_GEMINI"),
#     temperature=0,
# )