from database import collection_bank
import asyncio

async def get_bank_rates(bank_id):
    try:
        bank = await collection_bank.find_one({"bank_id": bank_id})  # Await the async query
        if not bank:
            return {"error": "Bank not found. Please check the bank ID."}
        
        rates = {
            "Savings Accounts": [
                {"account_type": rate.get("account_type", "Unknown"), "interest_rate": rate.get("interest_rate", 0)}
                for rate in bank.get("rates", []) if rate.get("type") == "savings"
            ],
            "Fixed Deposits": [
                {"term": rate.get("term", "Unknown"), "interest_rate": rate.get("interest_rate", 0)}
                for rate in bank.get("rates", []) if rate.get("type") == "fixed_deposit"
            ],
            "Loans": [
                {"term": rate.get("term", "Unknown"), "interest_rate": rate.get("interest_rate", 0)}
                for rate in bank.get("rates", []) if rate.get("type") == "loan"
            ]
        }
        return rates
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}

# Example usage:
bank_id = 20
rates_info = asyncio.run(get_bank_rates(bank_id))  # Run the async function
print(rates_info)
