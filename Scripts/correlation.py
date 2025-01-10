import pandas as pd

nifty_data = pd.read_csv("NIFTY50.csv")
sp_data = pd.read_csv("S&P 500.csv")
sp_data['Date'] = pd.to_datetime(sp_data['Date'], format='%d-%m-%Y')

# Convert Date column to datetime and remove time info
nifty_data['Date'] = pd.to_datetime(nifty_data['Date']).dt.date