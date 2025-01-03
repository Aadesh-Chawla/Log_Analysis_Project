from imblearn.over_sampling import SMOTE
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Load the dataset
df = pd.read_csv("D:\\Final Year\\Major Project\\dataset\\merged_versions\\anonymized_merged_logs_2.csv")

# Features (log messages) and target (levels)
X = df['anonymized_message']  # Text data
y = df['level']               # Target column (info, error, warning)

# Convert the text data into numerical format using TF-IDF
vectorizer = TfidfVectorizer()
X_tfidf = vectorizer.fit_transform(X)

# Apply SMOTE to balance the levels
smote = SMOTE(random_state=42, sampling_strategy={'INFO': 168920, 'ERROR': 50000, 'WARN': 50000})
X_resampled, y_resampled = smote.fit_resample(X_tfidf, y)

# Convert resampled data back to DataFrame
resampled_df = pd.DataFrame(X_resampled.toarray(), columns=vectorizer.get_feature_names_out())
resampled_df['level'] = y_resampled

# Save the balanced dataset to a CSV
resampled_df.to_csv("balanced_logs_by_level.csv", index=False)

print("SMOTE applied based on 'level' and saved to 'balanced_logs_by_level.csv'")
