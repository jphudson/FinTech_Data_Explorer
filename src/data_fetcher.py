import yfinance as yf
import pandas as pd

def fetch_stock_data(stock, period="1y"):
    """
    Fetch historical stock data for a given stock ticker over a specified period.

    Parameters:
    stock (str): The stock ticker symbol (e.g., 'AAPL').
    period (str): The period over which to fetch historical data (e.g., "1d", "1mo", "1y", "5y", "10y", "max").

    Returns:
    pd.DataFrame: A DataFrame containing the historical stock data, or None if the fetch failed.
    """
    try:
        # Fetch the stock data from Yahoo Finance
        stock_data = yf.Ticker(stock)
        historical_data = stock_data.history(period=period)

        # Check if data is returned
        if historical_data.empty:
            print(f"No data found for {stock}.")
            return None

        # Reset index to get dates as a column
        historical_data.reset_index(inplace=True)
        
        return historical_data
    except Exception as e:
        print(f"Error fetching data for {stock}: {e}")
        return None