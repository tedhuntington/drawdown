from pandas_datareader import data as pdr
from datetime import datetime

def get_data(symbol):
    #data = pdr.get_data_yahoo(symbol)
    start = datetime(1928,1,2)
    end = datetime.now()
    data = pdr.DataReader(symbol, 'yahoo', start, end)
    data = data.reset_index()
    data = data.rename(columns={
        'Date': 'd',
        'High': 'high',
        'Low': 'low',
        'Close': 'close',
        'Adj Close': 'value',
        'Open': 'open',
        'Volume': 'volume'
    })

    return data
