# main.py
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from model import predict_price

app = FastAPI(title="AI Stock Predictor")

@app.get("/predict")
async def predict(ticker: str = Query(..., description="Stock symbol (e.g., AAPL)")):
    prediction = predict_price(ticker)
    return JSONResponse(prediction)
