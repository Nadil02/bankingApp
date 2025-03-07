
from datetime import datetime
#import sys
import os
#sys.path.append(os.path.abspath("c:/Users/ASUS TUF/Desktop/sftw/bankingApp/backend"))
from database import collection_account, collection_transaction#, collection_chatbot_details
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.chains.combine_documents import create_stuff_documents_chain
import chromadb
from pypdf import PdfReader

async def get_total_spendings_for_given_time_period(user_id: str, start_date: datetime, end_date: datetime) -> str:
    # Step 1: Find the user's accounts
    print("inside")
    user_accounts = collection_account.find({"user_id": user_id})
    user_accounts = await user_accounts.to_list(length=None)    
    # Get all account_ids associated with this user
    account_ids = [account["account_id"] for account in user_accounts]
    if not account_ids:
        return f"No accounts found for user ID: {user_id}"
    
    # Step 2: Find transactions for these accounts within the date range
    pipeline = [
        {
            "$match": {
                "account_id": {"$in": account_ids},
                "date": {"$gte": start_date, "$lte": end_date},
                "payment": {"$gt": 0}  # Only count outgoing payments
            }
        },
        {
            "$group": {
                "_id": None,
                "total_spendings": {"$sum": "$payment"}
            }
        }
    ]
    
    total_spendings_result = collection_transaction.aggregate(pipeline)
    
    # Process the result
    # result_list = list(total_spendings_result)
    result_list = await total_spendings_result.to_list(length=None)

    if result_list and "total_spendings" in result_list[0]:
        total_amount = result_list[0]["total_spendings"]
        formatted_start = start_date.strftime('%Y-%m-%d')
        formatted_end = end_date.strftime('%Y-%m-%d')
        print("total_amount",total_amount)
        return f"user`s total spendings are ${total_amount} for the period {formatted_start} to {formatted_end} use this and return ${total_amount} were spent by the user in the given time period. here {total_amount} is the amount, add that to the response. "
    else:
        print("No transactions found")
        return f"No transactions found for the period {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}"




# Initialize ChromaDB client and collection once (outside the function)
chroma_client = chromadb.PersistentClient(path="./chroma_db")
chroma_collection = chroma_client.get_or_create_collection(name="system_details")


async def chatbot_system_answer(query:str)->str :
    if chroma_collection.count() == 0:
        
        #doc = await collection_chatbot_details.find_one({}, {"_id": 0})  
        #if not doc:
         #   return "No system details available."
        #document_text = doc[list(doc.keys())[0]]

        pdf_path = './data/app.pdf'  # Path to the PDF file
        

        document_text = ""
        pdf_reader = PdfReader(pdf_path)
        for page in pdf_reader.pages:
            document_text += page.extract_text() or ""
        

        # Split text into chunks and get embeddings once
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = text_splitter.split_text(document_text)

        if chroma_collection.count() == 0:
            # Only insert chunks into ChromaDB once, if empty
            embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
            for idx, chunk in enumerate(chunks):
                embedding = embedding_model.embed_documents([chunk])
                chroma_collection.add(
                    ids=[str(idx)],
                    documents=[chunk],
                    embeddings=[embedding]
                )
            print(f"Inserted {len(chunks)} chunks into ChromaDB.")

    
    # Embed the user query once (reuse existing embedding model)
    embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    query_embedding = embedding_model.embed_query(query)

    # Search in ChromaDB for relevant documents
    results = chroma_collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    retrieved_chunks = results["documents"][0] if results["documents"] else []
    return "\n".join(retrieved_chunks) if retrieved_chunks else "No relevant information found."