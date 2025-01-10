import pandas as pd

nifty_data = pd.read_csv("D:\\MI\\trial\\starter\\sp500-nifty50-analysis\\\Data\\NIFTY50.csv")
sp_data = pd.read_csv("D:\\MI\\trial\\starter\\sp500-nifty50-analysis\\Data\\S&P 500.csv")
sp_data['Date'] = pd.to_datetime(sp_data['Date'], format='mixed')



# Convert Date column to datetime and remove time info
nifty_data['Date'] = pd.to_datetime(nifty_data['Date']).dt.date
