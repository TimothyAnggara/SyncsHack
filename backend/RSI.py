import pandas as pd
import matplotlib.pyplot as plt
import json

def calculate_rsi(data, window_length):
    delta = data.diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=window_length).mean()
    avg_loss = loss.rolling(window=window_length).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def RSI_monthly(datajson, window_length, start_date, end_date):
    #with open(json.dumps(datajson), 'r') as json_file: OPENS FILE
    #    json_data = json.load(json_file) , turns file into json object
    json_data = datajson # datajson is a json file

    # extract monthly adjusted time series data
    time_series_data = json_data['monthly']["Monthly Adjusted Time Series"]
    
    df = pd.DataFrame(time_series_data).T
    df.index = pd.to_datetime(df.index) # so there's no overlap of years

    df = df.apply(pd.to_numeric, errors='coerce') 

    if (start_date == '0') & (end_date == '0'): # no start/end date = default ALL months
        pass
    else:
        filtered_df = df[(df.index >= start_date) & (df.index <= end_date)]
        df = filtered_df

    df['rsi'] = calculate_rsi(df['4. close'], window_length)
    #print(df['rsi'])

    return df # for silvey, possibly need .toString like pudding said??

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
    

def RSI_weekly(datajson, window_length, start_date, end_date):
    #with open(json.dumps(datajson), 'r') as json_file: OPENS FILE
    #    json_data = json.load(json_file) , turns file into json object
    json_data = datajson # datajson is a json file

    # extract weekly adjusted time series data
    time_series_data = json_data['weekly']["Weekly Adjusted Time Series"]
    
    df = pd.DataFrame(time_series_data).T
    df.index = pd.to_datetime(df.index) # so there's no overlap of years

    df = df.apply(pd.to_numeric, errors='coerce') 

    if (start_date == '0') & (end_date == '0'): # no start/end date = default ALL
        pass
    else:
        filtered_df = df[(df.index >= start_date) & (df.index <= end_date)]
        df = filtered_df

    df['rsi'] = calculate_rsi(df['4. close'], window_length)
    #print(df['rsi'])

    return df # for silvey, possibly need .toString like pudding said??

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


def RSI_daily(datajson, window_length, start_date, end_date):
    #with open(json.dumps(datajson), 'r') as json_file: OPENS FILE
    #    json_data = json.load(json_file) , turns file into json object
    json_data = datajson # datajson is a json file

    # extract weekly adjusted time series data
    time_series_data = json_data["daily"]["Time Series (Daily)"]
    
    df = pd.DataFrame(time_series_data).T
    df.index = pd.to_datetime(df.index) #change so there's no overlap of years

    df = df.apply(pd.to_numeric, errors='coerce')

    if (start_date == '0') & (end_date == '0'): # no start/end date = default ALL data
        pass
    else:
        filtered_df = df[(df.index >= start_date) & (df.index <= end_date)]
        df = filtered_df

    df['rsi'] = calculate_rsi(df['4. close'], window_length)
    #print(df['rsi'])
    
    return df # for silvey, possibly need .toString like pudding said??

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

with open('data.json', 'r') as file:
    data = json.load(file)
#Test monthly
#RSI_monthly(fetch.fetchDataMonthly("AAPL"), 4, '0', '0')

#Test weekly
#RSI_weekly(fetch.fetchDataWeekly("AAPL"), 4, '0', '0')

#Test daily
window_length = 14
start_date = '0'
end_date = '0'

df_daily = RSI_daily(data, window_length, start_date, end_date)
daily_rsi_data = df_daily['rsi']

df_weekly = RSI_weekly(data, window_length, start_date, end_date)
weekly_rsi_data = df_weekly['rsi']

df_monthly = RSI_monthly(data, window_length, start_date, end_date)
monthly_rsi_data = df_monthly['rsi']

# Convert Timestamps to strings for each RSI dictionary
daily_rsi_dict = daily_rsi_data.reset_index().astype(str).set_index('index').to_dict()['rsi']
weekly_rsi_dict = weekly_rsi_data.reset_index().astype(str).set_index('index').to_dict()['rsi']
monthly_rsi_dict = monthly_rsi_data.reset_index().astype(str).set_index('index').to_dict()['rsi']


# 2. Convert the 'rsi' column from each dataframe to a dictionary
# daily_rsi_dict = daily_rsi_data.to_dict()
# weekly_rsi_dict = weekly_rsi_data.to_dict()
# monthly_rsi_dict = monthly_rsi_data.to_dict()

# 3. Combine these dictionaries into a single dictionary
combined_rsi_data = {
    "daily": daily_rsi_dict,
    "weekly": weekly_rsi_dict,
    "monthly": monthly_rsi_dict
}

# 4. Serialize the final combined dictionary to a JSON format
combined_rsi_json = json.dumps(combined_rsi_data, default=str, indent=4)

# 5. Save the JSON string to a file
with open('combined_rsi_data.json', 'w') as file:
    file.write(combined_rsi_json)

