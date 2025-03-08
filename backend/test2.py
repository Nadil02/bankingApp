from sklearn.feature_extraction.text import TfidfVectorizer
from database import collection_chatbot_details

async def chatbot_system_answer(query: str) -> str:
    # Fetch the latest document from MongoDB
    doc = await collection_chatbot_details.find_one({}, {"_id": 0, "introduction": 1})
    if not doc or "introduction" not in doc:
        return "No system details available."

    document_text = doc["introduction"]

    # Break the document into larger chunks (e.g., by splitting into sentences or based on character count)
    document_chunks = document_text.split(". ")  # Split by sentence end

    # Vectorize using TF-IDF
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(document_chunks + [query])

    # Calculate cosine similarity
    cosine_similarities = (tfidf_matrix[-1] * tfidf_matrix[:-1].T).toarray().flatten()

    # Find the chunk with the highest similarity
    most_similar_idx = cosine_similarities.argmax()

    # Reassemble context from neighboring chunks
    # Add a few neighboring chunks around the most relevant chunk to provide more context
    context_start = max(0, most_similar_idx - 2)
    context_end = min(len(document_chunks), most_similar_idx + 3)  # Next 2 chunks
    relevant_chunks = document_chunks[context_start:context_end]
    
    # Return a more complete response
    return " ".join(relevant_chunks)

# Example usage
import asyncio

async def test_chatbot_system_answer():
    query = "What is todo list used for?"  # Example query
    response = await chatbot_system_answer(query)
    print("Response from chatbot system:", response)

asyncio.run(test_chatbot_system_answer())
