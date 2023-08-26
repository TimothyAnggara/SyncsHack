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
    
def SMA(json_data, timeframe, window_length):
    if (timeframe == 'daily'):
        # Extract Monthly Adjusted Time Series data
        time_series_data = json_data["daily"]["Time Series (Daily)"]

        # Convert data to DataFrame
        df = pd.DataFrame.from_dict(time_series_data, orient='index')

        # Convert column data to numeric
        numeric_columns = ["1. open", "2. high", "3. low", "4. close", "5. volume"]
        df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric)
        df.index=pd.to_datetime(df.index)
        

        df['SMA'] = df['4. close'].rolling(window=window_length).mean()
        # print(df['SMA'].to_string())
        # print("Daily")
        return df
    
    elif (timeframe == 'weekly'):
        # Extract Monthly Adjusted Time Series data
        time_series_data = json_data['weekly']["Weekly Adjusted Time Series"]

        # Convert data to DataFrame
        df = pd.DataFrame.from_dict(time_series_data, orient='index')

        # Convert column data to numeric
        numeric_columns = ["1. open", "2. high", "3. low", "4. close", "5. adjusted close", "6. volume", "7. dividend amount"]
        df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric)
        df.index=pd.to_datetime(df.index)


        df['SMA'] = df['4. close'].rolling(window=window_length).mean()
        # print(df['SMA'].to_string())
        # print("Weekly Adjusted")
        return df

    else: 
        # Extract Monthly Adjusted Time Series data
        time_series_data = json_data['monthly']["Monthly Adjusted Time Series"]

        # Convert data to DataFrame
        df = pd.DataFrame.from_dict(time_series_data, orient='index')
        df.index=pd.to_datetime(df.index)

        # Convert column data to numeric
        numeric_columns = ["1. open", "2. high", "3. low", "4. close", "5. adjusted close", "6. volume", "7. dividend amount"]
        df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric)

        df['SMA'] = df['4. close'].rolling(window=window_length).mean()
        # print(df['SMA'].to_string())
        # print("Monthly Adjusted")
        return df

    # Plotting
    df.index=pd.to_datetime(df.index)
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['4. close'], label='Close Price')
    plt.plot(df.index, df['SMA'], label='SMA', linestyle='dashed')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Simple Moving Average (SMA)')
    plt.legend()
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()
    plt.show()

#Test Daily
#SMA(fetch.fetchDataDaily("AAPL"), 'daily', 3)
#Test Weekly
#SMA(fetch.fetchDataWeekly("AAPL"), 'weekly', 3)
#Test Monthly
# SMA(fetch.fetchDataMonthly("AAPL"), 'monthly', 3)
def convert_to_json(data_frame):
    json_data = {}
    
    for index, row in data_frame.iterrows():
        date = str(index.date())
        sma_close = row['SMA']

        if not np.isnan(sma_close):
            json_data[date] = sma_close
    
    return json_data
with open('data.json', 'r') as file:
    data = json.load(file)
daily_df = SMA(data, 'daily', 3)
weekly_df = SMA(data, 'weekly', 3)
monthly_df = SMA(data, 'monthly', 3)
daily_json_data = convert_to_json(daily_df)
weekly_json_data = convert_to_json(weekly_df)
monthly_json_data = convert_to_json(monthly_df)

combined_json_data = {
    "Daily": daily_json_data,
    "Weekly": weekly_json_data,
    "Monthly": monthly_json_data
}

with open("sma-close.json", 'w') as output_json_file:
    json.dump(combined_json_data, output_json_file, indent=4)

print("JSON conversion complete.")