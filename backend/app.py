from flask import Flask, jsonify #pip install Flask
import requests #pip install requests
from flask_cors import CORS #pip install Flask-Cors
from SMA import SMA
from RSI import calculate_rsi, RSI_monthly, RSI_daily, RSI_weekly
from EMA import daily_ema, weekly_ema, monthly_ema
import json
import math

app = Flask(__name__)
CORS(app)

API_KEY = "6ZP516EDZC9M2JBK"
with open('data.json', 'r') as file:
    fetchedData = json.load(file)
    
def convert_to_json(data_frame):
    json_data = {}
    
    for index, row in data_frame.iterrows():
        date = str(index.date())
        ema_close = row['EMA-close']

        if not np.isnan(ema_close):
            json_data[date] = ema_close
    
    return json_data

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
    fetchedData = jsonify(combined_data)
    return fetchedData

@app.route('/sma', methods=['GET'])
def get_sma():
    # Collect data as before
    combined_data = fetchedData

    df_daily = SMA(combined_data, 'daily', 3)
    daily_data = df_daily['SMA']

    df_weekly = SMA(combined_data, 'weekly', 3)
    weekly_data = df_weekly['SMA']

    df_monthly = SMA(combined_data, 'monthly', 3)
    monthly_data = df_monthly['SMA']

    daily_data_dict = daily_data.to_dict()
    weekly_data_dict = weekly_data.to_dict()
    monthly_data_dict = monthly_data.to_dict()

    # Convert dictionary to JSON format
    combined_data = {
        "daily": daily_data_dict,
        "weekly": weekly_data_dict,
        "monthly": monthly_data_dict
    }

    combined_data_json = json.dumps(combined_data, default=str)
    return combined_data_json
@app.route('/rsi', methods=['GET'])
def get_rsi():
    # Collect data as before
    combined_data = fetchedData
    
    window_length = 4
    start_date = '0'
    end_date = '0'

    df_daily = RSI_daily(combined_data, window_length, start_date, end_date)
    daily_rsi_data = df_daily['rsi']

    df_weekly = RSI_weekly(combined_data, window_length, start_date, end_date)
    weekly_rsi_data = df_weekly['rsi']

    df_monthly = RSI_monthly(combined_data, window_length, start_date, end_date)
    monthly_rsi_data = df_monthly['rsi']

    # Convert Timestamps to strings for each RSI dictionary
    daily_rsi_dict = daily_rsi_data.reset_index().astype(str).set_index('index').to_dict()['rsi']
    weekly_rsi_dict = weekly_rsi_data.reset_index().astype(str).set_index('index').to_dict()['rsi']
    monthly_rsi_dict = monthly_rsi_data.reset_index().astype(str).set_index('index').to_dict()['rsi']
    
    daily_rsi_dict = filter_nan_values(daily_rsi_dict)
    weekly_rsi_dict = filter_nan_values(weekly_rsi_dict)
    monthly_rsi_dict = filter_nan_values(monthly_rsi_dict)

    
    combined_rsi_data = {
    "daily": daily_rsi_dict,
    "weekly": weekly_rsi_dict,
    "monthly": monthly_rsi_dict
    }

    # 4. Serialize the final combined dictionary to a JSON format
    combined_rsi_json = json.dumps(combined_rsi_data, default=str, indent=4)
    return combined_rsi_json

@app.route('/ema', methods=['GET'])
def get_ema():
    combined_data = fetchedData
    daily_df = daily_ema(combined_data, 20)
    weekly_df = weekly_ema(combined_data, 20)
    monthly_df = monthly_ema(combined_data, 20)
    daily_json_data = convert_to_json(daily_df)
    weekly_json_data = convert_to_json(weekly_df)
    monthly_json_data = convert_to_json(monthly_df)
    
    combined_ema_data = {
    "Daily": daily_json_data,
    "Weekly": weekly_json_data,
    "Monthly": monthly_json_data
    }   
    combined_ema_json = json.dumps(combined_ema_data, default=str, indent=4)
    return combined_ema_json

        
    
if __name__ == '__main__':
    app.run(port=5000)
