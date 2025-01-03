import os

# Replace 'path_to_your_dataset_folder' with the actual path to your dataset folder
folder_path = "D:\\Final Year\\Major Project\\dataset\\unzipped"

for root, dirs, files in os.walk(folder_path):
    level = root.replace(folder_path, '').count(os.sep)
    indent = ' ' * 4 * level
    print(f"{indent}{os.path.basename(root)}/")
    subindent = ' ' * 4 * (level + 1)
    for f in files:
        print(f"{subindent}{f}")
