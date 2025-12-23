import numpy as np
import pandas as pd

def add_kpi_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds row-level KPI columns using your KPI definitions.
    Works even if dataset is aggregated.
    """
    df = df.copy()

    # On-time performance and delay rate (require arr_flights and arr_del15)
    if "arr_flights" in df.columns and "arr_del15" in df.columns:
        df["otp"] = (df["arr_flights"] - df["arr_del15"]) / df["arr_flights"]
        df["delay_rate_15"] = df["arr_del15"] / df["arr_flights"]

    # Average arrival delay minutes (arr_delay / arr_flights)
    if "arr_delay" in df.columns and "arr_flights" in df.columns:
        df["avg_arrival_delay_min"] = df["arr_delay"] / df["arr_flights"]

    # Cancellation rate
    if "arr_cancelled" in df.columns and "arr_flights" in df.columns:
        df["cancellation_rate"] = df["arr_cancelled"] / df["arr_flights"]

    # Total delay minutes for cause share (if cause columns exist)
    cause_cols = ["carrier_delay", "weather_delay", "nas_delay", "security_delay", "late_aircraft_delay"]
    existing = [c for c in cause_cols if c in df.columns]
    if existing:
        df["total_cause_delay_min"] = df[existing].sum(axis=1)

        for c in existing:
            share_col = f"{c}_share"
            df[share_col] = np.where(
                df["total_cause_delay_min"] > 0,
                df[c] / df["total_cause_delay_min"],
                np.nan
            )

    return df

