import numpy as np, pandas as pd, joblib, xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
from pathlib import Path

rng = np.random.default_rng(42)
N = 8000
df = pd.DataFrame({
    "distance_est": rng.normal(40, 15, N).clip(1, 150),
    "sku_volume": rng.lognormal( -3, 0.8, N),
    "wave_size": rng.integers(10, 200, N),
    "weekday": rng.integers(0, 7, N),
    "hour": rng.integers(6, 22, N)
})
# target sintético
noise = rng.normal(0, 3, N)
df["eta_minutes"] = 0.35*df["distance_est"] + 14*df["sku_volume"] + 0.04*df["wave_size"] + 0.2*df["weekday"] + 0.1*df["hour"] + noise

X = df[["distance_est","sku_volume","wave_size","weekday","hour"]].values
y = df["eta_minutes"].values

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)

model = xgb.XGBRegressor(
    n_estimators=200, max_depth=5, learning_rate=0.07, subsample=0.9, colsample_bytree=0.9, n_jobs=2
)
model.fit(X_tr, y_tr)
pred = model.predict(X_te)
mae = mean_absolute_error(y_te, pred)
rmse = mean_squared_error(y_te, pred, squared=False)
print(f"MAE={mae:.3f} | RMSE={rmse:.3f}")

Path("artifacts").mkdir(exist_ok=True)
joblib.dump(model, "artifacts/model.pkl")
with open("artifacts/metrics.txt","w") as f:
    f.write(f"MAE={mae:.3f}\nRMSE={rmse:.3f}\n")
print("Modelo guardado en artifacts/model.pkl")
