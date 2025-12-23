from src.pipeline import run_pipeline

if __name__ == "__main__":
    df = run_pipeline(save=True)
    print("✅ Pipeline complete.")
    print("Rows:", len(df))
    print("Columns:", len(df.columns))
    print(df.head())
