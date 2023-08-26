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
       

def daily_ema(json_data, periods):
    time_series_data = json_data["daily"]["Time Series (Daily)"]

    # Convert data to DataFrame
    df = pd.DataFrame.from_dict(time_series_data, orient='index')

    # Convert column data to numeric
    numeric_columns = ["1. open", "2. high", "3. low", "4. close"]
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric)
    
    df['EMA-open'] = ta.ema(df['1. open'], length=periods)
    df['EMA-high'] = ta.ema(df['2. high'], length=periods)
    df['EMA-low'] = ta.ema(df['3. low'], length=periods)
    df['EMA-close'] = ta.ema(df['4. close'], length=periods)

    df.index=pd.to_datetime(df.index)
    # Uncomment if need tostring
    # print(df['EMA-open'].to_string())
    # print(df['EMA-high'].to_string())
    # print(df['EMA-low'].to_string())
    # print(df['EMA-close'].to_string())
    
    # # Plotting
    # plt.figure()

    # # Price data
    # plt.plot(df.index, df['4. close'], label='Price', color='blue')

    # # EMA-close
    # plt.plot(df.index, df['EMA-close'], label='EMA-close', color='red')

    # plt.xlabel('Date')
    # plt.ylabel('Price')
    # plt.title('Price and EMA-close Plot')
    # plt.legend()
    # plt.grid(True)
    # plt.savefig('daily_ema_close.png')
    return df

def weekly_ema(json_data, periods):
    time_series_data = json_data["weekly"]["Weekly Adjusted Time Series"]

    # Convert data to DataFrame
    df = pd.DataFrame.from_dict(time_series_data, orient='index')

    # Convert column data to numeric
    numeric_columns = ["1. open", "2. high", "3. low", "4. close"]
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric)
    
    df['EMA-open'] = ta.ema(df['1. open'], length=periods)
    df['EMA-high'] = ta.ema(df['2. high'], length=periods)
    df['EMA-low'] = ta.ema(df['3. low'], length=periods)
    df['EMA-close'] = ta.ema(df['4. close'], length=periods)

    df.index=pd.to_datetime(df.index)
    # Uncomment if need tostring
    # print(df['EMA-open'].to_string())
    # print(df['EMA-high'].to_string())
    # print(df['EMA-low'].to_string())
    # print(df['EMA-close'].to_string())
    # Plotting
    # plt.figure()

    # # Price data
    # plt.plot(df.index, df['4. close'], label='Price', color='blue')

    # # EMA-close
    # plt.plot(df.index, df['EMA-close'], label='EMA-close', color='red')

    # plt.xlabel('Date')
    # plt.ylabel('Price')
    # plt.title('Price and EMA-close Plot')
    # plt.legend()
    # plt.grid(True)
    # plt.savefig('weekly_ema.png')
    return df 

def monthly_ema(json_data, periods):
    time_series_data = json_data["monthly"]["Monthly Adjusted Time Series"]

    # Convert data to DataFrame
    df = pd.DataFrame.from_dict(time_series_data, orient='index')

    # Convert column data to numeric
    numeric_columns = ["1. open", "2. high", "3. low", "4. close"]
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric)
    
    df['EMA-open'] = ta.ema(df['1. open'], length=periods)
    df['EMA-high'] = ta.ema(df['2. high'], length=periods)
    df['EMA-low'] = ta.ema(df['3. low'], length=periods)
    df['EMA-close'] = ta.ema(df['4. close'], length=periods)

    df.index=pd.to_datetime(df.index)
    # Uncomment if need tostring
    # print(df['EMA-open'].to_string())
    # print(df['EMA-high'].to_string())
    # print(df['EMA-low'].to_string())
    # print(df['EMA-close'].to_string())

    # Plotting
    # plt.figure()

    # # Price data
    # plt.plot(df.index, df['4. close'], label='Price', color='blue')

    # # EMA-close
    # plt.plot(df.index, df['EMA-close'], label='EMA-close', color='red')

    # plt.xlabel('Date')
    # plt.ylabel('Price')
    # plt.title('Price and EMA-close Plot')
    # plt.legend()
    # plt.grid(True)
    # plt.savefig('monthly_ema.png')
    return df

def convert_to_json(data_frame):
    json_data = {}
    
    for index, row in data_frame.iterrows():
        date = str(index.date())
        ema_close = row['EMA-close']

        if not np.isnan(ema_close):
            json_data[date] = ema_close
    
    return json_data


with open('data.json', 'r') as file:
    data = json.load(file)
daily_df = daily_ema(data, 20)
weekly_df = weekly_ema(data, 20)
monthly_df = monthly_ema(data, 20)
daily_json_data = convert_to_json(daily_df)
weekly_json_data = convert_to_json(weekly_df)
monthly_json_data = convert_to_json(monthly_df)

combined_json_data = {
    "Daily": daily_json_data,
    "Weekly": weekly_json_data,
    "Monthly": monthly_json_data
}   

with open("ema-close.json", 'w') as output_json_file:
    json.dump(combined_json_data, output_json_file, indent=4)

print("JSON conversion complete.")