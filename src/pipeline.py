import pandas as pd

from .io import load_raw_data, basic_clean
from .features import add_kpi_columns
from .config import PROCESSED_DATA_PATH

def run_pipeline(save: bool = True) -> pd.DataFrame:
    """
    End-to-end pipeline:
    1) load raw data
    2) basic clean
    3) add KPI feature columns
    4) optionally save to data/processed/
    """
    df = load_raw_data()
    df = basic_clean(df)
    df = add_kpi_columns(df)

    if save:
        # Save as parquet (preferred). If parquet fails, we can switch to CSV later.
        df.to_parquet(PROCESSED_DATA_PATH, index=False)

    return df
