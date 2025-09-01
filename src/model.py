from sklearn.ensemble import IsolationForest
import pandas as pd

def detect_anomalies(df_features, contamination=0.05): # Detect anomalies in logs using Isolation Forest.
    numeric_cols = df_features.select_dtypes(include=['float64', 'int64']).columns
    X = df_features[numeric_cols]

    model = IsolationForest(contamination=contamination, random_state=42)
    df_features['anomaly'] = model.fit_predict(X)

    anomalies = df_features[df_features['anomaly'] == -1]
    return df_features, anomalies


if __name__ == "__main__":
    from parser import parse_logs
    from features import extract_features
    import os

    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "sample_log.csv")
    df = parse_logs(file_path)
    df_features = extract_features(df)
    df_features, anomalies = detect_anomalies(df_features)
    print("Detected anomalies:")
    print(anomalies)
