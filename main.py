# CS-finance v.0
# import sys
import yfinance as yf
import pandas as pd

# if len(sys.argv) <= 1:
#     print('Ticker symbol CLI argument missing!')
#     sys.exit(2)

# ticker = sys.argv[1]
ticker = 'TSLA'

# Download 1 month of data for {ticker} at 4-hour intervals
data = pd.DataFrame(yf.download(ticker, period='2y', interval='1h'))
data.to_csv(f'{ticker.lower()}_stock_data_2y.csv')

# import time
# import requests
# from bs4 import BeautifulSoup
#
# # Check for CLI argument
# if len(sys.argv) <= 1:
#     print('Ticker symbol CLI argument missing!')
#     sys.exit(2)
#
# ticker = sys.argv[1]
#
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                          'Chrome/133.0.0.0 Safari/537.36'}
# url = f"https://finance.yahoo.com/quote/{ticker}/"
#
# r = requests.get(url)
#
# # Check if the request was successful
# if r.status_code != 200:
#     print(f"Error fetching data for {ticker}: Status code {r.status_code}")
#
# if r.status_code == 429:
#     retry_after = r.headers.get("Retry-After")
#     print(f"Rate limited. Retry after {retry_after} seconds.")
#     # time.sleep(int(retry_after))
#
# print(r.status_code)
# print(r.text)