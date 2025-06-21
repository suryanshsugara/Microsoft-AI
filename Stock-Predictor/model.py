import yfinance as yf
import numpy as np
from xgboost import XGBRegressor
import pandas as pd
from sklearn.preprocessing import StandardScaler

model = XGBRegressor()
scaler = StandardScaler()

# Dummy train once (you can replace this with Azure ML trained model)
def predict_price(ticker):
    df = yf.download(ticker, period="6mo", interval="1d")
    df.dropna(inplace=True)
    df['Return'] = df['Close'].pct_change()
    df['Volatility'] = df['Return'].rolling(5).std()
    df.dropna(inplace=True)

    X = df[['Close', 'Volatility']].values[-10:]
    X_scaled = scaler.fit_transform(X)
    y = df['Close'].values[-10:]
    model.fit(X_scaled, y)

    next_day_features = scaler.transform([[X[-1][0], X[-1][1]]])
    predicted_price = model.predict(next_day_features)[0]

    return {
        "ticker": ticker,
        "predicted_close_price": round(float(predicted_price), 2),
        "last_close": round(float(X[-1][0]), 2)
    }
