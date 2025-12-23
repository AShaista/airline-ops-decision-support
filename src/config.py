from pathlib import Path

# Project root assumed as repository root
REPO_ROOT = Path(__file__).resolve().parents[1]

RAW_DATA_PATH = REPO_ROOT / "data" / "raw" / "airline_delay_sample.csv"
PROCESSED_DIR = REPO_ROOT / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

PROCESSED_DATA_PATH = PROCESSED_DIR / "airline_delay_clean.parquet"

