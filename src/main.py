from parser import parse_logs
from features import extract_features
import os

def main():
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "sample_log.csv")
    
    df = parse_logs(file_path)
    print("Parsed logs:")
    print(df.head())
    
    df_features = extract_features(df)
    print("\nFeatures DataFrame:")
    print(df_features.head())

if __name__ == "__main__":
    main()
