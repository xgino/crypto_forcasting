from pipelines.data_loader import load_data
from pipelines.feature_engineer import clean_data, add_features

if __name__ == "__main__":
    # 1. Load data
    df = load_data()
    print("Loaded DataFrame:")
    print(df.head())

    # 2. Clean timeline
    df = clean_data(df)
    print("Cleaned DataFrame:")
    print(df.head())

    # 3. Feature Engineering
    df = add_features(df)
    print("After feature engineering:")
    print(df.head())

    # 4. 
    # 4. 
    # 4. 
    # 4. 
    # 4. 