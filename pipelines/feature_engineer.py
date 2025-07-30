import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and normalize raw time-series data."""
    # 1. Convert timestamp to datetime
    df['timestamp'] = pd.to_datetime(df['Timestamp'], unit='s')  # Unix seconds to datetime

    # 2. Sort by timestamp just to be safe
    df = df.sort_values('timestamp').reset_index(drop=True)

    # 3. Drop duplicates if any
    df = df.drop_duplicates(subset=['timestamp'])

    return df


def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add simple placeholder features (moving averages, returns)."""
    # Feature 1: Returns (percentage change)
    df['return'] = df['Close'].pct_change()

    # Feature 2: Moving averages
    df['ma_5'] = df['Close'].rolling(window=5).mean()
    df['ma_20'] = df['Close'].rolling(window=20).mean()

    # Drop rows with NaNs created by rolling windows
    df.dropna(inplace=True)

    return df