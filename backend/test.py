from datetime import datetime
import os
from database import collection_chatbot_details
from langchain.text_splitter import RecursiveCharacterTextSplitter
import chromadb

# HuggingFaceEmbeddings import (updated version if needed)
from langchain_community.embeddings import HuggingFaceEmbeddings




# Initialize embedding model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

async def chatbot_system_answer(query: str) -> str:
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
        
        # Debugging: Print out stored data to understand its structure
        print("Stored Data: ", stored_data)
        
        stored_texts = set(stored_data["documents"]) if stored_data and "documents" in stored_data else set()

        if document_text not in stored_texts:
            print("Database updated. Refreshing ChromaDB...")

            # Retrieve all document IDs in the collection
            stored_data = chroma_collection.get(include=["documents"])  # or ["metadatas"]
            all_documents = stored_data.get("documents", [])

            # Debugging: Print all documents to check their structure
            print("All Documents: ", all_documents)

            # If you only want IDs, you may extract them from the documents (if they're available in your data)
            # Check if all_documents is a list of strings or dictionaries
            if all_documents and isinstance(all_documents[0], dict):  # If it's a list of dictionaries
                all_ids = [doc['id'] for doc in all_documents]
            else:
                all_ids = [str(i) for i in range(len(all_documents))]  # In case it's a list of strings (chunks)

            if all_ids:
                chroma_collection.delete(ids=all_ids)  # Delete all documents by IDs
                print(f"Deleted documents with IDs: {all_ids}")

            existing_count = 0  # Reset count after deletion

    # If ChromaDB is empty, insert the latest system details
    if existing_count == 0:
        print("Inserting new data into ChromaDB...")
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
        chunks = text_splitter.split_text(document_text)

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

    # Query ChromaDB for relevant documents
    results = chroma_collection.query(
        query_embeddings=[query_embedding],
        n_results=2
    )

    # Retrieve the best results
    retrieved_chunks = results.get("documents", [[]])[0]
    return " ".join(retrieved_chunks).strip() if retrieved_chunks else "No relevant information found."


# Test the function
import asyncio

async def test_chatbot_system_answer():
    query = "What is todo list in this system?"  # Example query
    response = await chatbot_system_answer(query)
    print("Response from chatbot system:", response)

# Run the test function
asyncio.run(test_chatbot_system_answer())
