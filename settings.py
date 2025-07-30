import os

# Base directory of the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Data directories
DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, "processed")

# Configs
CONFIG_DIR = os.path.join(BASE_DIR, "configs")

# Model saving directory
MODEL_DIR = os.path.join(BASE_DIR, "models/saved")

# Create folders if missing
for path in [DATA_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR, MODEL_DIR]:
    os.makedirs(path, exist_ok=True)