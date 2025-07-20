import asyncio
import os
import sys
import pandas as pd
import re
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.preprocessing import StandardScaler,normalize
from sklearn.cluster import DBSCAN
from sklearn.metrics.pairwise import cosine_similarity

# Add the parent directory to Python path to find database.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import collection_transaction_category_changes, collection_category_name_changes, collection_transaction, collection_transaction_category

#this need to be integrated with data income pipeline
# df = pd.read_excel(r'C:\level2Sem1\AI_software_project\testing\ShiharaFinalizedDatasetReceipts.xlsx') # type: ignore
# df = pd.read_excel(r'C:\level2Sem1\AI_software_project\testing\ShiharaFinalizedDatasetExpenses.xlsx') # type: ignore
# df = pd.read_excel(r'C:\level2Sem1\AI_software_project\testing\nadilFinalizedDatasetExpenses.xlsx') # type: ignore
# df = pd.read_excel(r'C:\level2Sem1\AI_software_project\testing\nadilFinalizedDatasetIncomes.xlsx') # type: ignore
df = pd.read_excel(r'C:\level2Sem1\AI_software_project\testing\credit_card_monthly_cycle.xlsx') # type: ignore

account_id = 3

pd.set_option('display.max_rows', None)  
pd.set_option('display.max_columns', None) 

abbreviations = {
    'PYT': 'payment',
    'TRF': 'transfer',
    'DEP': 'deposit',
    'WDL': 'withdrawal',
    'WD': 'withdrawal',
    'POS': 'point of sale',
    'ATM': 'atm withdrawal',
    'CHQ': 'cheque',
    'DD': 'demand draft',
    'BT': 'bank transfer',
    'ACH': 'automated clearing house',
    'NEFT': 'national electronic funds transfer',
    'RTGS': 'real-time gross settlement',
    'IMPS': 'immediate payment service',
    'UPI': 'unified payments interface',
    'INT': 'interest',
    'CHG': 'charge',
    'FEE': 'fee',
    'TXN': 'transaction',
    'REV': 'reversal',
    'EMI': 'equated monthly installment',
    'CC': 'credit card',
    'POS REF': 'point of sale refund',
    'BIL': 'bill payment',
    'BILP': 'bill payment',
    'INV': 'investment',
    'REF': 'refund',
    'SAL': 'salary credit',
    'SL': 'salary credit',
    'TFR': 'transfer'
}

category_keywords = {
    "Clothing and Apparel": ["nolimit", "piyara fashion", "spring & summer", "kandy", "cool planet", "odel", "mimosa", "zigzag", "super fashion"],
    "Grocery": ["keels", "foodcity", "sinhala", "cargills", "luluhyper", "laugfs super market"],
    "Electronics": ["dialog", "sri lanka telecom", "mobitel", "samsung", "huawei", "lg"],
    "Home Appliances": ["abans", "lg", "singer", "damro"],
    "Restaurants": ["kfc", "pizza hut", "burger king", "dominos", "sarasavi"],
    "Fuel": ["lanka fuel", "caltex", "shell", "petrol", "diesel"],
}

# Normalize Capitalization and Expand Abbreviations
def clean_text(text, abbr_dict):
    text = text.lower()

    # Expand abbreviations
    for abbr, full_form in abbr_dict.items():
        text = re.sub(rf'\b{abbr.lower()}\b', full_form.lower(), text)

    text = re.sub(r'\s+', ' ', text).strip() #remove extra spaces

    return text

# Apply text cleaning to 'cleaned_particulars' column
df['cleaned_particulars'] = df['Discription'].apply(lambda x: clean_text(str(x), abbreviations))

# Categorize based on Keywords
def categorize_by_keywords(description):
    description_lower = description.lower()
    for category, keywords in category_keywords.items():
        if any(keyword in description_lower for keyword in keywords):
            return category
    return "Uncategorized"

# Apply categorization for key words
df['Category'] = df['cleaned_particulars'].apply(lambda x: categorize_by_keywords(x))
#Separate Uncategorized Transactions
uncategorized_df = df[df['Category'] == "Uncategorized"].copy()

# Initialize the sentence transformer model
# model = SentenceTransformer('all-mpnet-base-v2')
model = SentenceTransformer('sentence-transformers/gtr-t5-large')
# Generate embeddings for the cleaned text of uncategorized transactions
uncategorized_embeddings = model.encode(uncategorized_df['cleaned_particulars'].tolist())



scaler = StandardScaler()
uncategorized_embeddings_scaled = scaler.fit_transform(uncategorized_embeddings)

uncategorized_embeddings_normalized = normalize(uncategorized_embeddings_scaled)
similarity_matrix = cosine_similarity(uncategorized_embeddings_normalized)
# Convert similarity to distance (1 - similarity)
distance_matrix = 1 - similarity_matrix

# Ensure the distance matrix has no negative values
distance_matrix = np.clip(distance_matrix, 0, None)

dbscan_model = DBSCAN(eps=0.4, min_samples=5, metric="precomputed")  
cluster_labels = dbscan_model.fit_predict(distance_matrix) 

#Add the cluster labels to the uncategorized dataframe
uncategorized_df['Cluster'] = cluster_labels

predefined_categories = list(category_keywords.keys())
unique_categories = df['Category'].unique()

for category in predefined_categories:
    if category in unique_categories:
        max_label=cluster_labels.max()
        unique_predefined=df[df['Category'].isin(predefined_categories)]['Category'].unique()
        category_id_mapping={}
        new_id=max_label+1
        for category_ in unique_predefined:
            category_id_mapping[category_]=new_id
            new_id+=1
        print(category_id_mapping)
        df['Cluster'] = df['Category'].map(category_id_mapping)
        break

# Automatically Identify Cluster Names Based on Frequent Descriptions
def get_most_frequent_description(cluster_data):
    # Count occurrences of each description in the cluster
    description_counts = cluster_data['cleaned_particulars'].value_counts()
    # Return the most frequent description
    return description_counts.idxmax()

# Function to automatically assign a name to a cluster based on the most frequent description
def assign_cluster_name(cluster_data):
    # Get the most frequent description in the cluster
    most_frequent_description = get_most_frequent_description(cluster_data)
    # Return the most frequent description as the cluster name
    return most_frequent_description.upper()

# Function to clean cluster names by removing numbers and random strings
def clean_cluster_name(name):
    # Remove non-alphabetical characters (including numbers and special characters)
    name = re.sub(r'[^a-zA-Z\s]', '', name)
    return name.strip()

# Function to map the cluster name to a predefined category (if applicable)
def map_to_predefined_category(cluster_name):
    # Clean the cluster name first
    clean_name = clean_cluster_name(cluster_name)
    
    for category, keywords in category_keywords.items():
        if any(keyword in clean_name.lower() for keyword in keywords):
            return category
    return clean_name  # If no match, return the generated cluster name

print("\n=== Predefined Categories ===")
for category in category_keywords.keys():
    category_transactions = df[df['Category'] == category]
    if not category_transactions.empty:
        print(f"\nCategory: {category}")
        print(category_transactions[['Date', 'Discription', 'Payments', 'Receipts', 'Balance']])

print("\n=== Clustered Categories ===")
unique_clusters = set(cluster_labels)
# Update uncategorized_df with cluster labels, then print the clustered data
for cluster in unique_clusters:
    # Filter rows for the current cluster
    cluster_data = uncategorized_df[uncategorized_df['Cluster'] == cluster]
    
    # If the cluster label is -1 (indicating no cluster), categorize it as "Uncategorized"
    if cluster == -1:
        uncategorized_df.loc[uncategorized_df['Cluster'] == cluster, 'Category'] = 'Uncategorized'
        continue
    
    # Automatically assign a name to the cluster based on the most frequent description
    cluster_name = assign_cluster_name(cluster_data)
    
    # Map the cluster name to a predefined category (if applicable)
    category_name = map_to_predefined_category(cluster_name)
    
    # Update the 'Category' column for this cluster
    uncategorized_df.loc[uncategorized_df['Cluster'] == cluster, 'Category'] = category_name

    print(f"\nCategory: {category_name}")
    print(cluster_data[['Date', 'Discription', 'Payments', 'Receipts', 'Balance']])

# After clustering, print any "Uncategorized" data
uncategorized_transactions_after_clustering = uncategorized_df[uncategorized_df['Category'] == 'Uncategorized']
if not uncategorized_transactions_after_clustering.empty:
    print("\nCategory: Uncategorized (After Clustering)")
    print(uncategorized_transactions_after_clustering[['Date', 'Discription', 'Payments', 'Receipts', 'Balance']])

# Merge the categorized and clustered results back into the main dataframe
df = pd.concat([df[df['Category'] != "Uncategorized"], uncategorized_df], ignore_index=True)

print("\n=== All Cluster Names ===")
for cluster in unique_clusters:
    if cluster == -1:
        print("Cluster: Uncategorized")
        continue

    # Filter rows for the current cluster
    cluster_data = uncategorized_df[uncategorized_df['Cluster'] == cluster]

    # Automatically assign a name to the cluster based on the most frequent description
    cluster_name = assign_cluster_name(cluster_data)

    # Print the cluster name
    print(f"Cluster {cluster}: {cluster_name}")


async def get_category_changes_by_account(account_id: int):
    """Get all category changes for a specific account"""
    
    # Get transaction category changes
    transaction_changes = await collection_transaction_category_changes.find(
        {"account_id": account_id}
    ).to_list(length=None)
    
    # Get category name changes
    name_changes = await collection_category_name_changes.find(
        {"account_id": account_id}
    ).to_list(length=None)
    
    return {
        "transaction_category_changes": transaction_changes,
        "category_name_changes": name_changes
    }

async def apply_stored_changes_by_account(df, account_id: int):
    """Apply stored changes for a specific account to the dataframe"""
    
    changes = await get_category_changes_by_account(account_id)
    
    if changes['category_name_changes'] is not None:
        # Apply category name changes
        name_change_map = {}
        for change in changes["category_name_changes"]:
            old_name = change.get('old_category_name')
            new_name = change.get('new_category_name')
            if old_name and new_name:
                name_change_map[old_name] = new_name
        
        # Update category names in dataframe for this account
        if name_change_map:
            df.loc['Category'] = df.loc['Category'].replace(name_change_map)
    else:
        print("No category name changes found for this account.")
    
    if changes['transaction_category_changes'] is None:
        print("No transaction category changes found for this account.")
        return df
    available_categories = set(df['Category'].unique())
    # Apply transaction category changes
    for change in changes["transaction_category_changes"]:
        new_category = change.get('new_category')
        old_category = change.get('previous_category')
        change_date= change.get('transaction_date')
        change_detail= change.get('transaction_detail')

        if old_category is None or new_category is None:
            print(f"Warning: Could not get category names for change: old_id={old_category}, new_id={new_category}")
            continue
        if old_category not in available_categories or new_category not in available_categories:
            print(f"Warning: Old category '{old_category}' not found in dataframe. Available: {available_categories}")
            continue
        # Find transaction by date and description
        if change_date and change_detail:
            try:
                # Convert date to comparable format
                if isinstance(change_date, str):
                    change_date = pd.to_datetime(change_date).date()
                elif hasattr(change_date, 'date'):
                    change_date = change_date.date()
                
                # Create masks for date and description matching
                date_mask = pd.to_datetime(df['Date']).dt.date == change_date
                detail_mask = df['Discription'].str.contains(change_detail, case=False, na=False, regex=False)
                
                # Find rows that match both date and description
                matching_mask = date_mask & detail_mask
                
                if matching_mask.any():
                    matching_rows = df[matching_mask]
                    print(f"Found {len(matching_rows)} transaction(s) matching date {change_date} and detail '{change_detail}'")
                    
                    # Check which of the matching rows have the old category
                    old_category_mask = matching_rows['Category'] == old_category
                    
                    if old_category_mask.any():
                        # Get the final mask for rows to update (date + description + old category)
                        final_mask = matching_mask & (df['Category'] == old_category)
                        
                        rows_to_update = final_mask.sum()
                        print(f"Found {rows_to_update} row(s) with old category '{old_category}' to update to '{new_category}'")
                        
                        # Update the category for matching rows
                        df.loc[final_mask, 'Category'] = new_category
                        
                        print(f"Successfully updated {rows_to_update} transaction(s) from '{old_category}' to '{new_category}'")
                        
                    else:
                        current_categories = matching_rows['Category'].unique()
                        print(f"Warning: No matching rows have old category '{old_category}'. Found categories: {current_categories}")
                        
                else:
                    print(f"Warning: No transactions found matching date {change_date} and detail '{change_detail}'")
                    
            except Exception as e:
                print(f"Error processing change for date {change_date}, detail '{change_detail}': {e}")
                continue
        else:
            print(f"Warning: Missing date or detail for transaction change.")
    return df

df['account_id'] = account_id
df.to_excel('creditCardDataSetWithmin5expensesv4.xlsx',index=False) 

async def update_mongodb_with_transactions(df, account_id):

    existing_special_category = await collection_transaction_category.find_one({
        "account_id": account_id,
        "category_id": -20
    })
    
    # Only clear existing categories if category_id = -10 exists
    if existing_special_category:
        print(f"Found category_id = -20 for account {account_id}. Clearing existing transactions...")
        await collection_transaction.delete_many({"account_id": account_id})
    else:
        print(f"No category_id = -20 found for account {account_id}. Keeping existing transactions...")

    # Get the maximum transaction_id from the collection
    max_transaction = await collection_transaction.find_one(
        {}, 
        sort=[("transaction_id", -1)]
    )
    
    # Start from 1 if no transactions exist, otherwise increment from max
    next_transaction_id = 1 if max_transaction is None else max_transaction.get("transaction_id", 0) + 1

    # Create a copy of the dataframe to avoid modifying the original
    df_copy = df.copy()

    columns_to_drop = ['cleaned_particulars','Category']  
    df_copy = df_copy.drop(columns=columns_to_drop, errors='ignore')


    # Rename columns to match MongoDB schema
    column_mapping = {
        'Date': 'date',
        'Discription': 'description', 
        'Payments': 'payment',
        'Receipts': 'receipt',
        'Balance': 'balance',
        'Cluster': 'category_id',
        'account_id': 'account_id'
    }
    
    df_copy = df_copy.rename(columns=column_mapping)

    # Add auto-incrementing transaction_id
    df_copy['transaction_id'] = range(next_transaction_id, next_transaction_id + len(df_copy))

    # Convert dataframe to list of dictionaries for MongoDB insertion
    records = df_copy.to_dict('records')

    # Insert new data into MongoDB
    if records:
        await collection_transaction.insert_many(records)
        print(f"Successfully inserted {len(records)} records for account_id {account_id}")
    else:
        print("No records to insert")

    # print(df.to_string())
    if df['Payments'].isna().any():
        print("Found NaN values in payments column. adding category ID -10...")
        # Add a special category with ID -10 for NaN payments
        special_category = {
            'account_id': account_id,
            'category_id': -20,  # Special category ID for NaN payments
            'category_name': 'flag category'
        }
        await collection_transaction_category.insert_one(special_category)
    

async def store_categories_in_mongodb(df, account_id):
    """Store category information in collection_transaction_category using DataFrame data"""
    
    existing_special_category = await collection_transaction_category.find_one({
        "account_id": account_id,
        "category_id": -10
    })
    
    # Only clear existing categories if category_id = -10 exists
    if existing_special_category:
        print(f"Found category_id = -10 for account {account_id}. Clearing existing categories...")
        await collection_transaction_category.delete_many({"account_id": account_id})
    else:
        print(f"No category_id = -10 found for account {account_id}. Keeping existing categories...")
    
    # Get unique combinations of Cluster and Category from the DataFrame
    unique_categories = df[['Cluster', 'Category']].drop_duplicates()
    
    # Create category records
    category_records = []
    for _, row in unique_categories.iterrows():
        category_records.append({
            'account_id': account_id,
            'category_id': int(row['Cluster']) if pd.notna(row['Cluster']) else -1,
            'category_name': row['Category']
        })
    
    # Insert into MongoDB
    if category_records:
        await collection_transaction_category.insert_many(category_records)
        print(f"Successfully inserted {len(category_records)} categories for account_id {account_id}")
        
        # Print the categories for verification
        print("\n=== Stored Categories ===")
        for record in category_records:
            print(f"Category ID: {record['category_id']}, Category Name: {record['category_name']}")
    else:
        print("No categories to insert")

    if df['Payments'].isna().any():
        print("Found NaN values in payments column. adding category ID -10...")
        # Add a special category with ID -10 for NaN payments
        special_category = {
            'account_id': account_id,
            'category_id': -10,  # Special category ID for NaN payments
            'category_name': 'flag category'
        }
        await collection_transaction_category.insert_one(special_category)



async def main():

    # Check if any values in 'Receipts' column are NaN
    if df['Payments'].isna().any():
        print("Found NaN values in payments column. Incrementing category IDs...")
        
        # Increment Cluster values by max category number availabl in collection_transaction_category for that account id, except for -1 (uncategorized)
        max_category = await collection_transaction_category.find_one(
            {"account_id": account_id},
            sort=[("category_id", -1)],
            projection={"category_id": 1}
        )
        max_category_id = max_category['category_id'] 

        df.loc[df['Cluster'] != -1, 'Cluster'] = df.loc[df['Cluster'] != -1, 'Cluster'] + max_category_id +1
        
        print("Category IDs incremented successfully.")
    else:
        print("No NaN values found in Receipts column.")

    # Optional: Print unique cluster values to verify
    print("Unique Cluster values after processing:", sorted(df['Cluster'].unique()))
    
    # Apply any stored changes first
    df_updated = await apply_stored_changes_by_account(df, account_id)
    
    # Store categories in MongoDB
    await store_categories_in_mongodb(df_updated, account_id)
    
    # Store transactions in MongoDB
    await update_mongodb_with_transactions(df_updated, account_id)

asyncio.run(main())
