import pandas as pd
import os

def parse_logs(file_path):
    df = pd.read_csv(file_path, parse_dates=['timestamp'])
    df['duration'] = pd.to_numeric(df['duration'], errors='coerce')
    df['status'] = df['status'].astype('category')
    return df

if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "sample_log.csv")
    df = parse_logs(file_path)
    print("Parsed logs:")
    print(df.head())
