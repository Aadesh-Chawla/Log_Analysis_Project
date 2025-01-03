
import pandas as pd
# df = pd.read_csv("D:\\Final Year\\Major Project\\dataset\\merged_versions\\anonymized_merged_logs_2.csv")
df = pd.read_csv("balanced_logs_by_level.csv")


print(df['level'].value_counts())