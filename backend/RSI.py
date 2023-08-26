import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt
import numpy as np
import json


# Load JSON data from file
# with open('daily-sample.json', 'r') as json_file:
#     daily_sample_data = json.load(json_file)

# with open('weekly-sample.json', 'r') as json_file:
#     weekly_sample_data = json.load(json_file)
    
# with open('monthly-sample.json', 'r') as json_file:
#     monthly_sample_data = json.load(json_file)
       
def calculate_rsi(data, window_length):
    delta = data.diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=window_length).mean()
    avg_loss = loss.rolling(window=window_length).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def RSI_monthly(datajson, window_length):
    #with open(json.dumps(datajson), 'r') as json_file: OPENS FILE
    #    json_data = json.load(json_file) , turns file into json object
    json_data = datajson # datajson is a json file

    # extract monthly adjusted time series data
    time_series_data = json_data['monthly']["Monthly Adjusted Time Series"]
    df = pd.DataFrame.from_dict(time_series_data, orient='index')
    
    # Convert column data to numeric
    numeric_columns = ["1. open", "2. high", "3. low", "4. close", "5. adjusted close", "6. volume", "7. dividend amount"]
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric)
    
    df.index = pd.to_datetime(df.index) # so there's no overlap of years


    df['rsi'] = ta.rsi(df['4. close'], length=window_length)

    return df
    ''' # plotting
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['rsi'], label='RSI')
    plt.axhline(y=70, color='r', linestyle='--', label='Overbought (70)')
    plt.axhline(y=30, color='g', linestyle='--', label='Oversold (30)')
    plt.title('Relative Strength Index (RSI)')
    plt.xlabel('Date')
    plt.ylabel('RSI Value')
    plt.legend()
    plt.grid(True)
    plt.show() '''
    

def RSI_weekly(datajson, window_length):
    #with open(json.dumps(datajson), 'r') as json_file: OPENS FILE
    #    json_data = json.load(json_file) , turns file into json object
    json_data = datajson # datajson is a json file

    # extract weekly adjusted time series data
    time_series_data = json_data['weekly']["Weekly Adjusted Time Series"]
    df = pd.DataFrame.from_dict(time_series_data, orient='index')
    
    # Convert column data to numeric
    numeric_columns = ["1. open", "2. high", "3. low", "4. close", "5. adjusted close", "6. volume", "7. dividend amount"]
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric)
    
    df.index = pd.to_datetime(df.index) # so there's no overlap of years


    df['rsi'] = ta.rsi(df['4. close'], length=window_length)

    return df

    '''# plotting
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['rsi'], label='RSI')
    plt.axhline(y=70, color='r', linestyle='--', label='Overbought (70)')
    plt.axhline(y=30, color='g', linestyle='--', label='Oversold (30)')
    plt.title('Relative Strength Index (RSI)')
    plt.xlabel('Date')
    plt.ylabel('RSI Value')
    plt.legend()
    plt.grid(True)
    plt.show()'''


def RSI_daily(datajson, window_length):
    #with open(json.dumps(datajson), 'r') as json_file: OPENS FILE
    #    json_data = json.load(json_file) , turns file into json object
    json_data = datajson # datajson is a json file

    # extract weekly adjusted time series data
    time_series_data = json_data['daily']["Time Series (Daily)"]
    
    df = pd.DataFrame.from_dict(time_series_data, orient='index')
    
    # Convert column data to numeric
    numeric_columns = ["1. open", "2. high", "3. low", "4. close", "5. volume"]
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric)
    
    df.index = pd.to_datetime(df.index) # so there's no overlap of years


    df['rsi'] = ta.rsi(df['4. close'], length=window_length)

    return df
    '''# plotting
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['rsi'], label='RSI')
    plt.axhline(y=70, color='r', linestyle='--', label='Overbought (70)')
    plt.axhline(y=30, color='g', linestyle='--', label='Oversold (30)')
    plt.title('Relative Strength Index (RSI)')
    plt.xlabel('Date')
    plt.ylabel('RSI Value')
    plt.legend()
    plt.grid(True)
    plt.show()'''

#Test monthly
#RSI_monthly(fetch.fetchDataMonthly("AAPL"), 4, '0', '0')

#Test weekly
#RSI_weekly(fetch.fetchDataWeekly("AAPL"), 4, '0', '0')

#Test daily
#RSI_daily(fetch.fetchDataDaily("TSLA"), 4, '0', '0')
def convert_to_json(data_frame):
    json_data = {}
    
    for index, row in data_frame.iterrows():
        date = str(index.date())
        rsi_close = row['rsi']

        if not np.isnan(rsi_close):
            json_data[date] = rsi_close
    
    return json_data
with open('data.json', 'r') as file:
    data = json.load(file)
daily_df = RSI_daily(data, 14)
weekly_df = RSI_weekly(data, 14)
monthly_df = RSI_monthly(data, 14)
daily_json_data = convert_to_json(daily_df)
weekly_json_data = convert_to_json(weekly_df)
monthly_json_data = convert_to_json(monthly_df)

combined_json_data = {
    "Daily": daily_json_data,
    "Weekly": weekly_json_data,
    "Monthly": monthly_json_data
}

with open("rsi-close.json", 'w') as output_json_file:
    json.dump(combined_json_data, output_json_file, indent=4)

print("JSON conversion complete.")