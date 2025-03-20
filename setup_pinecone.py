import os
import json
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
from config import Config

# Load environment variables
load_dotenv()

# ✅ Initialize Pinecone
pc = Pinecone(api_key=Config.PINECONE_API_KEY)

# ✅ Define existing Pinecone index name
index_name = "covid-faq-index"

# ✅ Connect to the existing Pinecone index
index = pc.Index(index_name)

# ✅ Use a correct embedding model (1024 dimensions)
embedding_model = SentenceTransformer("BAAI/bge-large-en-v1.5")  # ✅ This model outputs 1024-dim vectors

# ✅ Load questions from covid_faq.json
with open("covid_faq.json", "r", encoding="utf-8") as file:
    faq_data = json.load(file)

# ✅ Function to generate and store embeddings
def generate_embedding(text, unique_id):
    vector = embedding_model.encode(text).tolist()  # Convert text to embedding vector
    index.upsert(vectors=[(unique_id, vector)])
    print(f"✅ Stored embedding for ID {unique_id}")

# ✅ Check if faq_data is a list or dict and process accordingly
if isinstance(faq_data, dict):
    # JSON is in dictionary format
    questions = faq_data.keys()
elif isinstance(faq_data, list):
    # JSON is in list format
    questions = [item["question"] for item in faq_data if "question" in item]
else:
    raise ValueError("Invalid JSON format: Expected a dictionary or a list of question-answer pairs.")

# ✅ Generate embeddings for questions
for i, question in enumerate(questions):
    generate_embedding(question, unique_id=str(i))

print("🎉 Setup complete. Embeddings stored in Pinecone.")
