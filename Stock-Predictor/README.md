# AI Stock Predictor 📈🤖

A FastAPI-based stock price predictor using real-time data from Yahoo Finance and machine learning models like XGBoost.

## 🔧 Setup
```bash
git clone https://github.com/suryanshsugara/Microsoft-AI/tree/main/Stock-Predictor
cd ai-stock-predictor
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## 💡 Features
- Real-time stock price prediction using yfinance
- Rolling volatility + return as features
- Scikit-learn + XGBoost training
- API returns predicted next-day closing price

## ☁️ Microsoft Tech Used
- Azure ML (for future deployment/tracking)
- Azure Functions (for scheduling predictions – optional)

## 📬 Contact
Built with ❤️ by [Suryansh Sugara](https://github.com/suryanshsugara).
