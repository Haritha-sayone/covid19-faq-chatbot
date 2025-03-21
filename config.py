import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT")
    PINECONE_INDEX = os.getenv("PINECONE_INDEX")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

