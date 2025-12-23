import pandas as pd

def summarize_overall(df: pd.DataFrame) -> pd.DataFrame:
    """Overall KPI summary (single-row table)."""
    out = {}

    # Weighted OTP and delay rate by flights
    if {"arr_flights", "arr_del15"}.issubset(df.columns):
        total_flights = df["arr_flights"].sum()
        out["arr_flights"] = total_flights
        out["otp_weighted"] = (total_flights - df["arr_del15"].sum()) / total_flights
        out["delay_rate_15_weighted"] = df["arr_del15"].sum() / total_flights

    if {"arr_flights", "arr_delay"}.issubset(df.columns):
        out["avg_arrival_delay_min_weighted"] = df["arr_delay"].sum() / df["arr_flights"].sum()

    if {"arr_flights", "arr_cancelled"}.issubset(df.columns):
        out["cancellation_rate_weighted"] = df["arr_cancelled"].sum() / df["arr_flights"].sum()

    return pd.DataFrame([out])

def summarize_by(df: pd.DataFrame, group_cols: list[str], top_n: int | None = None) -> pd.DataFrame:
    """
    Grouped KPI summary. Uses weighted calculations where appropriate.
    """
    g = df.groupby(group_cols, dropna=False)

    agg = g.agg(
        arr_flights=("arr_flights", "sum"),
        arr_del15=("arr_del15", "sum"),
        arr_delay=("arr_delay", "sum"),
        arr_cancelled=("arr_cancelled", "sum"),
    ).reset_index()

    # Derived weighted metrics
    agg["otp"] = (agg["arr_flights"] - agg["arr_del15"]) / agg["arr_flights"]
    agg["delay_rate_15"] = agg["arr_del15"] / agg["arr_flights"]
    agg["avg_arrival_delay_min"] = agg["arr_delay"] / agg["arr_flights"]
    agg["cancellation_rate"] = agg["arr_cancelled"] / agg["arr_flights"]

    if top_n:
        agg = agg.sort_values("arr_flights", ascending=False).head(top_n)

    return agg

