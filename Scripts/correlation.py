import pandas as pd

nifty_data = pd.read_csv("D:\\MI\\trial\\starter\\sp500-nifty50-analysis\\Data\\NIFTY 50_.csv")
sp_data = pd.read_csv("D:\\MI\\trial\\starter\\sp500-nifty50-analysis\\Data\\S&P 500.csv")
# Handle mixed date formats for S&P 500
def parse_dates(date):
    for fmt in ('%m/%d/%Y', '%m-%d-%Y'):
        try:
            return pd.to_datetime(date, format=fmt)
        except ValueError:
            continue
    return pd.NaT

sp_data['Date'] = sp_data['Date'].apply(parse_dates)
sp_data = sp_data.drop(["Vol."],axis = 1)
sp_data = sp_data.drop(["Change %"],axis = 1)

# Convert Date column to datetime and remove time info
nifty_data['Date'] = pd.to_datetime(nifty_data['Date']).dt.date

nifty_data = nifty_data.drop(['Index Name'],axis = 1)
nifty_data['change'] = nifty_data['Close'].pct_change() * 100
nifty_data['change'] = nifty_data['change'].round(2)
nifty_data = nifty_data.dropna()
# Convert Date columns to datetime for both datasets
nifty_data['Date'] = pd.to_datetime(nifty_data['Date'])
sp_data['Date'] = pd.to_datetime(sp_data['Date'])

# Merge datasets on the Date column
combined_data = pd.merge(nifty_data[['Date', 'change']], 
                         sp_data[['Date', 'change']], 
                         on='Date', 
                         suffixes=('_NIFTY', '_SP'))

# Display the first few rows to verify
print(combined_data.shape)


from scipy.stats import spearmanr

# Calculate Pearson correlation
corr, p_value = spearmanr(combined_data['change_NIFTY'], combined_data['change_SP'])

# Display results
print(f"Pearson Correlation: {corr:.2f}")
print(f"P-value: {p_value:.4f}")

if p_value < 0.05:
    print("The correlation is statistically significant.")
else:
    print("The correlation is not statistically significant.")


