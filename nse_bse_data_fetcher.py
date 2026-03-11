import requests
import pandas as pd

class StockDataFetcher:
    def __init__(self, stock_symbol):
        self.stock_symbol = stock_symbol

    def fetch_nse_data(self):
        # Fetch data from NSE
        try:
            url = f'https://www.nseindia.com/api/quote-equity?symbol={self.stock_symbol}'
            headers = {
                'User-Agent': 'Mozilla/5.0',
                'Accept': 'application/json'
            }
            response = requests.get(url, headers=headers)
            data = response.json()
            return data
        except Exception as e:
            print(f'Error fetching NSE data: {e}')
            return None

    def fetch_bse_data(self):
        # Fetch data from BSE
        try:
            url = f'https://api.bseindia.com/BseIndiaAPI/Intraday/GetData?strCode={self.stock_symbol}'
            response = requests.get(url)
            data = response.json()
            return data
        except Exception as e:
            print(f'Error fetching BSE data: {e}')
            return None

    def fetch_data(self):
        nse_data = self.fetch_nse_data()
        bse_data = self.fetch_bse_data()
        return nse_data, bse_data

if __name__ == '__main__':
    stock_symbol = input('Enter stock symbol: ')  # Example: 'RELIANCE'
    fetcher = StockDataFetcher(stock_symbol)
    nse_data, bse_data = fetcher.fetch_data()
    print('NSE Data:', nse_data)
    print('BSE Data:', bse_data)