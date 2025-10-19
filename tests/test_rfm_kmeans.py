import pandas as pd
from scripts.rfm_kmeans import compute_rfm_clusters
import pytest


def test_compute_rfm_clusters_happy_path():
    df = pd.DataFrame({
        'frequency':[1,5,2,10],
        'monetary':[100,500,200,1000],
        'recency_days':[30,5,60,2],
        'rfm_segment':['A','B','A','C']
    })
    out = compute_rfm_clusters(df, n_clusters=2)
    assert 'cluster' in out.columns
    assert out['cluster'].nunique() <= 2


def test_compute_rfm_clusters_missing_columns():
    df = pd.DataFrame({
        'frequency':[1,2],
        # missing monetary and recency_days
    })
    with pytest.raises(ValueError):
        compute_rfm_clusters(df)
