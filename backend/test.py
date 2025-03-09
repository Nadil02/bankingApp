import re
import chromadb
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from database import collection_chatbot_details
import asyncio

# Function to limit the answer by sentences
def limit_answer_by_sentences(response: str, sentence_limit: int = 6) -> str:
    sentences = re.split(r'(?<=\.)\s+', response)
    
    # If there are more sentences than the limit, truncate and add ellipsis
    if len(sentences) > sentence_limit:
        return " ".join(sentences[:sentence_limit]) + "..."
    
    return response


# Main function for answering chatbot queries
async def chatbot_system_answer(query: str) -> str:
    try:
        # Initialize embedding model
        embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

        # Initialize ChromaDB client and collection
        chroma_client = chromadb.PersistentClient(path="./chroma_db")
        chroma_collection = chroma_client.get_or_create_collection(name="system_details")

        # Fetch the latest document from MongoDB
        doc = await collection_chatbot_details.find_one({}, {"_id": 0, "introduction": 1})
        if not doc or "introduction" not in doc:
            return "No system details available."

        document_text = doc["introduction"]

        # Check if stored embeddings match the latest database entry
        existing_count = chroma_collection.count()

        if existing_count > 0:
            # Retrieve existing stored data to compare
            stored_data = chroma_collection.get(include=["documents"])
            stored_texts = set(stored_data["documents"]) if stored_data and "documents" in stored_data else set()

            # Update the ChromaDB only if document has changed
            if document_text not in stored_texts:
                print("Database updated. Refreshing ChromaDB...")

                # Retrieve all document IDs in the collection
                stored_data = chroma_collection.get(include=["documents"])
                all_documents = stored_data.get("documents", [])

                # Determine document IDs
                if all_documents and isinstance(all_documents[0], dict):
                    all_ids = [doc['id'] for doc in all_documents]
                else:
                    all_ids = [str(i) for i in range(len(all_documents))]

                if all_ids:
                    chroma_collection.delete(ids=all_ids)
                    print(f"Deleted documents with IDs: {all_ids}")

                existing_count = 0

        # If ChromaDB is empty, insert the latest system details
        if existing_count == 0:
            print("Inserting new data into ChromaDB...")
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
            chunks = text_splitter.split_text(document_text)

            # Insert chunks into ChromaDB
            for idx, chunk in enumerate(chunks):
                embedding = embedding_model.embed_documents([chunk])[0]
                chroma_collection.add(
                    ids=[str(idx)],
                    documents=[chunk],
                    embeddings=[embedding]
                )
            print(f"Inserted {len(chunks)} chunks into ChromaDB.")

        # Process query to get embedding
        query_embedding = embedding_model.embed_query(query)

        # ChromaDB query for relevant documents
        results = chroma_collection.query(
            query_embeddings=[query_embedding],
            n_results=4
        )

        # Retrieve and format results
        retrieved_chunks = results.get("documents", [[]])[0]
        response = " ".join(retrieved_chunks).strip() if retrieved_chunks else "No relevant information found."

        # Limit the answer by sentences
        return limit_answer_by_sentences(response, sentence_limit=3)

    except Exception as e:
        return f"An error occurred: {str(e)}"


# Test the chatbot system
async def test_chatbot_system_answer():
    query = "What is todo list in this system?"  
    response = await chatbot_system_answer(query)
    print("Response from chatbot system:", response)

# Running the test function
asyncio.run(test_chatbot_system_answer())
