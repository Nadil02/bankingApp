
user_id=1
# for this user id input documents for collection_predicted_balance table using balance_prediction.excel file
# required fields: account_id, prediction_id, date, description, explanation, balance, user_id. use base model PredictedIncome in models.py
# excel has this columns Date, Denormalized_Forecast column which hase balance value. and Explanation column with explanation.
# use account_id=1, description="account balance prediction "for all documents.
# for each row in excel add max prediction_id from collection_predicted_balance table + 1
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from datetime import datetime
from models import PredictedBalance 
from database import collection_predicted_balance
import pandas as pd
async def insert_predicted_balance_from_excel():
    # Read the Excel file
    df = pd.read_excel(r"C:\Users\User\Downloads\balance_shiharadata_with_explanations.xlsx")

    # Get the maximum prediction_id from the collection
    max_prediction_id = await collection_predicted_balance.find_one(
        {}, sort=[("prediction_id", -1)]
    )
    max_prediction_id = max_prediction_id['prediction_id'] if max_prediction_id else 0

    # Prepare the documents to be inserted
    documents = []
    for index, row in df.iterrows():
        document = PredictedBalance(
            account_id=2,
            prediction_id=int(max_prediction_id) + int(index) if isinstance(index, int) else int(max_prediction_id) + int(str(index)) + 1,
            date=row['Date'],
            description="account balance prediction",
            explanation=row['Explanation'],
            balance=row['Forecast'],
            user_id=1
        )
        documents.append(document.dict())

    # Insert the documents into the collection
    if documents:
        await collection_predicted_balance.insert_many(documents)
if __name__ == "__main__":
    import asyncio
    asyncio.run(insert_predicted_balance_from_excel())

