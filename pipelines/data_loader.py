import pandas as pd
from settings import RAW_DATA_DIR

def load_data():
    """Loads CSV data and parses timestamps."""
    df = pd.read_csv(f"{RAW_DATA_DIR}/btcusd_1-min_data.csv")
    df.rename(columns={"Timestamp": "timestamp"}, inplace=True)
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    df.sort_values('timestamp', inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df