import spacy
import pandas as pd

# Load the pre-trained spaCy model
nlp = spacy.load("en_core_web_sm")

# Function to replace recognized entities with placeholders
def anonymize_with_ner(log_message):
    doc = nlp(log_message)
    # Iterate through the entities recognized by spaCy's NER
    for ent in doc.ents:
        # Replace the entity with its type as placeholder (e.g., [PERSON], [DATE], [GPE])
        log_message = log_message.replace(ent.text, f"[{ent.label_}]")
    return log_message

# Load your dataset
df = pd.read_csv("D:\\Final Year\\Major Project\\dataset\\merged_versions\\merged_dataset_labels_hot_without_time.csv")

# Apply the NER anonymization function to the message column
df['anonymized_message'] = df['message'].apply(anonymize_with_ner)

# Save the updated dataset to a new CSV
df.to_csv('anonymized_logs_with_ner.csv', index=False)

print("NER-based anonymization applied and saved to 'anonymized_logs_with_ner.csv'")
