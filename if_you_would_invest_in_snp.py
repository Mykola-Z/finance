# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 13:51:47 2021

@author: mzly903
"""

from datetime import datetime
import requests

from_date = datetime.strptime("1-1-1990", "%d-%m-%Y")
till_date = datetime.now()

# convert current date into timestamp
start = int(datetime.timestamp(from_date))
end = int(datetime.timestamp(till_date))


def get_prices(ticker, interval="1mo"):

    url = "https://query1.finance.yahoo.com/v8/finance/chart/" + ticker
    params = {"period1": start, "period2": end}
    params["interval"] = interval.lower()
    params["includePrePost"] = 'False'
    params["events"] = "div,splits"
    proxy = {"https": None}
    data = requests.get(url=url, params=params, proxies=proxy)
    content = data.json()
    prices = content["chart"]["result"][0]['indicators']['quote'][0]['close']
    return prices

ticker = "^GSPC"  # "^GSPC" for s&p500
prices = get_prices(ticker)

montly_invest = 250
portfolio = 0
invested = 0

for i in range(len(prices)):
    portfolio += montly_invest/prices[i]
    invested += montly_invest

print("invested", invested)
print("portfolio", portfolio*prices[-1])
