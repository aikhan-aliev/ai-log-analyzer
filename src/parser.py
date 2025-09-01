import pandas as pd

def parse_logs(file_path):
    df = pd.read_csv(file_path, parse_dates=['timestamp'])
    df['duration'] = pd.to_numeric(df['duration'], errors='coerce')
    df['status'] = df['status'].astype('category')
    return df

if __name__ == "__main__":
    df = parse_logs("logs/sample_log.csv")
    print(df.head())