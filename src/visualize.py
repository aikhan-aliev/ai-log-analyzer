import matplotlib.pyplot as plt
import seaborn as sns

def plot_status_distribution(df):
    """Plot the distribution of job statuses (success/fail)."""
    plt.figure(figsize=(6, 4))
    sns.countplot(x="status", data=df, order=df["status"].value_counts().index)
    plt.title("Job Status Distribution")
    plt.xlabel("Status")
    plt.ylabel("Count")
    plt.show()


def plot_stage_distribution(df):
    """Plot how many logs per pipeline stage (build/test/deploy)."""
    plt.figure(figsize=(6, 4))
    sns.countplot(x="stage", data=df, order=df["stage"].value_counts().index)
    plt.title("Stage Distribution")
    plt.xlabel("Stage")
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
            sns.boxplot(x="anomaly_label", y=col, data=df_features,
                        palette={"Normal": "green", "Anomaly": "red"})
            plt.title(f"Feature Distribution by Anomaly: {col}")
            plt.show()
