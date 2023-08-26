from flask import Flask, jsonify #pip install Flask
import requests #pip install requests
from flask_cors import CORS #pip install Flask-Cors

app = Flask(__name__)
CORS(app)
API_KEY = "6ZP516EDZC9M2JBK "

@app.route('/fetchData/<symbol>', methods=['GET'])
def fetchData(symbol):
    API_URL_DAILY = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
    API_URL_WEEKLY = f"https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol={symbol}&apikey={API_KEY}"
    API_URL_MONTHLY = f"https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol={symbol}&apikey={API_KEY}"
    
    daily_data = requests.get(API_URL_DAILY).json()
    weekly_data = requests.get(API_URL_WEEKLY).json()
    monthly_data = requests.get(API_URL_MONTHLY).json()
    
    combined_data = {
        "daily": daily_data,
        "weekly": weekly_data,
        "monthly": monthly_data
    }

    return jsonify(combined_data)

if __name__ == '__main__':
    app.run(port=5000)
