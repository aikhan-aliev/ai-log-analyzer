from parser import parse_logs
from features import extract_features
from model import detect_anomalies
import os


def main():
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "sample_log.csv")
    
    # Parse logs
    df = parse_logs(file_path)
    print("✅ Parsed logs:")
    print(df.head())
    
    # Feature engineering
    df_features = extract_features(df)
    print("\n📊 Feature DataFrame:")
    print(df_features.head())
    
    # Detect anomalies
    df_features, anomalies = detect_anomalies(df_features)
    print(f"\n🚨 Detected {len(anomalies)} anomalies:")
    print(anomalies)

    # Visualization
    from visualize import (
        plot_status_distribution,
        plot_stage_distribution,
        plot_anomalies_timeline,
        plot_feature_boxplots
    )

    print("\n📊 Generating visualizations...")
    plot_status_distribution(df)
    plot_stage_distribution(df)
    plot_anomalies_timeline(df_features)
    plot_feature_boxplots(df_features)


if __name__ == "__main__":
    main()
