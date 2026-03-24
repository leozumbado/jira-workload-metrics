import pandas as pd
import os

def load_all_csv(folder_path):
    dfs = []

    for file in os.listdir(folder_path):
        if file.endswith(".csv"):
            full_path = os.path.join(folder_path, file)
            
            try:
                df = pd.read_csv(full_path)
                df["source_file"] = file
                dfs.append(df)

            except Exception as e:
                print(f"Error loading {file}: {e}")

    if dfs:
        return pd.concat(dfs, ignore_index=True)
    
    return None