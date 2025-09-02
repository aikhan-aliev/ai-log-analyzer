import os
from src.parser import parse_logs
from src.features import extract_features
from src.model import detect_anomalies

def test_detect_anomalies():
    file_path = os.path.join(os.path.dirname(__file__), "..", "logs", "sample_log.csv")
    df = parse_logs(file_path)
    df_features = extract_features(df)
    df_features, anomalies = detect_anomalies(df_features)

    # Check anomaly column exists
    assert "anomaly" in df_features.columns
    assert "anomaly_label" in df_features.columns

    # anomalies should be a subset
    assert set(anomalies["job_id"]).issubset(set(df_features["job_id"]))
