from datetime import datetime, timedelta,timezone
from database import collection_transaction, collection_transaction_category, collection_predicted_balance, collection_predicted_expense, collection_predicted_income,collection_account,collection_credit_periods,collection_goal
from typing import Tuple
from schemas.dashboard import SelectedAccountResponse, SpendingCategory
from typing import List, Dict,Union,Optional,Any

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
        {"account_number":1, "account_type":1, "balance":1,"bank_account":1, "account_id":1}).to_list(length=100)
    account_list = [serialize_document(item) for item in items]
    account_ids = [item.get("account_id") for item in account_list]
    return account_ids, account_list


#most 6 spending categories with the ammount
async def fetch_top_spending_categories(account_ids:list, start_date:datetime, end_date:datetime, total_expenses:float) -> List[SpendingCategory]:
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
        SpendingCategory(category_name=category_map.get(item["_id"], "Unknown"), total_spent=item["total_spent"])
        for item in category_result
    ]

    # Add "Other" category if applicable
    if other_spent > 0 and (other_spent / total_expenses) < 0.3:
        top_categories.append(SpendingCategory(category_name="Other", total_spent=other_spent))

    return top_categories


# get total_income,total_expenses, total_savings for single account or list of account
async def fetch_financial_summary(account_ids:list, start_date:datetime, end_date:datetime) -> Dict[str, float]:
    # make pipeline
    pipeline = [
        {"$match": {"account_id":{"$in": account_ids},"date":{"$gte":start_date, "$lte":end_date}}},
        {"$group": {"_id": None, "total_income": {"$sum": "$receipt"}, "total_expenses": {"$sum": "$payment"}}}
    
    ]
    result = await collection_transaction.aggregate(pipeline).to_list(length=1)
    if not result:
        return {"total_income": 0.0, "total_expenses": 0.0, "total_savings": 0.0} # Default values
    
    aggregated_data = result[0]
    total_income = aggregated_data.get("total_income", 0.0)
    total_expenses = aggregated_data.get("total_expenses", 0.0)
    total_savings = max(total_income - total_expenses, 0.0)
    return {"total_income": total_income, "total_expenses": total_expenses, "total_savings": total_savings}


#past transactions for the graph
async def fetch_past_transactions(account_ids: list, end_date: datetime,days:int) -> List[Dict[str, Any]]:
    start_date_past = end_date - timedelta(days=days)

    transaction_pipeline = [
        {"$match": {"account_id": {"$in": account_ids}, "date": {"$gte": start_date_past, "$lte": end_date - timedelta(days=1)}}},
        {"$project": {"date": 1, "receipt": 1, "payment": 1, "balance": 1}},
        {"$sort": {"date": 1}}
    ]

    transaction_data = await collection_transaction.aggregate(transaction_pipeline).to_list(None)

    past_data = []
    for item in transaction_data:
        if item.get("payment", 0) > 0:
            past_data.append({"date": item["date"], "payment": item["payment"], "balance": item["balance"]})
        if item.get("receipt", 0) > 0:
            past_data.append({"date": item["date"], "receipt": item["receipt"], "balance": item["balance"]})

    return past_data

async def fetch_predicted_data(account_id: list, end_date: datetime, days: int):
    """Fetch upcoming predicted income, expenses, and balances for the given days."""
    
    start_date_future = end_date
    end_date_future = end_date + timedelta(days=days)
    print("???????????????????????????????")
    print("start_date_future : ",start_date_future)
    print("end_date_future : ",end_date_future)

    transaction_pipeline = [
        {"$match": {"account_id": {"$in": account_id}, "date": {"$gte": start_date_future, "$lte": end_date_future}}},
        {"$project": {"date": 1, "amount": 1, "balance": 1}},
        {"$sort": {"date": 1}}
    ]

    predicted_income_data = await collection_predicted_income.aggregate(transaction_pipeline).to_list(None)
    predicted_expense_data = await collection_predicted_expense.aggregate(transaction_pipeline).to_list(None)
    predicted_balance_data = await collection_predicted_balance.aggregate(transaction_pipeline).to_list(None)

    # Convert data to dictionaries for fast lookup (Ensure keys are datetime.date)
    income_dict = {data["date"].date(): data["amount"] for data in predicted_income_data}
    expense_dict = {data["date"].date(): data["amount"] for data in predicted_expense_data}
    balance_dict = {data["date"].date(): data["balance"] for data in predicted_balance_data}

    predicted_data = []
    
    for i in range(days):  # Ensure all 'days' are included
        current_date = (start_date_future + timedelta(days=i)).date()
        
        predicted_data.append({
            "date": current_date.strftime("%Y-%m-%d"),
            "predicted_income": income_dict.get(current_date, 0),
            "predicted_expenses": expense_dict.get(current_date, 0),
            "predicted_balance": balance_dict.get(current_date, 0)
        })

    return predicted_data

## update total income, expense, balance and predicted categories single account or whole account
async def update_second_header(account_id:Union[int, List[int]],start_date:Union[datetime,str], end_date:Union[datetime,str]):

    # converting all the account into list
    account_ids = account_list([account_id] if isinstance(account_id, int) else account_id)

    date_format = "%Y-%m-%d"

    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, date_format)
    
    # Convert end_date to datetime if it is a string
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, date_format)

    financial_summery = await fetch_financial_summary(account_ids,start_date, end_date)
    total_expenses = financial_summery["total_expenses"]
    print("total_expenses category " ,total_expenses)
    spending_category = await fetch_top_spending_categories(account_ids,start_date, end_date, total_expenses)
    #return as a touple
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
        return ["No Data", 0.0]  # Return default if no transactions exist

    most_spent_category_id = category_result[0]["_id"]
    most_spent_amount = category_result[0]["total_spent"]

    # Fetch the category name from the transaction_category collection
    category_data = await collection_transaction_category.find_one({"category_id": most_spent_category_id})
    most_spent_category_name = category_data["category_name"] if category_data else "Unknown"
    return [most_spent_category_name, most_spent_amount]

# load full details
async def load_full_details(user_id:int,start_date: Optional[str] = None,end_date: Optional[str] = None):
    account_ids, account_list = await all_accounts(user_id)
    saving_account_ids = [account["account_id"] for account in account_list if account["account_type"] == "savings"]
    credit_card_ids = [account["account_id"] for account in account_list if account["account_type"] == "credit"]
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("saving_account_ids : ",saving_account_ids)
    print("credit_card_ids : ",credit_card_ids)
    print("account_ids : ",account_ids)
    print("account_list : ",account_list)

    # if date is string convert it into datetime
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
    if isinstance(end_date, str):    
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

    # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>")
    # print("end_date : ",end_date)
    
    if not start_date:
        end_date = datetime.now(timezone.utc)
        start_date = end_date - timedelta(days=30)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("end_date : ",end_date)
        second_header = await update_second_header(saving_account_ids,start_date,end_date)
        past_transaction_100_days = await fetch_past_transactions(saving_account_ids,end_date,100)
        predicted_transaction_7_days = await fetch_predicted_data(saving_account_ids, end_date,8)
        most_spending_category_100_days = await fetch_most_spent_category_100_days(saving_account_ids,end_date) 
        return account_list,second_header, past_transaction_100_days, predicted_transaction_7_days,most_spending_category_100_days
    else:
        return await update_second_header(saving_account_ids,start_date,end_date)
    

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
async def load_specific_account(user_id:int,account_id:int,start_date: Optional[str] = None,end_date: Optional[str] = None):
    account_ids = [account_id]
    if not start_date:
        end_date = datetime.now(timezone.utc)
        start_date = end_date - timedelta(days=30)
        second_header = await update_second_header(account_ids,start_date,end_date)
        past_transaction_100_days = await fetch_past_transactions(account_ids,end_date,100)
        predicted_transaction_7_days = await fetch_predicted_data(account_ids, end_date,8)
        most_spending_category_100_days = await fetch_most_spent_category_100_days(account_ids,end_date)
        negative_balance_prediction= await fetch_minus_predicted_balance(account_id)
        surplus_accounts = await check_surplus_accounts( user_id,account_id)
        return second_header, past_transaction_100_days, predicted_transaction_7_days,most_spending_category_100_days, negative_balance_prediction,surplus_accounts
    else:
        print("start_date",start_date)
        print("end_date",end_date)
        return await update_second_header(account_ids,start_date,end_date)
    

# Financial summaries for credit account
async def fetch_credit_financial_summary(account_id: int, timeperiod:Optional[int] = None ):
    
    if timeperiod:
        # Fetch data from credit_periods collection based on given timeperiod
        credit_summary = await collection_credit_periods.find_one(
            {"account_id": account_id, "period_id": timeperiod},  
            {"credit_limit": 1, "total_expenses": 1, "remaining_balance": 1, "_id": 0}
        )
        if credit_summary:
            return (
                credit_summary.get("credit_limit", 0.0),
                credit_summary.get("total_expenses", 0.0),
                credit_summary.get("remaining_balance", 0.0)
            )
    
    # If timeperiod is not given, fetch data from account_collection
    account_data = await collection_account.find_one(
        {"account_id": account_id},
        {"credit_limit": 1, "balance": 1, "due_date": 1, "_id": 0}
    )
    
    if not account_data:  # Check if account_data is None
        return 0.0, 0.0, 0.0  # Return default values if no account is found

    credit_limit = account_data.get("credit_limit", 0.0)
    total_expenses = account_data.get("balance", 0.0)
    remaining_balance = credit_limit - total_expenses

    return credit_limit, total_expenses, remaining_balance

#most spending categories
async def fetch_most_spent_categories(account_id: int, total_expenses: float,timeperiod: Optional[int] = None):
    
    account_data = await collection_account.find_one({"account_id": account_id})
    due_date = account_data["due_date"]

    if timeperiod:
        period = await collection_credit_periods.find_one({"account_id": account_id, "period_id": timeperiod})
        
        period_id = period["period_id"]
        current_period_start_date = due_date - timedelta(days=30)
        start_date = current_period_start_date - timedelta(days=period_id * 30)
        end_date = start_date + timedelta(days=30)
    else:
        end_date = due_date
        start_date = end_date - timedelta(days=30)

    # call the fucntion of dashboard_new.py
    account_ids = [account_id]
    spending_category = await fetch_top_spending_categories(account_ids, start_date, end_date, total_expenses)
    return spending_category

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

    return current_credit_limit,current_due_date, total_credit_available,total_credit_used


async def calculate_insufficient_credit(account_id: int) -> Optional[float]:
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

    return insufficient_credit if insufficient_credit > 0 else 0.0

# Check surplus accounts for credit account
async def check_surplus_accounts_for_creditcard( account_id: int,insufficient_credit:float) -> List[Dict[str, Any]]:
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

async def graph_data(account_id: int) -> Dict[str, Any]:
    start_date = datetime.utcnow()
    
    # Fetch account data and check if account exists
    account_data = await collection_account.find_one({"account_id": account_id})
    if not account_data:
        return {"error": "Account not found"}

    due_date = account_data.get("due_date")
    
    end_date = due_date
    period_begin_date = due_date - timedelta(days=30)

    # Past expenses pipeline
    past_expenses_pipeline = [
        {"$match": {"account_id": account_id, "date": {"$gte": period_begin_date, "$lte": start_date - timedelta(days=1)}}},
        {"$project": {"_id": 0, "date": 1, "previous_expenses": "$payment"}},
        {"$sort": {"date": 1}}
    ]
    previous_expenses_data = await collection_transaction.aggregate(past_expenses_pipeline).to_list(None)
    print("prvious_expense_data ", previous_expenses_data)

    # Predicted expenses pipeline
    expenses_pipeline = [
        {"$match": {"account_id": account_id, "date": {"$gte": start_date, "$lte": end_date}}},
        {"$project": {"_id": 0, "date": 1, "predicted_expenses": "$amount"}},
        {"$sort": {"date": 1}}
    ]
    predicted_expenses_data = await collection_predicted_expense.aggregate(expenses_pipeline).to_list(None)

    # Return data wrapped in a dictionary
    pre_graph_data = [{"previous_expenses": previous_expenses_data},{"predicted_expenses":predicted_expenses_data}]
    return pre_graph_data

# Handling Credit Card
async def get_credit_summary(account_id: int,timeperiod:int | None=None):

    if not timeperiod:
        credit_limit,total_expenses,remaining_balance = await fetch_credit_financial_summary(account_id, timeperiod)
        top_categories=await fetch_most_spent_categories(account_id,total_expenses,timeperiod=None) 
        current_credit_limit,current_due_date, total_credit_available,total_credit_used=await fetch_current_period_data(account_id)
        insufficient_credit = await calculate_insufficient_credit(account_id)
        sufficient_accounts=await check_surplus_accounts_for_creditcard(account_id,insufficient_credit)
        pre_graph_data= await graph_data(account_id)
        return credit_limit,total_expenses,remaining_balance,top_categories,current_credit_limit,current_due_date,total_credit_available,total_credit_used,insufficient_credit,sufficient_accounts,pre_graph_data

    else:
        credit_limit,total_expenses,remaining_balance = await fetch_credit_financial_summary(account_id, timeperiod)
        top_categories=await fetch_most_spent_categories(account_id,total_expenses,timeperiod=None)
        return credit_limit,total_expenses,remaining_balance,top_categories