import os
import pandas as pd
from src.parser import parse_logs

def test_parse_logs():
    file_path = os.path.join(os.path.dirname(__file__), "..", "logs", "sample_log.csv")
    df = parse_logs(file_path)

    assert not df.empty

    expected_cols = {"timestamp", "job_id", "stage", "status", "duration", "error_message"}
    assert expected_cols.issubset(df.columns)

    assert pd.api.types.is_datetime64_any_dtype(df["timestamp"])
    assert pd.api.types.is_integer_dtype(df["job_id"])
