import pandas as pd
import os
import re

def parse_log_line(line):
    # Define a regex pattern to extract relevant log details
    log_pattern = re.compile(
        r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) '
        r'(?P<log_level>\w+) \[(?P<thread>\w+)\] (?P<class>[\w\.]+): (?P<message>.+)'
    )
    
    match = log_pattern.match(line)
    if match:
        return match.groupdict()
    return None

def convert_logs_to_csv(log_root_directory, output_csv):
    all_logs = []

    # Walk through the directory to find all log files
    for root, dirs, files in os.walk(log_root_directory):
        for filename in files:
            if filename.endswith('.log'):
                log_file_path = os.path.join(root, filename)
                print(f"Processing file: {log_file_path}")  # Optional: to see progress
                with open(log_file_path, 'r') as file:
                    for line in file:
                        log_entry = parse_log_line(line)
                        if log_entry:
                            all_logs.append(log_entry)

    # Convert to DataFrame and save as CSV
    if all_logs:
        df = pd.DataFrame(all_logs)
        df.to_csv(output_csv, index=False)
        print(f"Merged logs saved to {output_csv}")
    else:
        print("No log entries found.")

# Example usage
log_root_directory = "D:\\Final Year\\Major Project\\dataset\\unzipped\Hadoop_c"  # Update with your main directory containing all application folders
output_csv = 'merged_logs.csv'  # Specify the output CSV file name
convert_logs_to_csv(log_root_directory, output_csv)
