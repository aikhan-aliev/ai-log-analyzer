import os
from src.parser import parse_logs
from src.features import extract_features

def test_extract_features():
    file_path = os.path.join(os.path.dirname(__file__), "..", "logs", "sample_log.csv")
    df = parse_logs(file_path)
    df_features = extract_features(df)

    # Features should include engineered columns
    assert "hour" in df_features.columns
    assert "weekday" in df_features.columns
    assert "status_fail" in df_features.columns
    assert "stage_build" in df_features.columns
