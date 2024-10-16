# src/visualizer.py
import matplotlib.pyplot as plt
import seaborn as sns

def plot_stock_data(stock, df, window=20):
    """
    Plots the stock's closing price and daily returns.

    Parameters:
    stock (str): The stock ticker.
    df (pd.DataFrame): The processed DataFrame containing the stock data.
    """
    #Calculate the rolling volatility (standard deviation) based on daily returns
    df['volatility'] = df['daily_return'].rolling(window=window).std()

    # Set up the figure and axes
    fig, axs = plt.subplots(3, figsize=(10, 12))

    # Plot closing prices
    sns.lineplot(data=df, x=df.index, y='close_price', ax=axs[0])
    axs[0].set_title(f'{stock} Closing Prices')
    axs[0].set_xlabel('Date')
    axs[0].set_ylabel('Close Price')

    # Plot daily returns
    sns.lineplot(data=df, x=df.index, y='daily_return', ax=axs[1])
    axs[1].set_title(f'{stock} Daily Returns')
    axs[1].set_xlabel('Date')
    axs[1].set_ylabel('Daily Return')

    # Plot rolling volatility
    sns.lineplot(data=df, x=df.index, y='volatility', ax=axs[2], color='orange')
    axs[2].set_title(f'{stock} Rolling Volatility (Window = {window} Days)')
    axs[2].set_xlabel('Date')
    axs[2].set_ylabel('Volatility')

    plt.tight_layout()
    plt.show()

def plot_volatility_comparison(stock, df, rolling_window=20, historical_window=100):
    """
    Plots the rolling volatility and historical average rolling volatility for a given stock.

    Parameters:
    stock (str): The stock ticker.
    df (pd.DataFrame): The processed DataFrame containing the stock data.
    rolling_window (int): The window size for calculating rolling volatility.
    historical_window (int): The window size for calculating historical average volatility.
    """
    # Calculate rolling volatility
    df['rolling_volatility'] = df['daily_return'].rolling(window=rolling_window).std()

    # Calculate historical average rolling volatility
    df['historical_avg_volatility'] = df['rolling_volatility'].rolling(window=historical_window).mean()

    # Plotting
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x=df.index, y='rolling_volatility', label='20-Day Rolling Volatility', color='blue')
    sns.lineplot(data=df, x=df.index, y='historical_avg_volatility', label='Historical Avg Volatility (100 Days)', color='orange')
    plt.title(f'{stock} Volatility Comparison')
    plt.xlabel('Date')
    plt.ylabel('Volatility')
    plt.legend()
    plt.grid()
    plt.show()