import re
import pandas as pd

def anonymize_logs(log_message):
    # Anonymize job IDs
    log_message = re.sub(r'job_\d+_\d+', 'job_id', log_message)
    
    # Anonymize application IDs
    log_message = re.sub(r'application_\d+_\d+', 'application_id', log_message)
    
    # Anonymize task attempts (embedded numbers in words)
    log_message = re.sub(r'attempt_\d+_\d+_m_\d+_\d+', 'task_attempt', log_message)
    
    # Anonymize file paths
    log_message = re.sub(r'\/[^\s]+', 'file_path', log_message)
    
    # Anonymize port numbers
    log_message = re.sub(r'\b\d{4,5}\b', 'port_number', log_message)
    
    # Anonymize IP addresses
    log_message = re.sub(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', 'ip_address', log_message)
    
    # Replace all other numbers (even those embedded within words or special characters)
    log_message = re.sub(r'\d+', '-', log_message)
    
    return log_message

# Load your dataset
df = pd.read_csv("D:\\Final Year\\Major Project\\dataset\\merged_versions\\merged_dataset_labels_hot_without_time.csv")

# Apply the anonymization function to the message column
df['anonymized_message'] = df['message'].apply(anonymize_logs)

# Save the updated dataset to a new CSV
df.to_csv('anonymized_merged_logs_2.csv', index=False)

print("Anonymization with embedded numbers handled and saved to 'anonymized_merged_logs.csv'")
