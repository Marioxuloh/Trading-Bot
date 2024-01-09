import pandas as pd
import matplotlib.pyplot as plt

def calculate_moving_averages(data, window):
    # Calculate simple and exponential moving averages
    data['SMA'] = data['Close'].rolling(window=window, min_periods=1).mean()
    data['EMA'] = data['Close'].ewm(span=window, adjust=False, min_periods=1).mean()
    return data

def find_cross_dates(data):
    # Find Golden Crosses (SMA crosses above EMA) and Death Crosses (SMA crosses below EMA)
    golden_crosses = data[(data['SMA'] > data['EMA']) & (data['SMA'].shift(1) <= data['EMA'].shift(1))]
    death_crosses = data[(data['SMA'] < data['EMA']) & (data['SMA'].shift(1) >= data['EMA'].shift(1))]

    golden_cross_dates = golden_crosses.index
    death_cross_dates = death_crosses.index

    return golden_cross_dates, death_cross_dates

def calculate_and_plot_moving_averages(asset, data):
    # Calculate moving averages with a window of 30 days
    data_with_ma = calculate_moving_averages(data, window=30)

    # Find dates of Golden Crosses and Death Crosses
    golden_cross_dates, death_cross_dates = find_cross_dates(data_with_ma)

    # Add columns for Golden Cross and Death Cross dates
    data['Golden Cross Dates'] = data_with_ma.index.isin(golden_cross_dates)
    data['Death Cross Dates'] = data_with_ma.index.isin(death_cross_dates)

    # Return the DataFrame with moving averages
    return data
