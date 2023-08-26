import pandas as pd
import matplotlib.pyplot as plt
import json


def SMA (json_data, timeframe, window_length):
    if (timeframe == 'daily'):
        # Extract Monthly Adjusted Time Series data
        time_series_data = json_data["daily"]["Time Series (Daily)"]

        # Convert data to DataFrame
        df = pd.DataFrame.from_dict(time_series_data, orient='index')

        # Convert column data to numeric
        numeric_columns = ["1. open", "2. high", "3. low", "4. close", "5. volume"]
        df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric)

        # Calculate 3-month Simple Moving Average (SMA)
        df['SMA'] = df['4. close'].rolling(window=window_length).mean()
        print(df['SMA'].to_string())
        print("Daily")
        return df
    
    elif (timeframe == 'weekly'):
        # Extract Monthly Adjusted Time Series data
        time_series_data = json_data["weekly"]["Weekly Adjusted Time Series"]

        # Convert data to DataFrame
        df = pd.DataFrame.from_dict(time_series_data, orient='index')

        # Convert column data to numeric
        numeric_columns = ["1. open", "2. high", "3. low", "4. close", "5. adjusted close", "6. volume", "7. dividend amount"]
        df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric)

        # Calculate 3-month Simple Moving Average (SMA)
        df['SMA'] = df['4. close'].rolling(window=window_length).mean()
        print(df['SMA'].to_string())
        print("Weekly Adjusted")
        return df

    else: 
        # Extract Monthly Adjusted Time Series data
        time_series_data = json_data["monthly"]["Monthly Adjusted Time Series"]

        # Convert data to DataFrame
        df = pd.DataFrame.from_dict(time_series_data, orient='index')

        # Convert column data to numeric
        numeric_columns = ["1. open", "2. high", "3. low", "4. close", "5. adjusted close", "6. volume", "7. dividend amount"]
        df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric)

        # Calculate 3-month Simple Moving Average (SMA)
        df['SMA'] = df['4. close'].rolling(window=window_length).mean()
        print(df['SMA'].to_string())
        print("Monthly Adjusted")
        return df
    # # Plotting
    # df.index=pd.to_datetime(df.index)
    # plt.figure(figsize=(10, 6))
    # plt.plot(df.index, df['4. close'], label='Close Price')
    # plt.plot(df.index, df['SMA'], label='SMA', linestyle='dashed')
    # plt.xlabel('Date')
    # plt.ylabel('Price')
    # plt.title('Simple Moving Average (SMA)')
    # plt.legend()
    # plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    # plt.tight_layout()
    # plt.show()

#Test Daily
#SMA(fetch.fetchDataDaily("AAPL"), 'daily', 3)
#Test Weekly
#SMA(fetch.fetchDataWeekly("AAPL"), 'weekly', 3)
#Test Monthly

with open('data.json', 'r') as file:
    data = json.load(file)

df_daily = SMA(data, 'daily', 3)
daily_data = df_daily['SMA']

df_weekly = SMA(data, 'weekly', 3)
weekly_data = df_weekly['SMA']

df_monthly = SMA(data, 'monthly', 3)
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

with open('combined_data.json', 'w') as file:
    json.dump(combined_data, file, default=str)
