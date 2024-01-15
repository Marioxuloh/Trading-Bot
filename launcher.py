import yfinance as yf
import financial_analysis
import trading_bot
from moving_averages import calculate_moving_averages_and_crosses
from tabulate import tabulate

# Read the scopes of our trading bot
with open("scope.txt", "r") as fscope:
    scope = fscope.read().splitlines()

# period time 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
period = "1wk"

#window suele ser de 50 y 200 sesiones
window = 50

# Table header
table_header = ["Asset", "Trading Advice", "Period"]

# Table data
table_data = []

# Collect data about each asset from yfinance
for asset in scope:
    # Get historical price data for the last 6 months
    data = yf.Ticker(asset).history(period)

    # Apply financial analysis module
    data_with_returns = financial_analysis.calculate_returns(data)
    data_with_cumulative_returns = financial_analysis.calculate_cumulative_returns(data_with_returns)
    data_with_avg_volume = financial_analysis.calculate_average_daily_volume(data_with_cumulative_returns)

    # Calculate and plot moving averages with additional financial analysis, and set de window for calculate it
    data_with_ma_crosses = calculate_moving_averages_and_crosses(asset, data_with_avg_volume, window)

    # Use the trading bot to get advice
    bot_advice = trading_bot.bot_advice(data_with_ma_crosses)

    # Add data to the table
    table_data.append([asset, bot_advice, period])

# Print the table
print(tabulate(table_data, headers=table_header, tablefmt="fancy_grid"))
