from motor.motor_asyncio import AsyncIOMotorClient
from database import collection_bank, collection_account

# # MongoDB connection
# client = AsyncIOMotorClient("mongodb://localhost:27017")
# db = client["your_database_name"]
# collection = db["your_collection_name"]

# bank_account_data = {
#     "bank_account": "Peoples_Bank",
#     "bank_id": 23,
#     "account_id": "125A",
#     "user_id": 1,
#     "account_number": 6789123,
#     "account_type": "savings",
#     "credit_limit": 0,
#     "due_date": 0,
#     "balance": 0
# }

bank_data = {
    "bank_name": "Peoples",
    "logo": "<logo_url>",
    "bank_id": 23
}


async def insert_bank():
    result = await collection_bank.insert_one(bank_data)
    print(f"Inserted document ID: {result.inserted_id}")

# # Insert document asynchronously
# async def insert_bank_account():
#     result = await collection.insert_one(bank_account_data)
#     print(f"Inserted document ID: {result.inserted_id}")

# Run the async function
import asyncio
# asyncio.run(insert_bank_account())
asyncio.run(insert_bank())
