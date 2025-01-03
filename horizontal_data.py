import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load your log data
df_t = pd.read_csv('final_dataset_for_model.csv')

# Define parameters
window_size = 5  # Number of events per sequence

# Step 1: Create combined sequences with sliding windows
sequences = []
labels = []

for i in range(len(df_t) - window_size):
    # Combine messages in the window into a single string
    combined_sequence = " ".join(df_t['anonymized_message'].iloc[i:i + window_size].tolist())
    # Label the sequence based on the final message's label
    label = df_t['labels'].iloc[i + window_size - 1]
    
    sequences.append(combined_sequence)
    labels.append(label)

# Step 2: Vectorize combined sequences
tfidf_vectorizer = TfidfVectorizer(max_features=500)  # Adjust max_features as needed
X = tfidf_vectorizer.fit_transform(sequences)

# Convert to DataFrame
X_df = pd.DataFrame(X.toarray(), columns=tfidf_vectorizer.get_feature_names_out())
X_df['labels'] = labels

# Split data into features and labels
X = X_df.drop(columns=['labels'])
y = X_df['labels']

print("Sequences prepared for modeling. Shape of X:", X.shape)
print("Shape of y:", y.shape)

