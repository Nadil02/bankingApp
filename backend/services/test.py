from datetime import datetime
from llmAgentTools import get_total_spendings_for_given_time_period

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