"""
Script extracted from df_RFM_clustering_kmeans.ipynb
- Provides a function `compute_rfm_clusters(df, n_clusters=5, use_dataiku=False)`
- If `use_dataiku=True`, the script will try to import Dataiku Dataset APIs.
- Otherwise it works with plain pandas DataFrames.

Usage:
from scripts.rfm_kmeans import compute_rfm_clusters
df_with_clusters = compute_rfm_clusters(df)
"""

from typing import Optional
import pandas as pd
import numpy as np

try:
    import dataiku
    from dataiku import pandasutils as pdu
    DATAIKU_AVAILABLE = True
except Exception:
    DATAIKU_AVAILABLE = False

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


def compute_rfm_clusters(df: pd.DataFrame, n_clusters: int = 5) -> pd.DataFrame:
    """Compute RFM clusters and return a dataframe with a new `cluster` column.

    Inputs:
    - df: pandas DataFrame that must contain columns ['frequency','monetary','recency_days']
      and optionally 'rfm_segment' for one-hot encoding.
    - n_clusters: number of clusters for KMeans.

    Output:
    - DataFrame with additional column 'cluster'.

    Error modes:
    - Raises ValueError if required columns are missing.
    """

    required = {"frequency", "monetary", "recency_days"}
    if not required.issubset(df.columns):
        missing = required - set(df.columns)
        raise ValueError(f"DataFrame missing required columns: {missing}")

    df = df.copy()

    # One-hot encoding for rfm_segment if present
    if "rfm_segment" in df.columns:
        df = pd.get_dummies(df, columns=["rfm_segment"], prefix="segment")

    # Select features for clustering
    X_cols = ["frequency", "monetary", "recency_days"] + [col for col in df.columns if col.startswith("segment_")]
    X = df[X_cols].fillna(0)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df["cluster"] = kmeans.fit_predict(X_scaled)

    return df


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Compute RFM clusters from a CSV file and write output CSV")
    parser.add_argument("--input", help="Input CSV path", required=True)
    parser.add_argument("--output", help="Output CSV path", required=True)
    parser.add_argument("--n-clusters", type=int, default=5)
    args = parser.parse_args()

    df_input = pd.read_csv(args.input)
    df_out = compute_rfm_clusters(df_input, n_clusters=args.n_clusters)
    df_out.to_csv(args.output, index=False)
