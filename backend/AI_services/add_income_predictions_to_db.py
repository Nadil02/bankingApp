
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
from models import PredictedIncome 
from database import collection_predicted_income
import pandas as pd
async def insert_predicted_income_from_excel():
    # Read the Excel file
    df = pd.read_excel(r"C:\Users\User\Downloads\tft_predictions_with_confidence_Shihara_income.xlsx")

    # Get the maximum prediction_id from the collection
    # max_prediction_id = await collection_predicted_income.find_one(
    #     {}, sort=[("prediction_id", -1)]
    # )
    # max_prediction_id = max_prediction_id['prediction_id'] if max_prediction_id else 0

    # Prepare the documents to be inserted
    documents = []
    for index, row in df.iterrows():
        document = PredictedIncome(
            account_id=2,
            date=pd.to_datetime(row['Date']),
            explanation="This balance forecast relies heavily on the precedent of surprising and irregular adjustments. The rarity and unpredictability of past events shape the estimation of this balance.",
            amount=float(row['Predicted_Amount']),
            category_id=int(row['Cluster']),
            user_id=1,
            clasification_uncertainity=float(row['Uncertainty']),
            regression_uncertainity=float(row['Uncertainty'])
        )
        documents.append(document.dict())

    # Insert the documents into the collection
    if documents:
        await collection_predicted_income.insert_many(documents)
if __name__ == "__main__":
    import asyncio
    asyncio.run(insert_predicted_income_from_excel())

