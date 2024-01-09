import yfinance as yf
import pandas as pd

def get_financial_info(asset, start_date, end_date):
    #Get financial information for a given asset within a specified date range.
    data = yf.Ticker(asset).history(start=start_date, end=end_date)
    return data

def calculate_returns(data):
    #Calculate daily returns for a given DataFrame.
    data['Daily Returns'] = data['Close'].pct_change()
    return data

def calculate_cumulative_returns(data):
    #Calculate cumulative returns for a given DataFrame.
    data['Cumulative Returns'] = (1 + data['Daily Returns']).cumprod() - 1
    return data

def calculate_average_daily_volume(data):
    # Calculate the average daily volume for a given DataFrame.
    data['Average Volume'] = data['Volume'].mean()
    return data