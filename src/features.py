import pandas as pd

def extract_features(df):
    df = df.copy()
    
    df = pd.get_dummies(df, columns=['stage', 'status'])
    
    df['hour'] = df['timestamp'].dt.hour
    df['weekday'] = df['timestamp'].dt.weekday
    
    return df

if __name__ == "__main__":
    from parser import parse_logs
    import os

    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "sample_log.csv")
    df = parse_logs(file_path)
    df_features = extract_features(df)
    print("Feature DataFrame:")
    print(df_features.head())
