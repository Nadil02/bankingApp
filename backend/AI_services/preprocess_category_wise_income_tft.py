import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
import os

def sumOfTheDay(df: pd.DataFrame) -> pd.DataFrame:
    result_df = df.groupby(['Cluster', 'Date']).agg({
    'Receipts': 'sum'  # Sum receipts for same day/cluster
    # 'Balance': 'last'   # Take the last balance for that day/cluster
    }).reset_index()

    # Sort by Cluster and Date within each cluster
    result_df = result_df.sort_values(['Cluster', 'Date'])

    # Display the result
    return result_df


def fillDate(df: pd.DataFrame) -> pd.DataFrame:
    start=df['Date'].min()
    end=df['Date'].max()
    # print("Start Date:", start)
    # print("End Date:", end)

    # Create a complete date range from start to end
    date_range = pd.date_range(start=start, end=end)

    # Get unique clusters
    clusters = df['Cluster'].unique()
    # print("Clusters:", clusters)

    # Create an empty list to store dataframes for each cluster
    all_cluster_dfs = []

    # For each cluster, create a complete date series
    for cluster in clusters:
        # Filter data for this cluster
        cluster_data = df[df['Cluster'] == cluster]
        
        # Create a DataFrame with all dates for this cluster
        cluster_full_dates = pd.DataFrame({'Date': date_range, 'Cluster': cluster})
        
        # Merge actual data with the complete date series
        cluster_complete = pd.merge(
            cluster_full_dates, 
            cluster_data,
            on=['Date', 'Cluster'], 
            how='left'
        )
    
        # Fill missing Receipts with 0 (keep Balance as NaN)
        cluster_complete['Receipts'] = cluster_complete['Receipts'].fillna(0)
    
        # Add to our list
        all_cluster_dfs.append(cluster_complete)

    # print("Number of clusters processed:", len(all_cluster_dfs))
    # Combine all cluster dataframes
    complete_df = pd.concat(all_cluster_dfs)

    # Sort by Cluster and Date
    complete_df = complete_df.sort_values(['Cluster', 'Date'])

    # Reset index
    complete_df = complete_df.reset_index(drop=True)
    # print("Final DataFrame shape after filling dates:", complete_df.shape)

    return complete_df


def handleBalance(file_path1: str) -> pd.DataFrame:
    """
    Reads an Excel file containing transaction data, calculates the balance for each transaction,
    and saves the updated DataFrame to a new Excel file.

    Parameters:
    - file_path: str, path to the input Excel file containing transaction data.

    Returns:
    - DataFrame: Updated DataFrame with a new 'Balance' column.
    """
    # Load the data
    df1 = pd.read_excel(file_path1)

    # drop unncessary columns
    df1 = df1.drop(columns=['Discription','Receipts','cleaned_particulars','Category','Payments','Cluster'])

    # Concatenate the DataFrames
    # combined_df = pd.concat([df1, df2], ignore_index=True)

    combined_df = df1.copy()

    # Convert the 'Date' column to datetime objects if it's not already
    combined_df['Date'] = pd.to_datetime(combined_df['Date'])

    # Sort the DataFrame by 'Date'
    combined_df = combined_df.sort_values(by=['Date'])

    # Reset the index (optional)
    combined_df = combined_df.reset_index(drop=True)

    # Group by 'Date' and get the last balance of each day
    final_df = combined_df.groupby('Date')['Balance'].last().reset_index()

    # Create a date range from the minimum to maximum date in your dataset
    date_range = pd.date_range(start=final_df['Date'].min(), end=final_df['Date'].max(), freq='D')

    # Create a new DataFrame with the complete date range
    all_dates_df = pd.DataFrame({'Date': date_range})

    # Merge the original DataFrame with the complete date range DataFrame
    final_df = pd.merge(all_dates_df, final_df, on='Date', how='left')

    # Forward fill missing balance values
    final_df['Balance'] = final_df['Balance'].ffill()

    final_df2 = final_df.copy()

    # Group by 'Date' and get the last balance of each day
    final_df = final_df.groupby('Date')['Balance'].last().reset_index()

    final_df.to_csv('final_df.csv', index=False)

    # handle outliers in the Balance column

    outliers_df = final_df.copy()
    # Calculate IQR
    Q1 = outliers_df['Balance'].quantile(0.25)
    Q3 = outliers_df['Balance'].quantile(0.75)
    IQR = Q3 - Q1

    # Define bounds
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Apply capping
    outliers_df['Balance'] = outliers_df['Balance'].clip(lower=lower_bound, upper=upper_bound)

    # Normalize the balance column
    # Create the scaler
    scaler = MinMaxScaler()

    # Reshape needed if using a single column (sklearn expects 2D input)
    outliers_df['Balance'] = scaler.fit_transform(outliers_df[['Balance']])

    # Rename the column
    outliers_df2 = outliers_df.rename(columns={'Balance': 'Actual_Balance'})
    # print(outliers_df2)
    return outliers_df2


def outliers(group):
    non_zero_group = group[group['Receipts'] != 0]

    if not non_zero_group.empty:
        Q1 = non_zero_group['Receipts'].quantile(0.25)
        Q3 = non_zero_group['Receipts'].quantile(0.75)
        IQR = Q3 - Q1

        # Step 2: Calculate lower and upper bounds
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        # Cap the outliers instead of removing them
        non_zero_group['Receipts'] = np.clip(non_zero_group['Receipts'], lower_bound, upper_bound)

    # Preserve zero-payment rows
    zero_group = group[group['Receipts'] == 0].copy()
    
    # Concatenate the bounded non-zero group with zero-value rows
    to_df_marked = pd.concat([zero_group, non_zero_group], ignore_index=True)
    to_df_marked.sort_values(by=['Cluster', 'Date'], inplace=True)
    to_df_marked.reset_index(drop=True, inplace=True)


    return to_df_marked


def addFetures(df: pd.DataFrame) -> pd.DataFrame:
    # Days since last transaction
    # Step 1: Make sure 'Date' is in datetime format
    df['Date'] = pd.to_datetime(df['Date'])

    # print("DataFrame shape before feature engineering:", df.shape)
    

    # Step 2: Create an empty list to collect results for each cluster
    results1 = []

    # Step 3: Group by Cluster and calculate days since last transaction
    for cluster_id, group in df.groupby('Cluster'):
        last_txn_date = None
        days_since = []

        # Sort each cluster's data by date
        group = group.sort_values('Date')

        for date, receipt in zip(group['Date'], group['Receipts']):
            if last_txn_date is None:
                days_since.append(None)
            else:
                days_since.append((date - last_txn_date).days)

            if receipt > 0:
                last_txn_date = date

        group = group.copy()
        group['Days_Since_Last_Txn'] = days_since
        results1.append(group)

    # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    # print("results1 shape:", len(results1))


    # Sum of number of last 3 transacions
    # Step 4: Combine all clusters back into a single dataframe
    days_df2 = pd.concat(results1).sort_values(['Cluster', 'Date']).reset_index(drop=True).fillna(0)


    # Ensure Date column is datetime
    days_df2['Date'] = pd.to_datetime(days_df2['Date'])

    # Sort by Cluster and Date
    ddf_final2 = days_df2.sort_values(['Cluster', 'Date'])

    results2 = []

    # Iterate cluster-wise
    for cluster_id, group in days_df2.groupby('Cluster'):
        past_txns = []  # store only past transaction amounts (non-zero)
        total_last_3 = []

        for receipt in group['Receipts']:
            # Calculate sum of last 3 transactions (or fewer if cold start)
            total_last_3.append(sum(past_txns[-3:]))
            
            # If current row has a transaction, add it to past_txns
            if receipt > 0:
                past_txns.append(receipt)

        # Assign back to group
        group = group.copy()
        group['Total_Past_3_Txns'] = total_last_3
        results2.append(group)

    # Combine all clusters back
    df_final4 = pd.concat(results2).sort_index()

    # Average of past 3 transactions
    # Make sure Date is datetime and data is sorted
    df_final4['Date'] = pd.to_datetime(df_final4['Date'])
    df_final4 = df_final4.sort_values(['Cluster', 'Date'])

    results3 = []

    # Iterate over each cluster
    for cluster_id, group in df_final4.groupby('Cluster'):
        past_txns = []  # only track actual (non-zero) transactions
        avg_last_3 = []

        for receipt in group['Receipts']:
            # Cold start-friendly average
            if len(past_txns) == 0:
                avg_last_3.append(0.0)
            else:
                avg_last_3.append(sum(past_txns[-3:]) / len(past_txns[-3:]))
            
            # Only store if it's an actual transaction
            if receipt > 0:
                past_txns.append(receipt)

        # Assign result back to the group
        group = group.copy()
        group['Avg_Past_3_Txns'] = avg_last_3
        results3.append(group)

    # Merge clusters back
    df_final5 = pd.concat(results3).sort_index()

    # Number of transactions last 60 days
    # Ensure datetime and sort properly
    df_final5['Date'] = pd.to_datetime(df_final5['Date'])
    df_final5 = df_final5.sort_values(['Cluster', 'Date'])

    results4 = []

    # Loop through clusters
    for cluster_id, group in df_final5.groupby('Cluster'):
        group = group.copy()
        txn_counts = []

        for idx, row in group.iterrows():
            current_date = row['Date']
            # Lookback window: last 60 days
            window_start = current_date - pd.Timedelta(days=60)

            # Filter to this 60-day window
            past_window = group[(group['Date'] > window_start) & (group['Date'] < current_date)]

            # Count how many of those days had non-zero transactions
            txn_count = (past_window['Receipts'] > 0).sum()

            txn_counts.append(txn_count)

        group['Txns_Past_60_Days'] = txn_counts
        results4.append(group)

    # Combine all results
    df_final6 = pd.concat(results4).sort_index()

    df_final5_edit_2 = df_final6.copy()

    return df_final5_edit_2


def normalizeDF(df: pd.DataFrame) -> pd.DataFrame:
    column_list = ["Days_Since_Last_Txn", "Total_Past_3_Txns", "Avg_Past_3_Txns", "Txns_Past_60_Days"]

    # Step 1: Remove outliers using IQR method for each cluster
    def cap_outliers(group):
        for col in column_list:
            if not group.empty:
                Q1 = group[col].quantile(0.25)
                Q3 = group[col].quantile(0.75)
                IQR = Q3 - Q1

                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR

                group[col] = np.clip(group[col], lower_bound, upper_bound)
        return group

    df = pd.DataFrame(df.groupby('Cluster', group_keys=False).apply(cap_outliers))
    df.sort_values(by=['Cluster', 'Date'], inplace=True)
    df.reset_index(drop=True, inplace=True)

    # Step 2: Normalize columns within each cluster
    normalized_chunks = []
    for cluster in df['Cluster'].unique():
        cluster_df = df[df['Cluster'] == cluster].copy()
        scaler = MinMaxScaler()

        cluster_df[column_list] = scaler.fit_transform(cluster_df[column_list])
        normalized_chunks.append(cluster_df)

    # Combine all normalized clusters
    final_df = pd.concat(normalized_chunks)
    final_df.sort_values(['Cluster', 'Date'], inplace=True)
    final_df.reset_index(drop=True, inplace=True)

    return final_df


def process_transactions(file_path: str, balancedf:pd.DataFrame, expensesdf:pd.DataFrame):
    """
    Processes transaction data from an Excel/csv file, cleans it, and saves the processed data to a CSV file.

    Parameters:
    - file_path: str, path to the input Excel file containing transaction data.
    - output_path: str, optional, path to save the processed CSV file. If None, does not save.

    Returns:
    - DataFrame: Processed transaction data.
    """
    # Load the data
    df = pd.read_excel(file_path)

    # Display initial information
    print("Initial DataFrame shape:", df.shape)
    print("Columns:", df.columns.tolist())

    # drop unnecessary columns
    df = df.drop(columns=['Discription','Payments','cleaned_particulars','Category','Balance'])

    # Convert each column into there original data format
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    # df['Balance'] = pd.to_numeric(df['Balance'], errors='coerce') because Balance not in this dataframe
    df['Cluster'] = pd.to_numeric(df['Cluster'], errors='coerce')
    df['Receipts'] = pd.to_numeric(df['Receipts'], errors='coerce')

    # Check if there is any NaN or NaT colums available
    df.isnull().any()
    
    # Group the dataframe by Cluster and sort by Date within each group
    clustered_df = df.sort_values(['Cluster', 'Date']).reset_index(drop=True)

    # In same category if many transaction happend in single day take sum of the transactions
    result_df = sumOfTheDay(clustered_df)
    # print("Grouped DataFrame shape:", result_df.shape) # correct untill this point

    # Take start date and end date and fill the all days in between that start date and end date
    complete_df = fillDate(result_df)
    print("Filled DataFrame shape:", complete_df.shape) # correct untill this point

    # Merge the two dataframes (complete_df and balancedf)
    filtered_df2 = complete_df.copy()
    outliers_df2 = balancedf.copy()
    expenses_df2 = expensesdf.copy()    

    # First, ensure Date is in datetime format in both dataframes
    filtered_df2['Date'] = pd.to_datetime(filtered_df2['Date'])
    outliers_df2['Date'] = pd.to_datetime(outliers_df2['Date'])
    expenses_df2['Date'] = pd.to_datetime(expenses_df2['Date'])


    # Merge the dataframes on Date column
    merged_df = pd.merge(
        filtered_df2,
        outliers_df2[['Date', 'Balance']], 
        on='Date',
        how='left'
    )

    merged_df = pd.merge(
        merged_df,
        expenses_df2[['Date', 'Payments']], 
        on='Date',
        how='left'
    )

    # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    # print("Merged DataFrame shape:", merged_df.shape) # correct untill this point
    # remove outliers of each cluster
    # listIQR  = []
    merged_df_new3 = merged_df.copy()
    df_marked4 = merged_df_new3.groupby('Cluster', group_keys=False).apply(outliers)

    # print("Outliers removed DataFrame shape:", df_marked4.shape) # correct untill this point
    

    # no need to do normalization for Receipts column

    complete_normalized_df2 = df_marked4.copy()

    # feature engineering
    df_final5_edit_2 = addFetures(complete_normalized_df2)

    # print("Feature Engineering DataFrame shape:", df_final5_edit_2.shape) # correct untill this point

    # normalize fetures
    # df_final5_edit_2  = normalizeDF(df_final5_edit_2)
    df_final5_edit_3 = df_final5_edit_2.copy()

    # add some more features 
    # Day of week (Monday=0, Sunday=6)
    df_final5_edit_3['DayOfWeek'] = df_final5_edit_3['Date'].dt.dayofweek
    df_final5_edit_3['DayOfWeek_sin'] = np.sin(2 * np.pi * df_final5_edit_3['DayOfWeek'] / 7)
    df_final5_edit_3['DayOfWeek_cos'] = np.cos(2 * np.pi * df_final5_edit_3['DayOfWeek'] / 7)

    # Month (January=1, December=12)
    df_final5_edit_3['Month'] = df_final5_edit_3['Date'].dt.month
    df_final5_edit_3['Month_sin'] = np.sin(2 * np.pi * df_final5_edit_3['Month'] / 12)
    df_final5_edit_3['Month_cos'] = np.cos(2 * np.pi * df_final5_edit_3['Month'] / 12)
    df_final5_edit_3['Transaction_Happened'] = (df_final5_edit_3['Receipts'] > 0).astype(int)

    df_final5_edit_3.drop(columns=['DayOfWeek', 'Month'], inplace=True)

    # Make sure the data is sorted by Cluster and Date
    df_final6_3 = df_final5_edit_3.sort_values(['Cluster', 'Date'])

    # Add time index (starts from 0 for each cluster)
    df_final6_3['time_idx'] = df_final6_3.groupby('Cluster').cumcount()

    # 4. Save or return
    # if output_path:
    #     out_ext = os.path.splitext(output_path)[-1].lower()
    #     if out_ext == '.csv':
    #         df_final6_3.to_csv(output_path, index=False)
    #     elif out_ext in ['.xls', '.xlsx']:
    #         df_final6_3.to_excel(output_path, index=False)
    #     else:
    #         raise ValueError("Unsupported output file format")

    print("Processed DataFrame shape:", df_final6_3)
    df_final6_3.to_excel('processed_transactions.xlsx', index=False)
    return df_final6_3

# remove outliers and do the normalization
def treatBalance(balance_path: str) -> pd.DataFrame:

    df = pd.read_excel(balance_path)

    df['Balance'] = df['Balance'].astype(str).str.replace(r'[^\d.-]', '', regex=True)
    df['Balance'] = pd.to_numeric(df['Balance'], errors='coerce')
    non_numeric_values = df['Balance'][df['Balance'].apply(lambda x: not isinstance(x, (int, float)))]
    print(non_numeric_values)

    # Calculate IQR
    Q1 = df['Balance'].quantile(0.25)
    Q3 = df['Balance'].quantile(0.75)
    IQR = Q3 - Q1

    # Define bounds
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

        # Apply capping
    df['Balance'] = df['Balance'].clip(lower=lower_bound, upper=upper_bound)

    # Normalize the balance column
    # Create the scaler
    # scaler = MinMaxScaler()
    # Reshape needed if using a single column (sklearn expects 2D input)
    # df['Balance'] = scaler.fit_transform(df[['Balance']])

    # Rename the column
    # outliers_df2 = df.rename(columns={'Balance': 'Actual_Balance'})
    outliers_df2 = df.copy()
    print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
    print("Outliers removed DataFrame:", outliers_df2)
    # print(outliers_df2)
    return outliers_df2

# remove outliers and do the normalization
def treatExpenses(expenses_path: str) -> pd.DataFrame:

    df = pd.read_excel(expenses_path)

    # Calculate IQR
    Q1 = df['Payments'].quantile(0.25)
    Q3 = df['Payments'].quantile(0.75)
    IQR = Q3 - Q1

    # Define bounds
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

        # Apply capping
    df['Payments'] = df['Payments'].clip(lower=lower_bound, upper=upper_bound)

    # Normalize the balance column
    # Create the scaler
    # scaler = MinMaxScaler()
    # Reshape needed if using a single column (sklearn expects 2D input)
    # df['Payments'] = scaler.fit_transform(df[['Payments']])

    # Rename the column
    # outliers_df2 = df.rename(columns={'Balance': 'Actual_Balance'})
    outliers_df2 = df.copy()
    # print(outliers_df2)
    print("EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
    print("Outliers removed DataFrame:", outliers_df2)
    return outliers_df2





# Optional test usage
if __name__ == "__main__":

    # create balance column by using full transactions and income dataset
    # correctBalance = handleBalance("shiharaResults.xlsx")
    # print("***************************************************")

    newBalance = treatBalance("fullBalance.xlsx")
    newExpenses = treatExpenses("fullExpense.xlsx")

    # preprocess the transactions
    processed = process_transactions("nadilDataSetWithmin5incomesv3.xlsx", newBalance, newExpenses)
    print(processed.head())
    # print("Processing complete. Rows:", len(processed))