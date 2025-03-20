from setup_pinecone import index

def get_chat_response(query):
    results = index.query(query, top_k=3, include_metadata=True)
    if results and results["matches"]:
        return results["matches"][0]["metadata"]["text"]
    return "Sorry, I couldn't find an answer. Please try rephrasing."
