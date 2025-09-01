from sklearn.ensemble import IsolationForest
import pandas as pd

def detect_anomalies(df_features, contamination=0.05): #Detect anomalies in logs using Isolation Forest
    # Select only numeric columns for anomaly detection
    numeric_cols = df_features.select_dtypes(include='number').columns
    X = df_features[numeric_cols]

    # Fit Isolation Forest model
    model = IsolationForest(contamination=contamination, random_state=42)
    df_features['anomaly'] = model.fit_predict(X)

    # Add human-readable labels
    df_features['anomaly_label'] = df_features['anomaly'].map({1: "Normal", -1: "Anomaly"})

    # Extract only anomalies
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
