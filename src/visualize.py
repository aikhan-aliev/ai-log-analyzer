import matplotlib.pyplot as plt
import seaborn as sns

def plot_log_levels(df):
    """Plot the distribution of log levels."""
    plt.figure(figsize=(6, 4))
    sns.countplot(x="log_level", data=df, order=df["log_level"].value_counts().index)
    plt.title("Log Level Distribution")
    plt.xlabel("Log Level")
    plt.ylabel("Count")
    plt.show()


def plot_anomalies_timeline(df_features):
    """Plot anomalies over time."""
    plt.figure(figsize=(10, 5))
    sns.scatterplot(
        x="timestamp", y="duration", 
        hue="anomaly_label", style="anomaly_label",
        data=df_features, palette={"Normal": "green", "Anomaly": "red"}
    )
    plt.title("Anomalies Over Time")
    plt.xlabel("Timestamp")
    plt.ylabel("Duration")
    plt.legend(title="Log Status")
    plt.show()


def plot_feature_boxplots(df_features):
    """Plot boxplots to compare anomaly vs normal for numeric features."""
    numeric_cols = df_features.select_dtypes(include="number").columns
    for col in numeric_cols:
        if col not in ["anomaly"]:  # skip the anomaly flag itself
            plt.figure(figsize=(6, 4))
            sns.boxplot(x="anomaly_label", y=col, data=df_features, palette={"Normal": "green", "Anomaly": "red"})
            plt.title(f"Feature Distribution by Anomaly: {col}")
            plt.show()
