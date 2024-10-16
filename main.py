import pandas as pd
from src.data_fetcher import *
from src.data_processor import *
from src.visualizer import *  # Import the plot function

def main():
    # Example stock tickers CSV file
    stock_file = 'data/example/stock_tickers.csv'
    stocks = pd.read_csv(stock_file)['Ticker'].tolist()
    i = 0
    # Loop through each stock and fetch and process the data
    for stock in stocks:
        print(f"Processing data for {stock}...")
        # Fetch historical data for the stock
        stock_data = fetch_stock_data(stock, period="1y")
        
        if stock_data is not None:
            # Process the data (clean and calculate metrics)
            processed_df, volatility = process_stock_data(stock_data)
            
            # Save processed data
            processed_df.to_csv(f"data/processed/{stock}_processed.csv", index=False)
            
        else:
            print(f"Failed to retrieve data for {stock}")

if __name__ == "__main__":
    main()