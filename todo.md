## Project To‑Do Roadmap

### 1. Code Baseline  
- Use Kaggle API to pull BTC forecasting notebooks (e.g., Random Forest, LSTM) :contentReference[oaicite:0]{index=0}.  
- Audit GitHub repos for data pipelines and feature‑engineering examples.

### 2. Data Gathering  
- **Baseline:** CoinGecko free API for OHLCV & market metrics :contentReference[oaicite:1]{index=1}.  
- **Expandables:** CoinMarketCap, CryptoDataDownload CSVs :contentReference[oaicite:2]{index=2}, CoinAPI, Glassnode on‑chain :contentReference[oaicite:3]{index=3}, Santiment GraphQL :contentReference[oaicite:4]{index=4}, Twitter/Reddit sentiment, NewsAPI/CryptoPanic, RSS, Google Trends, NFT marketplace APIs.

### 3. Model Development  
- **Baseline:** Random Forest regressor + ARIMA trend blend :contentReference[oaicite:5]{index=5}.  
- **Future:** XGBoost, LSTM/GRU or TCN, ARCH/GARCH :contentReference[oaicite:6]{index=6}, Transformers, ensembles, DQN/PPO RL, GANs/VAE augmentation.

### 4. Validation  
- Implement walk‑forward (expanding‑window) CV :contentReference[oaicite:7]{index=7}.  
- Log MAPE, RMSE, mean directional accuracy (MDA) :contentReference[oaicite:8]{index=8}.

### 5. Hyperparameter Tuning  
- Start with manual sweeps.  
- Adopt Optuna for Bayesian HP optimization (TPE sampler) :contentReference[oaicite:9]{index=9}.

### 6. Monitoring & Explainability  
- Integrate Evidently AI for drift/performance reports :contentReference[oaicite:10]{index=10}.  
- (Optional) Log SHAP summaries per prediction.

### 7. Iteration Loop  
- Version components (v1, v2, …) and repeat steps 2–6 on new data or model updates.

### 8. Deployment & Model Registry  
- Containerize FastAPI with `/health` & `/predict` endpoints :contentReference[oaicite:11]{index=11}.  
- Register and stage models in MLflow Model Registry :contentReference[oaicite:12]{index=12}.  
- Automate CI/CD for retraining, testing, and rollout.
