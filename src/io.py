import pandas as pd
from .config import RAW_DATA_PATH

def load_raw_data(path: str | None = None) -> pd.DataFrame:
    """Load raw airline delay dataset."""
    p = path if path else str(RAW_DATA_PATH)
    df = pd.read_csv(p)
    return df

def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    """
    Minimal cleaning:
    - standardize column names
    - coerce numeric columns where possible
    - drop rows with missing core denominators (arr_flights)
    """
    df = df.copy()

    # Standardize column names: lower, strip, spaces->underscore
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    # Coerce key numeric columns (if present)
    numeric_candidates = [
        "arr_flights", "arr_del15", "arr_delay", "arr_cancelled",
        "carrier_delay", "weather_delay", "nas_delay", "security_delay",
        "late_aircraft_delay"
    ]
    for col in numeric_candidates:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Drop rows without denominator
    if "arr_flights" in df.columns:
        df = df[df["arr_flights"].notna()]
        df = df[df["arr_flights"] > 0]

    return df

