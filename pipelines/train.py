import joblib

def train_model(model, X_train, y_train):
    """Train a model (placeholder for ML or DL)."""
    model.fit(X_train, y_train)
    return model

def save_model(model, path="models/saved_model.pkl"):
    joblib.dump(model, path)