from pandas_datareader import data as DataReader

df = DataReader.get_data_yahoo("SPY", start="2017-01-01", end="2017-04-30")

print(df)
