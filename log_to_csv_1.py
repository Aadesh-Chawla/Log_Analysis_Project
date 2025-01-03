import pandas as pd
import os
import re
from sklearn.preprocessing import MultiLabelBinarizer

# Sample abnormal_labels dictionary (you can add all entries from the provided abnormal_labels data)
# abnormal_labels = {
#     'application_1445087491445_0001': ['Machine down'],
#     'application_1445087491445_0005': ['Normal'],
#     'application_1445175094696_0001': ['Network disconnection'],
#     'application_1445182159119_0001': ['Disk full'],
#     # Add all other applications and their respective labels here
# }


# Full abnormal_labels dictionary based on the abnormal_labels file you provided
abnormal_labels = {
    # WordCount
    'application_1445087491445_0001': ['Machine down'],
    'application_1445087491445_0002': ['Machine down'],
    'application_1445087491445_0003': ['Machine down'],
    'application_1445087491445_0004': ['Machine down'],
    'application_1445087491445_0005': ['Normal'],
    'application_1445087491445_0006': ['Machine down'],
    'application_1445087491445_0007': ['Normal'],
    'application_1445087491445_0008': ['Machine down'],
    'application_1445087491445_0009': ['Machine down'],
    'application_1445087491445_0010': ['Machine down'],
    'application_1445094324383_0001': ['Machine down'],
    'application_1445094324383_0002': ['Machine down'],
    'application_1445094324383_0003': ['Machine down'],
    'application_1445094324383_0004': ['Machine down'],
    'application_1445094324383_0005': ['Machine down'],
    
    'application_1445175094696_0001': ['Network disconnection'],
    'application_1445175094696_0002': ['Network disconnection'],
    'application_1445175094696_0003': ['Network disconnection'],
    'application_1445175094696_0004': ['Network disconnection'],
    'application_1445175094696_0005': ['Normal'],
    
    'application_1445182159119_0001': ['Disk full'],
    'application_1445182159119_0002': ['Disk full'],
    'application_1445182159119_0003': ['Disk full'],
    'application_1445182159119_0004': ['Disk full'],
    'application_1445182159119_0005': ['Disk full'],

    # PageRank
    'application_1445062781478_0011': ['Normal'],
    'application_1445062781478_0012': ['Machine down'],
    'application_1445062781478_0013': ['Machine down'],
    'application_1445062781478_0014': ['Machine down'],
    'application_1445062781478_0015': ['Machine down'],
    'application_1445062781478_0016': ['Normal'],
    'application_1445062781478_0017': ['Machine down'],
    'application_1445062781478_0018': ['Machine down'],
    'application_1445062781478_0019': ['Normal'],
    'application_1445062781478_0020': ['Machine down'],
    
    'application_1445076437777_0001': ['Machine down'],
    'application_1445076437777_0002': ['Normal'],
    'application_1445076437777_0003': ['Machine down'],
    'application_1445076437777_0004': ['Machine down'],
    'application_1445076437777_0005': ['Normal'],

    'application_1445144423722_0020': ['Network disconnection'],
    'application_1445144423722_0021': ['Normal'],
    'application_1445144423722_0022': ['Network disconnection'],
    'application_1445144423722_0023': ['Network disconnection'],
    'application_1445144423722_0024': ['Normal'],

    'application_1445182159119_0011': ['Disk full'],
    'application_1445182159119_0012': ['Normal'],
    'application_1445182159119_0013': ['Disk full'],
    'application_1445182159119_0014': ['Disk full'],
    'application_1445182159119_0015': ['Disk full'],
    
    'application_1445182159119_0016': ['Machine down'],
    'application_1445182159119_0017': ['Machine down'],
    'application_1445182159119_0018': ['Machine down'],
    'application_1445182159119_0019': ['Machine down'],
    'application_1445182159119_0020': ['Machine down']
}


# Function to parse a log line
def parse_log_line(line):
    log_pattern = re.compile(r'(?P<timestamp>\S+\s+\S+)\s+(?P<level>\w+)\s+\[(?P<thread>[^\]]+)\]\s+(?P<class>[^\s:]+):\s+(?P<message>.+)')
    match = log_pattern.match(line)
    if match:
        return match.groupdict()
    return None

# Function to process a single log file
def process_log_file(filepath):
    log_data = []
    with open(filepath, 'r') as f:
        for line in f:
            parsed_line = parse_log_line(line)
            if parsed_line:
                log_data.append(parsed_line)
    return log_data

# Main function to process all log files and merge them into a single dataset
def merge_log_files(logs_root_folder):
    all_logs = []
    
    # Traverse all application run folders
    for root, dirs, files in os.walk(logs_root_folder):
        for file in files:
            if file.endswith('.log'):
                application_id = root.split(os.sep)[-1]  # Get the application_id from the folder name
                log_file_path = os.path.join(root, file)
                log_data = process_log_file(log_file_path)
                
                # Add the application ID to the log data
                for entry in log_data:
                    entry['application_id'] = application_id
                    # Map the abnormal labels based on the application_id
                    entry['labels'] = abnormal_labels.get(application_id, ['Unknown'])  # Default to 'Unknown' if not found
                all_logs.extend(log_data)
    
    # Convert the log data into a DataFrame
    df = pd.DataFrame(all_logs)
    
    # Convert the timestamp column to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    
    # Multi-hot encode the labels
    mlb = MultiLabelBinarizer()
    label_encoded = mlb.fit_transform(df['labels'])
    
    # Convert encoded labels to DataFrame
    labels_df = pd.DataFrame(label_encoded, columns=mlb.classes_)
    
    # Concatenate the log data with the encoded labels
    final_df = pd.concat([df, labels_df], axis=1)
    
    # Save the final DataFrame to a CSV file
    final_df.to_csv('merged_hadoop_logs_with_labels.csv', index=False)

# Call the function
merge_log_files("D:\\Final Year\\Major Project\\dataset\\unzipped\\Hadoop")
