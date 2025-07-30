from sklearn.metrics import mean_squared_error

def evaluate_model(model, X_val, y_val):
    """Return RMSE as an example metric."""
    preds = model.predict(X_val)
    rmse = mean_squared_error(y_val, preds, squared=False)
    return rmse