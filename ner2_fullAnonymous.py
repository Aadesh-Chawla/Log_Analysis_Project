import re
import pandas as pd

# Function to replace all numbers with "-"
def replace_numbers_with_placeholder(log_message):
    return re.sub(r'(?<!\[)\b\d+\b(?!\])', '-', log_message)

# Load your dataset
df = pd.read_csv("D:\\Final Year\\Major Project\\dataset\\merged_versions\\anonymized_logs_with_ner.csv")

# Apply the function to replace numbers with "-"
df['anonymized_message'] = df['message'].apply(replace_numbers_with_placeholder)

# Save the updated dataset to a new CSV
df.to_csv('anonymized_logs_ner_with_numbers_replaced.csv', index=False)

print("Numbers replaced with '-' and saved to 'anonymized_logs_ner_with_numbers_replaced.csv'")
