from datetime import datetime, timedelta,timezone
from utils.encrypt_and_decrypt import decrypt
from database import collection_transaction, collection_transaction_category, collection_predicted_balance, collection_predicted_expense, collection_predicted_income,collection_account,collection_credit_periods,collection_goal, collection_bank,collection_user
from typing import Tuple
from schemas.dashboard import ResponseSchemaUsernameProfilePic, SpendingCategory, ResponseSchema, CreditCardResponse, CategorySpending, Summary
from typing import List, Dict,Union,Optional,Any
from datetime import datetime, timedelta
import math

def serialize_document(document):
    document["_id"] = str(document["_id"])
    return document


# convert account id into id list
def account_list(account_id: Union[int, List[int]]):
    if isinstance(account_id, int):
        account_ids = [account_id]
    else:
        account_ids = account_id
    return account_ids


# get user all acount ids and account lits for dashboard drop down
async def all_accounts(user_id:int):
    items = await collection_account.find(
        {"user_id":user_id},
        {"account_number":1, "account_type":1, "balance":1,"bank_account":1, "account_id":1, "bank_id":1}).to_list(length=100)
    account_list = [serialize_document(item) for item in items]
    print("account_list",account_list)
    # bank_ids = []
    # for item in account_list:
    #     bank_ids.append(item["bank_id"])
    # print("bank_ids",bank_ids)
    # bank_name = await collection_bank.find({"bank_id":{"$in":bank_ids}},{"_id":0, "bank_name":1}).to_list(length=100)
    # print("bank_name",bank_name)
    # for i,item in enumerate(account_list):
    #     item.update({"bank_account":bank_name[i]["bank_name"]})
    bank_ids = [item["bank_id"] for item in account_list if "bank_id" in item]

    # Fetch bank names
    bank_name_data = await collection_bank.find(
        {"bank_id": {"$in": bank_ids}},
        {"_id": 0, "bank_id": 1, "bank_name": 1, "logo": 1}
    ).to_list(length=100)

    # Create a mapping of bank_id to bank_name
    bank_name_map = {bank["bank_id"]: bank["bank_name"] for bank in bank_name_data}
    bank_logo_map = {bank["bank_id"]: bank["logo"] for bank in bank_name_data}
    # Update account_list with bank names
    for item in account_list:
        bank_id = item.get("bank_id")
        item["bank_account"] = bank_name_map.get(bank_id, "Unknown")
        item["bank_logo"] = bank_logo_map.get(bank_id, "Unknown")
    account_ids = [item.get("account_id") for item in account_list]
    return account_ids, account_list


#most 6 spending categories with the ammount
async def fetch_top_spending_categories(account_ids:list, start_date:datetime, end_date:datetime, total_expenses:float):
    category_pipeline = [
        {"$match": {"account_id":{"$in": account_ids},"date":{"$gte":start_date, "$lte":end_date},"payment":{"$gt":0}}},
        {"$group": {"_id": "$category_id", "total_spent": {"$sum": "$payment"}}},
        {"$sort": {"total_spent": -1}},
        {"$limit":6}
    ]
    category_result = await collection_transaction.aggregate(category_pipeline).to_list(length=6)
    category_ids = [item["_id"] for item in category_result]


    # Fetch category names
    categories_data = await collection_transaction_category.find({"category_id": {"$in": category_ids}}).to_list(None)
    category_map = {cat["category_id"]: cat["category_name"] for cat in categories_data}

    # Compute spending categories
    top_categories_sum = sum(item["total_spent"] for item in category_result)
    other_spent = total_expenses - top_categories_sum

    # Prepare category list
    top_categories = [
    {"category_name": category_map.get(item["_id"], "Unknown"), "total_spent": item["total_spent"]}
    for item in category_result
    ]
    

    # Add "Other" category if applicable
    if other_spent > 0 and (other_spent / total_expenses) < 0.3:
        # top_categories.append(SpendingCategory(category_name="Other", total_spent=other_spent).dict())
        top_categories.append({"category_name":"Other", "total_spent":other_spent})

    for item in top_categories:
        item.update({"category_precentage":(item["total_spent"]/top_categories_sum)*100})
    print("KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK")
    print("top_categories",top_categories)
    
    return top_categories


# get total_income,total_expenses, total_savings for single account or list of account
async def fetch_financial_summary(account_ids:list, start_date:datetime, end_date:datetime):
    # make pipeline
    pipeline = [
        {"$match": {"account_id":{"$in": account_ids},"date":{"$gte":start_date, "$lte":end_date}}},
        {"$group": {"_id": None, "total_income": {"$sum": {
                    "$cond": [
                        {"$or": [{"$eq": ["$receipt", None]}, {"$eq": ["$receipt", float("NaN")]}]},
                        0,
                        {
                            "$convert": {
                                "input": "$receipt",
                                "to": "double",
                                "onError": 0,
                                "onNull": 0
                            }
                        }
                    ]
                }}, "total_expenses": { "$sum": {
                    "$cond": [
                        {"$or": [{"$eq": ["$payment", None]}, {"$eq": ["$payment", float("NaN")]}]},
                        0,
                        {
                            "$convert": {
                                "input": "$payment",
                                "to": "double",
                                "onError": 0,
                                "onNull": 0
                            }
                        }
                    ]
                }}}}
    
    ]
    print("start date",start_date)
    print("end date",end_date)
    print("Pipeline:", pipeline)

    result = await collection_transaction.aggregate(pipeline).to_list(length=1)
    if not result:
        print("No data found for the given date range.")
        return {"total_income": 0.0, "total_expenses": 0.0, "total_savings": 0.0} # Default values

    print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
    print("Result:", result)
    
    aggregated_data = result[0]
    total_income = aggregated_data.get("total_income", 0.0)
    total_expenses = aggregated_data.get("total_expenses", 0.0)

    # Replace NaN with 0
    if math.isnan(total_income):
        total_income = 0.0
    if math.isnan(total_expenses):
        total_expenses = 0.0


    total_savings = max(total_income - total_expenses, 0.0)
    
    result = Summary(total_income=total_income, total_expenses=total_expenses, total_savings=total_savings)
    result=result.dict()
    return result


async def fetch_first_transaction_date(account_ids: Union[str, List[str]]) -> dict:
    # Ensure account_ids is a list
    if isinstance(account_ids, str):
        account_ids = [account_ids]

    pipeline = [
        {"$match": {"account_id": {"$in": account_ids}}},
        {"$sort": {"date": 1}},  # Sort by ascending date
        {"$limit": 1},           # Get the earliest one
        {"$project": {"_id": 0, "date": 1}}  # Only return the date field
    ]

    result = await collection_transaction.aggregate(pipeline).to_list(length=1)

    return {"first_transaction_date": result[0]["date"] if result else None}


async def fetch_past_transactions(
    account_ids: list, end_date: datetime, days: int
) -> Dict[str, List[Dict[str, Any]]]:
    start_date_past = end_date - timedelta(days=days)
    transaction_pipeline = [
        {
            "$match": {
                "account_id": {"$in": account_ids},
                "date": {"$gte": start_date_past, "$lte": end_date - timedelta(days=1)}
            }
        },
        {
            "$sort": {"date": 1, "account_id": 1}  
        },
        {
            "$group": {
                "_id": {"date": "$date", "account_id": "$account_id"},
                "total_receipt": {"$sum": "$receipt"},
                "total_payment": {"$sum": "$payment"},
                "last_balance": {"$last": "$balance"}  
            }
        },
        {
            "$group": {
                "_id": "$_id.date",
                "total_receipt": {"$sum": "$total_receipt"},
                "total_payment": {"$sum": "$total_payment"},
                "final_balance": {"$sum": "$last_balance"}  
            }
        },
        {"$sort": {"_id": 1}}
    ]

    transaction_data = await collection_transaction.aggregate(transaction_pipeline).to_list(None)
    transactions_by_date = {item["_id"].date(): item for item in transaction_data}
    receipts = []
    payments = []
    balances = []
    last_balance = None  
    for i in range(days):
        current_date = (start_date_past + timedelta(days=i)).date()  
        if current_date in transactions_by_date:
            item = transactions_by_date[current_date]
            total_receipt = item["total_receipt"]
            total_payment = item["total_payment"]
            last_balance = item["final_balance"]  
        else:
            total_receipt = 0
            total_payment = 0
        receipts.append({"date": current_date.strftime("%Y-%m-%d"), "total_receipt": total_receipt})
        payments.append({"date": current_date.strftime("%Y-%m-%d"), "total_payment": total_payment})
        balances.append({"date": current_date.strftime("%Y-%m-%d"), "final_balance": last_balance if last_balance is not None else 0})
    return {"receipts": receipts, "payments": payments, "balances": balances}


async def fetch_predicted_data(
    account_ids: list,
    end_date: datetime,
    days: int
) -> Dict[str, List[Dict[str, Any]]]:
    start_date_future = end_date.replace(hour=0, minute=0, second=0, microsecond=0)
    end_date_future = (end_date + timedelta(days=days)).replace(hour=0, minute=0, second=0, microsecond=0)
    print("start_date_future",start_date_future)
    print("end_date_future",end_date_future)
    
    amount_pipeline = [
        {"$match": {
            "account_id": {"$in": account_ids},
            "date": {"$gte": start_date_future, "$lte": end_date_future}
        }},
        {"$group": {
            "_id": "$date",
            "total_amount": {"$sum": "$amount"}
        }},
        {"$sort": {"_id": 1}}
    ]

    balance_pipeline = [
        {"$match": {
            "account_id": {"$in": account_ids},
            "date": {"$gte": start_date_future, "$lte": end_date_future}
        }},
        {"$group": {
            "_id": "$date",
            "total_balance": {"$sum": "$balance"}
        }},
        {"$sort": {"_id": 1}} 
    ]

    # Fetch predicted data for all accounts
    predicted_income_data = await collection_predicted_income.aggregate(amount_pipeline).to_list(None)
    predicted_expense_data = await collection_predicted_expense.aggregate(amount_pipeline).to_list(None)
    predicted_balance_data = await collection_predicted_balance.aggregate(balance_pipeline).to_list(None)

    for data in predicted_income_data:
        if data["_id"] is None:
            print("Warning: Aggregation result with missing date:", data)
    # Convert transaction data into dictionaries for quick lookup
    income_dict = {data["_id"].date(): data["total_amount"] for data in predicted_income_data}
    expense_dict = {data["_id"].date(): data["total_amount"] for data in predicted_expense_data}
    balance_dict = {data["_id"].date(): data["total_balance"] for data in predicted_balance_data}

    print("predicted_income_data",income_dict)
    print("predicted_expense_data",expense_dict)
    print("predicted_balance_data",balance_dict)
    
    income_list = []
    expense_list = []
    balance_list = []

    for i in range(days):
        current_date = (start_date_future + timedelta(days=i)).date()

        income_list.append({"date": current_date.strftime("%Y-%m-%d"), "predicted_income": income_dict.get(current_date, 0)})
        expense_list.append({"date": current_date.strftime("%Y-%m-%d"), "predicted_expenses": expense_dict.get(current_date, 0)})
        balance_list.append({"date": current_date.strftime("%Y-%m-%d"), "predicted_balance": balance_dict.get(current_date, 0)})

    return {
        "predicted_income": income_list,
        "predicted_expenses": expense_list,
        "predicted_balance": balance_list
    }


async def update_second_header(account_id:Union[int, List[int]],start_date:Union[datetime,str], end_date:Union[datetime,str]):

    account_ids = account_list([account_id] if isinstance(account_id, int) else account_id)

    date_format = "%Y-%m-%d"

    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, date_format)
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, date_format)

    financial_summery = await fetch_financial_summary(account_ids,start_date, end_date)
    print("financial_summery_type",type(financial_summery))
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("financial_summery", financial_summery)
    total_expenses = financial_summery["total_expenses"]

    print("total_expenses",total_expenses)
    # print("total_expenses category " ,total_expenses)
    spending_category = await fetch_top_spending_categories(account_ids,start_date, end_date, total_expenses)
    #return as a touple
    print("spending_category", spending_category)
    return financial_summery,spending_category


# Most spent category for the past 100 days
async def fetch_most_spent_category_100_days(account_id: list, end_date: datetime) -> list:
    """ Fetch the most spent category and its amount for the past 100 days. """
    end_date = datetime.now(timezone.utc)
    start_date = end_date - timedelta(days=100)

    category_pipeline = [
        {"$match": {"account_id": {"$in": account_id}, "date": {"$gte": start_date, "$lte": end_date}, "payment": {"$gt": 0}}},
        {"$group": {"_id": "$category_id", "total_spent": {"$sum": "$payment"}}},
        {"$sort": {"total_spent": -1}},  # Sort by total_spent in descending order
        {"$limit": 1}  # Only get the top spending category
    ]

    category_result = await collection_transaction.aggregate(category_pipeline).to_list(length=1)
    if not category_result:
        return {"most_spending_category": "No Data", "most_spending_amount": 0.0}  # Return default if no transactions exist

    most_spent_category_id = category_result[0]["_id"]
    most_spent_amount = category_result[0]["total_spent"]

    # Fetch the category name from the transaction_category collection
    category_data = await collection_transaction_category.find_one({"category_id": most_spent_category_id})
    most_spent_category_name = category_data["category_name"] if category_data else "Unknown"
    return {"most_spending_category": most_spent_category_name, "most_spending_amount": most_spent_amount}


# load full details
async def load_full_details(user_id:int, start_date: Optional[Union[str, datetime]] = None, end_date: Optional[Union[str, datetime]] = None):

    #take account id and account details based on user id
    account_ids, account_list = await all_accounts(user_id)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    saving_account_ids = [account["account_id"] for account in account_list if account["account_type"] == "savings"]
    credit_card_ids = [account["account_id"] for account in account_list if account["account_type"] == "credit"]

    #get total balance of saving accounts
    total_balance = sum(account["balance"] for account in account_list if account["account_type"] == "savings")
    # if date is string convert it into datetime (if user provide date)
    if isinstance(start_date, str):
        parsed_start_date = datetime.strptime(start_date, "%Y-%m-%d")
    if isinstance(end_date, str):    
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

    # print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
    
    # if date is not provided the user
    if not start_date:
        # print("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
        end_date = datetime.now(timezone.utc)
        start_date = end_date - timedelta(days=30)
        financial_summery, spending_category = await update_second_header(saving_account_ids,start_date,end_date)
        past_transaction_100_days = await fetch_past_transactions(saving_account_ids,end_date,100)
        predicted_transaction_7_days = await fetch_predicted_data(saving_account_ids, end_date,8)
        most_spending_category_100_days = await fetch_most_spent_category_100_days(saving_account_ids,end_date) 
        date = {"start_date": start_date, "end_date": end_date}
        # print("account_list at not start date",account_list)
        user_details = await collection_user.find_one({"user_id": user_id},{"_id":0,"username":1})
        if user_details and "username" in user_details:
            userName = decrypt(user_details["username"])
        else:
            userName = "Unknown"
        first_transaction_info = await fetch_first_transaction_date(saving_account_ids)
        first_transaction_date = first_transaction_info.get("first_transaction_date")
        return ResponseSchema(
            user_name=userName,
            accounts_list=account_list,
            total_savings_accounts_balance=total_balance,
            financial_summary=financial_summery,
            category_spending=spending_category,
            past_100_days_transactions=past_transaction_100_days,
            upcoming_7_days_predictions=predicted_transaction_7_days,
            most_spending=most_spending_category_100_days,
            date=date,
            first_transaction_date=first_transaction_date
        )
    
    else:
        # print("RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
        if start_date is None or end_date is None:
            raise ValueError("start_date and end_date must not be None")
        # Ensure start_date and end_date are not None before calling update_second_header
        return await update_second_header(saving_account_ids, start_date, end_date)
    

async def fetch_minus_predicted_balance(account_id: int) -> List[Dict[str, Any]]:
    end_date = datetime.utcnow()
    predicted_balance_data = await collection_predicted_balance.find(
        {"account_id": account_id}
    ).to_list(None)

    negative_balance_prediction = []
    for prediction in predicted_balance_data:
        date = prediction["date"]
        predicted_balance = prediction["balance"]

        if predicted_balance < 0:
            negative_balance_prediction.append({
                "date": date,
                "predicted_balance": predicted_balance
            })
            break

    if not negative_balance_prediction:
        negative_balance_prediction.append({
            "date": end_date,
            "predicted_balance": 0
        })

    return negative_balance_prediction


# Check surplus accounts for savings account
async def check_surplus_accounts(user_id: int, account_id: int) -> List[Dict[str, Any]]:
    user_accounts = await collection_account.find({"user_id": user_id}).to_list(None)
    account_ids = [account["account_id"] for account in user_accounts if account["account_id"] != account_id]

    negative_balance_prediction = await fetch_minus_predicted_balance(account_id)

    if not negative_balance_prediction or all(nb["predicted_balance"] >= 0 for nb in negative_balance_prediction):
        return []

    required_balance = abs(negative_balance_prediction[0]["predicted_balance"])

    surplus_accounts = []
    for acc_id in account_ids:
        predicted_balances = await collection_predicted_balance.find(
            {"account_id": acc_id}
        ).sort("date", 1).to_list(None)

        if predicted_balances:
            min_balance = min(prediction["balance"] for prediction in predicted_balances)
            

            if min_balance >= required_balance:
                surplus_accounts.append({
                    "account_id": acc_id,
                    "min_surplus_balance": min_balance
                })

    return surplus_accounts


# load specific account details
async def load_specific_account(account_id:int, user_id:Optional[int] = None, start_date: Optional[Union[str, datetime]] = None, end_date: Optional[Union[str, datetime]] = None):
    account_ids = [account_id]

    # print("KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK")
    # print("account_ids",account_ids)
    # print("user_id",user_id)

    if not start_date:
        end_date = datetime.now(timezone.utc)
        start_date = end_date - timedelta(days=30)
        second_header = await update_second_header(account_ids,start_date,end_date)
        print("second_header",second_header)
        
        past_transaction_100_days = await fetch_past_transactions(account_ids,end_date,100)
        # print("past_transaction_100_days", past_transaction_100_days)
        predicted_transaction_7_days = await fetch_predicted_data(account_ids, end_date,8)
        print("predicted_transaction_7_days", predicted_transaction_7_days)
        

        most_spending_category_100_days = await fetch_most_spent_category_100_days(account_ids,end_date)
        negative_balance_prediction= await fetch_minus_predicted_balance(account_id)
        

        surplus_accounts = []
        if user_id is not None:
            surplus_accounts = await check_surplus_accounts(user_id, account_id)
        first_transaction_date = await fetch_first_transaction_date([str(aid) for aid in account_ids])
        print("DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")

        return second_header, past_transaction_100_days, predicted_transaction_7_days,most_spending_category_100_days, negative_balance_prediction,surplus_accounts,first_transaction_date
    else:
        print("start_date",start_date)
        print("end_date",end_date)
        return await update_second_header(account_ids,start_date,end_date)
    

# Financial summaries for credit account
async def fetch_credit_financial_summary(account_id: int, timeperiod: Optional[int] = None):
    
    if timeperiod:
        # Fetch data from credit_periods collection based on given timeperiod
        credit_summary = await collection_credit_periods.find_one(
            {"account_id": account_id, "period_id": timeperiod},  
            {"credit_limit": 1, "total_expenses": 1, "remaining_balance": 1, "_id": 0}
        )
        if credit_summary:
            return {
                "credit_limit": float(credit_summary.get("credit_limit", 0.0)),
                "total_expenses": float(credit_summary.get("total_expenses", 0.0)),
                "remaining_balance": float(credit_summary.get("remaining_balance", 0.0))
            }
    
    # If timeperiod is not given, fetch data from account_collection
    account_data = await collection_account.find_one(
        {"account_id": account_id},
        {"credit_limit": 1, "balance": 1, "due_date": 1, "_id": 0}
    )
    
    if not account_data:  # Check if account_data is None
        return {"credit_limit": 0.0, "total_expenses": 0.0, "remaining_balance": 0.0}

    # Convert to float before performing subtraction
    credit_limit = float(account_data.get("credit_limit", 0.0))
    total_expenses = float(account_data.get("balance", 0.0))
    remaining_balance = credit_limit - total_expenses
    
    # result = {"credit_limit": credit_limit, "total_expenses": total_expenses, "remaining_balance": remaining_balance}
    return CreditCardResponse(credit_limit=credit_limit, total_expenses=total_expenses, remaining_balance=remaining_balance)


#most spending categories
async def fetch_most_spent_categories(account_id: int, total_expenses: float,timeperiod: Optional[int] = None):
    
    account_data = await collection_account.find_one({"account_id": account_id})
    due_date = account_data["due_date"]

    if timeperiod:
        period = await collection_credit_periods.find_one({"account_id": account_id, "period_id": timeperiod})
        
        period_id = period["period_id"]
        current_period_start_date = due_date - timedelta(days=30)
        start_date = period["start_date"]
        start_date = period["end_date"]
    else:
        last_period_id =await collection_credit_periods.find_one({"account_id": account_id}, sort=[("period_id", -1)])
        print("last_period_id",last_period_id)
        period = await collection_credit_periods.find_one({"account_id": account_id, "period_id": last_period_id['period_id']})
        if not period:
            raise ValueError(f"No period data found for account_id: {account_id} and period_id: {last_period_id['period_id']}")
        print(period)
        end_date = due_date
        start_date = end_date - timedelta(days=30)

    # call the fucntion of dashboard_new.py
    account_ids = [account_id]
    spending_category = await fetch_top_spending_categories(account_ids, start_date, end_date, total_expenses)
    print("spent_category : ",spending_category)
    
    if not spending_category:
        return CategorySpending(category_name="No Data", total_spent=0.0, category_precentage=0.0)

    category_precentage = (spending_category[0]["total_spent"] / total_expenses) * 100 if total_expenses > 0 else 0.0

    return CategorySpending(category_name=spending_category[0]["category_name"], total_spent=spending_category[0]["total_spent"],category_precentage=category_precentage) 


#current period data
async def fetch_current_period_data(account_id:int):
    account_data = await collection_account.find_one(
        {"account_id": account_id},
        {"credit_limit": 1, "balance": 1, "due_date": 1, "_id": 0}
    )
    
    
    current_credit_limit = account_data.get("credit_limit", 0.0)
    current_due_date=account_data.get("due_date")
    total_credit_available=account_data.get("balance")
    total_credit_used=current_credit_limit - total_credit_available
    return {"current_credit_limit": current_credit_limit, "current_due_date": current_due_date, "total_credit_available": total_credit_available, "total_credit_used": total_credit_used}


async def calculate_insufficient_credit(account_id: int):
    # Fetch account details
    account_data = await collection_account.find_one({"account_id": account_id})
    
    if not account_data:
        return None  # No account found, return None

    due_date = account_data.get("due_date")
    balance = float(account_data.get("balance", 0))  # Ensure balance is float
    today = datetime.utcnow()

    if not due_date or not isinstance(due_date, datetime):
        return None  

    # Expenses from today to due_date
    expense_pipeline = [
        {"$match": {"account_id": account_id, "date": {"$gte": today, "$lte": due_date}, "amount": {"$gt": 0}}},
        {"$group": {"_id": "$account_id", "total_expenses": {"$sum": "$amount"}}}
    ]

    expense_result = await collection_predicted_expense.aggregate(expense_pipeline).to_list(length=1)
    total_expenses = float(expense_result[0]["total_expenses"]) if expense_result else 0.0  # Ensure float

    # Calculate insufficient credit
    insufficient_credit = total_expenses - balance
    result = insufficient_credit if insufficient_credit > 0 else 0.0
    print("result : ",result)
    result2 = {"insufficient_credit": result}
    print("result2", result2)
    return result2


# Check surplus accounts for credit account
async def check_surplus_accounts_for_creditcard( account_id: int,insufficient_credit:float):
    goal_accounts = await collection_goal.distinct("account_id")
    today = datetime.now(timezone.utc)

    # Find eligible accounts 
    eligible_accounts_pipeline = [
        {"$match": {"account_id": {"$ne": account_id}, "account_type": {"$ne": "credit"}, "account_id": {"$nin": goal_accounts}}},
        {"$project": {"account_id": 1, "account_number": 1}}
    ]
    eligible_accounts = await collection_account.aggregate(eligible_accounts_pipeline).to_list(None)

    # Find the minimum balance within the next 30 
    min_balance_pipeline = [
        {"$match": {"account_id": {"$in": [acc["account_id"] for acc in eligible_accounts]}, "date": {"$gte": today, "$lte": today + timedelta(days=30)}}},
        {"$group": {"_id": "$account_id", "min_balance": {"$min": "$balance"}}}
    ]
    min_balances = await collection_predicted_balance.aggregate(min_balance_pipeline).to_list(None)

    # Map balances to accounts
    balance_map = {item["_id"]: item["min_balance"] for item in min_balances}

    
    sufficient_accounts = [
        {
            "account_number": acc["account_number"], 
            "min_balance": balance_map.get(acc["account_id"], 0)
        }
        for acc in eligible_accounts if balance_map.get(acc["account_id"], 0) is not None and balance_map.get(acc["account_id"], 0) >= insufficient_credit

    ]

    return sufficient_accounts 


async def get_previous_expenses(account_id: int, start_date: datetime, period_begin_date: datetime) -> list:
    # Previous expenses pipeline
    past_expenses_pipeline = [
        {"$match": {"account_id": account_id, "date": {"$gte": period_begin_date, "$lte": start_date - timedelta(days=1)}}},
        {
            "$group": {
                "_id": "$date",  # Group by date
                "total_previous_expenses": {"$sum": "$payment"}  # Sum payments for the day
            }
        },
        {"$sort": {"_id": 1}}
    ]
    previous_expenses_data = await collection_transaction.aggregate(past_expenses_pipeline).to_list(None)

    # Convert to dictionary for easy lookup
    previous_expenses_dict = {data["_id"].date(): data["total_previous_expenses"] for data in previous_expenses_data}

    # Create a list of dates and their corresponding expense sums
    previous_expenses = []
    num_days = (start_date - period_begin_date).days + 1
    for i in range(num_days):
        current_date = (period_begin_date + timedelta(days=i)).date()
        previous_expenses.append({
            "date": current_date.strftime("%Y-%m-%d"),
            "total_previous_expenses": previous_expenses_dict.get(current_date, 0)  # Default to 0 if no data
        })
    
    return previous_expenses


async def get_predicted_expenses(account_id: int, start_date: datetime, end_date: datetime) -> list:
    # Predicted expenses pipeline
    expenses_pipeline = [
        {"$match": {"account_id": account_id, "date": {"$gte": start_date, "$lte": end_date}}},  
        {
            "$group": {
                "_id": "$date",  # Group by date
                "total_predicted_expenses": {"$sum": "$amount"}  # Sum predicted expenses for the day
            }
        },
        {"$sort": {"_id": 1}}
    ]
    predicted_expenses_data = await collection_predicted_expense.aggregate(expenses_pipeline).to_list(None)

    # Convert to dictionary for easy lookup
    predicted_expenses_dict = {data["_id"].date(): data["total_predicted_expenses"] for data in predicted_expenses_data}

    # Create a list of dates and their corresponding predicted sums
    predicted_expenses = []
    num_days = (end_date - start_date).days + 1
    for i in range(num_days):
        current_date = (start_date + timedelta(days=i)).date()
        predicted_expenses.append({
            "date": current_date.strftime("%Y-%m-%d"),
            "total_predicted_expenses": predicted_expenses_dict.get(current_date, 0)  # Default to 0 if no data
        })
    
    return predicted_expenses


async def get_previous_account_balances(account_id: int, start_date: datetime, period_begin_date: datetime) -> list:
    # Previous balances pipeline
    past_balances_pipeline = [
        {"$match": {"account_id": account_id, "date": {"$gte": period_begin_date, "$lte": start_date - timedelta(days=1)}}},
        {
            "$group": {
                "_id": "$date",  # Group by date
                "last_balance": {"$last": "$balance"}  # Get the last balance for each date
            }
        },
        {"$sort": {"_id": 1}}
    ]
    previous_balances_data = await collection_transaction.aggregate(past_balances_pipeline).to_list(None)

    # Convert to dictionary for easy lookup
    previous_balances_dict = {data["_id"].date(): data["last_balance"] for data in previous_balances_data}

    # Create a list of dates and their corresponding balances
    previous_balances = []
    num_days = (start_date - period_begin_date).days + 1
    previous_balance = None  # To carry forward the balance if there is a gap
    for i in range(num_days):
        current_date = (period_begin_date + timedelta(days=i)).date()
        balance = previous_balances_dict.get(current_date, previous_balance)
        if balance is not None:
            previous_balance = balance  # Update the balance for the next day
        previous_balances.append({
            "date": current_date.strftime("%Y-%m-%d"),
            "balance": previous_balance
        })
    
    return previous_balances


async def get_predicted_account_balances(account_id: int, start_date: datetime, end_date: datetime) -> list:
    # Predicted balances pipeline
    balances_pipeline = [
        {"$match": {"account_id": account_id, "date": {"$gte": start_date, "$lte": end_date}}},  
        {
            "$group": {
                "_id": "$date",  # Group by date
                "last_balance": {"$last": "$balance"}  # Get the last predicted balance for each date
            }
        },
        {"$sort": {"_id": 1}}
    ]
    predicted_balances_data = await collection_predicted_balance.aggregate(balances_pipeline).to_list(None)

    # Convert to dictionary for easy lookup
    predicted_balances_dict = {data["_id"].date(): data["last_balance"] for data in predicted_balances_data}

    # Create a list of dates and their corresponding predicted balances
    predicted_balances = []
    num_days = (end_date - start_date).days + 1
    for i in range(num_days):
        current_date = (start_date + timedelta(days=i)).date()
        predicted_balances.append({
            "date": current_date.strftime("%Y-%m-%d"),
            "balance": predicted_balances_dict.get(current_date, 0)  # Default to 0 if no data
        })
    
    return predicted_balances


async def graph_data(account_id: int) -> dict:
    start_date = datetime.utcnow()

    # Fetch account data and check if account exists
    account_data = await collection_account.find_one({"account_id": account_id})
    if not account_data:
        return {"error": "Account not found"}

    due_date = account_data.get("due_date")
    
    # Get timeframes
    end_date = due_date
    period_begin_date = due_date - timedelta(days=30)

    # Get previous and predicted expenses separately
    previous_expenses = await get_previous_expenses(account_id, start_date, period_begin_date)
    predicted_expenses = await get_predicted_expenses(account_id, start_date, end_date)

    # Get previous and predicted account balances separately
    previous_balances = await get_previous_account_balances(account_id, start_date, period_begin_date)
    predicted_balances = await get_predicted_account_balances(account_id, start_date, end_date)

    return {
        "previous_expenses": previous_expenses,
        "predicted_expenses": predicted_expenses,
        "previous_balances": previous_balances,
        "predicted_balances": predicted_balances
    }


# Handling Credit Card
async def get_credit_summary(account_id: int,timeperiod:int | None=None):

    if not timeperiod:
        credit_card_summery = await fetch_credit_financial_summary(account_id, timeperiod)
        top_categories=await fetch_most_spent_categories(account_id,credit_card_summery.total_expenses,timeperiod=None) 
        current_period_data=await fetch_current_period_data(account_id)
        insufficient_credit = await calculate_insufficient_credit(account_id)
        sufficient_accounts=await check_surplus_accounts_for_creditcard(account_id,insufficient_credit["insufficient_credit"])# for account suggestion
        pre_graph_data= await graph_data(account_id)
        return credit_card_summery, top_categories, current_period_data, insufficient_credit, sufficient_accounts, pre_graph_data

    else:
        credit_card_summery = await fetch_credit_financial_summary(account_id, timeperiod)
        top_categories=await fetch_most_spent_categories(account_id,credit_card_summery["total_expenses"],timeperiod=None)
        return credit_card_summery,top_categories


async def get_user_name_profile_pic(user_id : int) -> ResponseSchemaUsernameProfilePic:
    user = await collection_user.find_one({"user_id": user_id}, {"_id": 0, "username": 1, "user_image": 1})
    if user:
        user_name=str(decrypt(user["username"]))
        user_image=str(decrypt(user["user_image"]))
        return ResponseSchemaUsernameProfilePic(username=user_name, user_image=user_image)
    else:
        return ResponseSchemaUsernameProfilePic(username="Unknown", user_image="Unknown")