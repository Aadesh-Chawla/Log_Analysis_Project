import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import pickle

# Load the SMOTE output data
file_path = r"balanced_logs_by_level.csv"  # Update with your file path
data = pd.read_csv(file_path)

# Separate features (X) and target (y)
X = data.drop(columns=['level'])  # Replace 'level' with the target column name
y = data['level']

# Split into training and testing datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Train an SVM model
svm_model = SVC(kernel='linear', random_state=42)  # You can change the kernel to 'rbf', 'poly', etc.
svm_model.fit(X_train, y_train)

# Make predictions
y_pred = svm_model.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Save the trained model as a .pkl file
model_file = r"svm_model.pkl"  # Update with your desired file path
with open(model_file, 'wb') as file:
    pickle.dump(svm_model, file)

print(f"Model saved successfully at: {model_file}")
