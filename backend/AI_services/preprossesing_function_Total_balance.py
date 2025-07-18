#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def preprocess_balance_data(input_excel_path, output_excel_path='featured_dataset.xlsx', output_csv_path='featured_dataset.csv'):
    """
    Preprocess balance data from an Excel file and return normalized datasets.
    
    Parameters:
    -----------
    input_excel_path : str
        Path to the input Excel file containing the balance data
    output_excel_path : str, optional
        Path to save the processed Excel file (default: 'featured_dataset.xlsx')
    output_csv_path : str, optional
        Path to save the processed CSV file (default: 'featured_dataset.csv')
    
    Returns:
    --------
    tuple
        (processed DataFrame, Excel file path, CSV file path, min_balance, max_balance)
    """
    # Read the Excel file
    df = pd.read_excel(input_excel_path)
    
    # Extract and prepare balance data
    df_balance = df[["Date", "Balance"]].copy()
    df_balance = df_balance.drop(0)
    df_balance['Date'] = pd.to_datetime(df_balance['Date'])
    
    # Clean and convert Balance column to numeric
    # Remove any non-numeric values and convert to float
    df_balance['Balance'] = pd.to_numeric(df_balance['Balance'], errors='coerce')
    
    # Drop rows where Balance is NaN (were non-numeric)
    df_balance = df_balance.dropna(subset=['Balance'])
    
    # Group by date and sort
    df_balance = df_balance.groupby('Date', as_index=False).last()
    df_balance = df_balance.sort_values('Date')
    df_balance = df_balance.set_index('Date')
    
    # Create full date range and reindex
    full_index = pd.date_range(start=df_balance.index.min(), end=df_balance.index.max(), freq='D')
    df_balance = df_balance.reindex(full_index)
    df_balance['Balance'] = df_balance['Balance'].ffill()
    df_balance = df_balance.reset_index().rename(columns={'index': 'Date'})
    
    # Remove outliers using IQR method
    Q1 = df_balance['Balance'].quantile(0.25)
    Q3 = df_balance['Balance'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df_balance = df_balance[(df_balance['Balance'] > lower_bound) & (df_balance['Balance'] < upper_bound)]
    
    # Get min and max values for denormalization
    min_balance = df_balance['Balance'].min()
    max_balance = df_balance['Balance'].max()
    
    # Normalize the balance
    df_balance['Normalized_Balance'] = (df_balance['Balance'] - min_balance) / (max_balance - min_balance)
    
    # Create final dataset with features
    df_final = df_balance[['Date', 'Normalized_Balance']].copy()
    
    # Add cyclic features for day of week
    df_final['dayofweek'] = pd.to_datetime(df_final['Date']).dt.dayofweek
    df_final['dayofweek_sin'] = np.sin(2 * np.pi * df_final['dayofweek']/7)
    df_final['dayofweek_cos'] = np.cos(2 * np.pi * df_final['dayofweek']/7)
    df_final.drop('dayofweek', axis=1, inplace=True)
    
    # Add rolling window features
    df_final['balance_1d_ago'] = df_final['Normalized_Balance'].shift(1)
    df_final['balance_7d_ago'] = df_final['Normalized_Balance'].shift(7)
    df_final['balance_30d_ago'] = df_final['Normalized_Balance'].shift(30)
    
    # Add rolling mean features
    df_final['rolling_mean_7d'] = df_final['Normalized_Balance'].rolling(window=7).mean()
    df_final['rolling_mean_30d'] = df_final['Normalized_Balance'].rolling(window=30).mean()
    
    # Add rolling std features
    df_final['rolling_std_7d'] = df_final['Normalized_Balance'].rolling(window=7).std()
    df_final['rolling_std_30d'] = df_final['Normalized_Balance'].rolling(window=30).std()
    
    # Add balance change indicator
    df_final['balance_changed'] = (df_final['Normalized_Balance'] != df_final['balance_1d_ago']).astype(int)
    
    # Forward fill NaN values using the newer syntax
    df_final = df_final.ffill()
    
    # Save to Excel and CSV
    df_final.to_excel(output_excel_path, index=False)
    df_final.to_csv(output_csv_path, index=False)
    
    return df_final, output_excel_path, output_csv_path, min_balance, max_balance

# Example usage:
if __name__ == "__main__":
    # Example of how to use the function
    df_processed, excel_path, csv_path, min_bal, max_bal = preprocess_balance_data(
        input_excel_path=r"C:\level2Sem1\AI_software_project\testing\final_evaluation\no_test.xlsx", # type: ignore
        output_excel_path=r"C:\level2Sem1\AI_software_project\testing\final_evaluation\nadilFinalizedDatasetAcBalanceV2.xlsx", # type: ignore
        output_csv_path=r"C:\level2Sem1\AI_software_project\testing\final_evaluation\nadilFinalizedDatasetAcBalanceV2.csv" # type: ignore
    )
    print(f"Processed data saved to:\nExcel: {excel_path}\nCSV: {csv_path}")
    print(f"\nScaling information:")
    print(f"Minimum balance: {min_bal}")
    print(f"Maximum balance: {max_bal}")

#%%
