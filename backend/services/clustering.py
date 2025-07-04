import pandas as pd
import re
from sentence_transformers import SentenceTransformer
import hdbscan
import numpy as np
from sklearn.preprocessing import StandardScaler,normalize
from collections import Counter
import umap
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import DBSCAN
from sklearn.metrics.pairwise import cosine_similarity

#this need to be integrated with data income pipeline
df = pd.read_excel('C:\level2Sem1\AI_software_project\testing\nadilFinalizedDatasetExpenses.xlsx') # type: ignore

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

dbscan_model = DBSCAN(eps=0.4, min_samples=3, metric="precomputed")  
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

print(df.to_string())
df.to_excel('nadilDataSetWithmin5expensesv3.xlsx',index=False) 