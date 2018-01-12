#Alexander Galea(https://github.com/agalea91) did all the heavy lifting

import requests
import datetime
import pandas as pd
import matplotlib.pyplot as plt

def priceUSD(symbol, comparison_symbols=['USD'], exchange=''):
    url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}'\
            .format(symbol.upper(), ','.join(comparison_symbols).upper())
    if exchange:
        url += '&e={}'.format(exchange)
    page = requests.get(url)
    data = page.json()
    return data

def priceKRW(symbol, comparison_symbols=['KRW'], exchange=''):
    url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}'\
            .format(symbol.upper(), ','.join(comparison_symbols).upper())
    if exchange:
        url += '&e={}'.format(exchange)
    page = requests.get(url)
    data = page.json()
    return data

print("Coinbase ", priceUSD('BTC', exchange='Coinbase'))
print("Bitfinex ", priceUSD('BTC', exchange='Bitfinex'))
print("Gemini ", priceUSD('BTC', exchange='Gemini'))
print("Bitflyer ", priceUSD('BTC', exchange='Bitflyer'))

#Bithumb bunch
print("\n Bithumb Bunch")
print("Bitcoin ", priceKRW('BTC', exchange='Bithumb'))
print("Ripple ", priceKRW('XRP', exchange='Bithumb'))
print("Ethereum ", priceKRW('ETH', exchange='Bithumb'))
print("Bitcoin Cash ", priceKRW('BCH', exchange='Bithumb'))
print("Litecoin ", priceKRW('LTC', exchange='Bithumb'))
print("Dash ", priceKRW('DASH', exchange='Bithumb'))
print("Monero ", priceKRW('XMR', exchange='Bithumb'))
##print("EOS ", priceKRW('EOS', exchange='Bithumb'))
##print("Qtum ", priceKRW('QTUM', exchange='Bithumb'))
print("Bitcoin Gold ", priceKRW('BTG', exchange='Bithumb'))
print("Ethereum Classic ", priceKRW('ETC', exchange='Bithumb'))
print("Zcash ", priceKRW('ZEC', exchange='Bithumb'))

