import matplotlib.pyplot as plt
import seaborn as sns
import os

REPORTS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "reports")
os.makedirs(REPORTS_DIR, exist_ok=True)

def plot_status_distribution(df):
    plt.figure(figsize=(6, 4))
    sns.countplot(x="status", data=df, order=df["status"].value_counts().index)
    plt.title("Job Status Distribution")
    plt.xlabel("Status")
    plt.ylabel("Count")
    file_path = os.path.join(REPORTS_DIR, "status_distribution.png")
    plt.savefig(file_path)
    plt.close()
    print(f"Saved: {file_path}")


def plot_stage_distribution(df):
    plt.figure(figsize=(6, 4))
    sns.countplot(x="stage", data=df, order=df["stage"].value_counts().index)
    plt.title("Stage Distribution")
    plt.xlabel("Stage")
    plt.ylabel("Count")
    file_path = os.path.join(REPORTS_DIR, "stage_distribution.png")
    plt.savefig(file_path)
    plt.close()
    print(f"Saved: {file_path}")


def plot_anomalies_timeline(df_features):
    plt.figure(figsize=(10, 5))
    sns.scatterplot(
        x="timestamp", y="duration",
        hue="anomaly_label", style="anomaly_label",
        data=df_features, palette={"Normal": "green", "Anomaly": "red"}
    )
    plt.title("Anomalies Over Time")
    plt.xlabel("Timestamp")
    plt.ylabel("Duration")
    file_path = os.path.join(REPORTS_DIR, "anomalies_timeline.png")
    plt.savefig(file_path)
    plt.close()
    print(f"Saved: {file_path}")


def plot_feature_boxplots(df_features):
    """Plot boxplots to compare anomaly vs normal for numeric features."""
    numeric_cols = df_features.select_dtypes(include="number").columns
    for col in numeric_cols:
        if col not in ["anomaly"]:  # skip the anomaly flag itself
            plt.figure(figsize=(6, 4))
            sns.boxplot(
                y=col,
                x="anomaly_label",   # this becomes the hue for color mapping
                data=df_features,
                hue="anomaly_label", # explicitly assign hue
                palette={"Normal": "green", "Anomaly": "red"},
                dodge=False
            )
            plt.title(f"Feature Distribution by Anomaly: {col}")
            plt.xlabel("Anomaly Label")
            plt.ylabel(col)
            plt.legend([], [], frameon=False)  # hide extra legend
            plt.savefig(f"/app/reports/boxplot_{col}.png")
            plt.close()