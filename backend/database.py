import motor.motor_asyncio
import os
from dotenv import load_dotenv

# load environment variables from the .env file
load_dotenv()

# MongoDB URI from .env file
MONGO_URI = os.getenv("MONGO_URI")

# create a client instance for MongoDB
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)

# database
db = client["project"] 

#collections
collection_user = db["user"]
collection_OTP = db["OTP"]
collection_Todo_list = db["Todo-list"]
collection_account = db["account"]
collection_bank = db["bank"]
collection_chatbot = db["chatbot"]
collection_goal = db["goal"]
collection_notification = db["notification"]
collection_predicted_balance = db["predicted_balance"]
collection_predicted_expense = db["predicted_expense"]
collection_predicted_income = db["predicted_income"]
collection_transaction = db["transaction"]
collection_transaction_category = db["transaction_category"]
collection_credit_periods = db["credit_periods"]
collection_dummy_values = db["user_dummy"]
collection_credit_periods = db["credit_periods"]

