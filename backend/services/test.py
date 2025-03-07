from datetime import datetime
from llmAgentTools import get_total_spendings_for_given_time_period


#add tools here
tools = [
    {
        "name": "get_total_spendings_for_given_time_period", 
        "func": get_total_spendings_for_given_time_period, 
        "description": "Retrieves the total amount spent by a user within a specified time period. Required parameters: user_id (string), start_date (datetime), end_date (datetime). Use this when the user asks about their spending or expenses for a specific time range."
    },
    {
        "name": "get_total_incomes_for_given_time_period", 
        "func": get_total_incomes_for_given_time_period, 
        "description": "Calculates the total income received by a user within a specified time period. Required parameters: user_id (string), start_date (datetime), end_date (datetime). Use this when the user asks about their income or earnings for a specific time range."
    },
    {
        "name": "get_last_transaction", 
        "func": get_last_transaction, 
        "description": "Retrieves the most recent transaction for a specified user. Required parameters: user_id (string). Use this when the user asks about their latest or most recent transaction."
    },
    {
        "name": "get_monthly_summary_for_given_month", 
        "func": get_monthly_summary_for_given_month, 
        "description": "Provides a summary of total income and spending for a specified month. Required parameters: user_id (string), month (integer 1-12). Use this when the user asks for a financial summary for a specific month."
    },
    {
        "name": "get_all_transactions_for_given_date", 
        "func": get_all_transactions_for_given_date, 
        "description": "Retrieves all transactions that occurred on a specific date for a user. Required parameters: user_id (string), date (datetime). Use this when the user wants to see all transactions from a particular date."
    },
    {
        "name": "get_next_month_total_incomes", 
        "func": get_next_month_total_incomes, 
        "description": "Forecasts the total expected income for the upcoming month based on predicted data. Required parameters: user_id (string). Use this when the user asks about expected or future income for next month."
    },
    {
        "name": "get_next_month_total_spendings", 
        "func": get_next_month_total_spendings, 
        "description": "Forecasts the total expected spending for the upcoming month based on predicted data. Required parameters: user_id (string). Use this when the user asks about expected or future expenses for next month."
    },
    {
        "name": "get_next_income", 
        "func": get_next_income, 
        "description": "Identifies the next expected income transaction based on predicted data. Required parameters: user_id (string). Use this when the user asks when they'll receive their next income or payment."
    },
    {
        "name": "get_next_spending", 
        "func": get_next_spending, 
        "description": "Identifies the next expected expense based on predicted data. Required parameters: user_id (string). Use this when the user asks about their next upcoming expense or bill."
    },
    {
        "name": "handle_incomplete_time_periods", 
        "func": handle_incomplete_time_periods, 
        "description": "Helps manage queries with missing date parameters by prompting for the required information. Required parameters: user_id (string), start_date (datetime, optional), end_date (datetime, optional). Use this when the user's query is missing date information needed for financial analysis."
    }
]


# Test the function
def test_spending_function():
    # Set test parameters
    test_user_id = "1"  # The user ID you mentioned
    test_start_date = datetime(2025, 2, 1)  # Beginning of February 2025
    test_end_date = datetime(2025, 2, 28)   # End of February 2025
    
    # Call the function
    result = get_total_spendings_for_given_time_period(test_user_id, test_start_date, test_end_date)
    
    # Print the result
    print(result)
    
    # Test another date range to verify
    test_start_date2 = datetime(2025, 1, 1)
    test_end_date2 = datetime(2025, 1, 31)
    result2 = get_total_spendings_for_given_time_period(test_user_id, test_start_date2, test_end_date2)
    print(result2)

# Run the test
if __name__ == "__main__":
    test_spending_function()