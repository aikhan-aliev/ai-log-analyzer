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
    numeric_cols = df_features.select_dtypes(include="number").columns
    for col in numeric_cols:
        if col != "anomaly":
            plt.figure(figsize=(6, 4))
            sns.boxplot(
                x="anomaly_label", y=col, data=df_features,
                palette={"Normal": "green", "Anomaly": "red"}
            )
            plt.title(f"Feature Distribution by Anomaly: {col}")
            file_path = os.path.join(REPORTS_DIR, f"boxplot_{col}.png")
            plt.savefig(file_path)
            plt.close()
            print(f"Saved: {file_path}")
