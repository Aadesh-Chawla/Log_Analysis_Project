import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# Load your cleaned dataset
df_t = pd.read_csv('final_dataset_for_model.csv')

# Step 1: Prepare features and labels
X = df_t[['anonymized_message', 'level', 'thread']]  # Select relevant features
y = df_t['labels']  # Select target variable

# Step 2: Encode categorical variables
X['anonymized_message'] = X['anonymized_message'].astype('category').cat.codes
X['level'] = X['level'].astype('category').cat.codes
X['thread'] = X['thread'].astype('category').cat.codes

# Step 3: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train the model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Step 5: Evaluate the model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))