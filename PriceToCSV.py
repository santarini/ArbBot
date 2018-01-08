#Internal Arbitrage

import time
import datetime
import random
from selenium import webdriver
import csv

#start timer
start_time = time.time()

#Bithumb

driver = webdriver.Edge('C:\Program Files\Python\Python36\MicrosoftWebDriver.exe')
driver.get('https://www.bithumb.com/');

#btc
btc_bithumb_outterHTML = driver.find_element_by_id('assetRealBTC')
btc_bithumb_innerHTML = btc_bithumb_outterHTML.get_attribute('innerHTML')
#xrp
xrp_bithumb_outterHTML = driver.find_element_by_id('assetRealXRP')
xrp_bithumb_innerHTML = xrp_bithumb_outterHTML.get_attribute('innerHTML')
#eth
eth_bithumb_outterHTML = driver.find_element_by_id('assetRealETH')
eth_bithumb_innerHTML = eth_bithumb_outterHTML.get_attribute('innerHTML')
#bch
bch_bithumb_outterHTML = driver.find_element_by_id('assetRealBCH')
bch_bithumb_innerHTML = bch_bithumb_outterHTML.get_attribute('innerHTML')
#ltc
ltc_bithumb_outterHTML = driver.find_element_by_id('assetRealLTC')
ltc_bithumb_innerHTML = ltc_bithumb_outterHTML.get_attribute('innerHTML')
#dash
dash_bithumb_outterHTML = driver.find_element_by_id('assetRealDASH')
dash_bithumb_innerHTML = dash_bithumb_outterHTML.get_attribute('innerHTML')
#xmr
xmr_bithumb_outterHTML = driver.find_element_by_id('assetRealXMR')
xmr_bithumb_innerHTML = xmr_bithumb_outterHTML.get_attribute('innerHTML')
#eos
eos_bithumb_outterHTML = driver.find_element_by_id('assetRealEOS')
eos_bithumb_innerHTML = eos_bithumb_outterHTML.get_attribute('innerHTML')
#qtum
qtum_bithumb_outterHTML = driver.find_element_by_id('assetRealQTUM')
qtum_bithumb_innerHTML = qtum_bithumb_outterHTML.get_attribute('innerHTML')
#btg
btg_bithumb_outterHTML = driver.find_element_by_id('assetRealBTG')
btg_bithumb_innerHTML = btg_bithumb_outterHTML.get_attribute('innerHTML')
#etc
etc_bithumb_outterHTML = driver.find_element_by_id('assetRealETC')
etc_bithumb_innerHTML = etc_bithumb_outterHTML.get_attribute('innerHTML')
#zec
zec_bithumb_outterHTML = driver.find_element_by_id('assetRealZEC')
zec_bithumb_innerHTML = zec_bithumb_outterHTML.get_attribute('innerHTML')

driver.quit()

#CoinMarketCap

driver = webdriver.Chrome()
driver.get('https://coinmarketcap.com/');

#btc
btc_cmc_outterHTML = driver.find_element_by_xpath('//*[@id="id-bitcoin"]/td[4]/a')
btc_cmc_innerHTML = btc_cmc_outterHTML.get_attribute('innerHTML')
#xrp
xrp_cmc_outterHTML = driver.find_element_by_xpath('//*[@id="id-ripple"]/td[4]/a')
xrp_cmc_innerHTML = xrp_cmc_outterHTML.get_attribute('innerHTML')
#eth
eth_cmc_outterHTML = driver.find_element_by_xpath('//*[@id="id-ethereum"]/td[4]/a')
eth_cmc_innerHTML = eth_cmc_outterHTML.get_attribute('innerHTML')
#bch
bch_cmc_outterHTML = driver.find_element_by_xpath('//*[@id="id-bitcoin-cash"]/td[4]/a')
bch_cmc_innerHTML = bch_cmc_outterHTML.get_attribute('innerHTML')
#ltc
ltc_cmc_outterHTML = driver.find_element_by_xpath('//*[@id="id-litecoin"]/td[4]/a')
ltc_cmc_innerHTML = ltc_cmc_outterHTML.get_attribute('innerHTML')
#dash
dash_cmc_outterHTML = driver.find_element_by_xpath('//*[@id="id-dash"]/td[4]/a')
dash_cmc_innerHTML = dash_cmc_outterHTML.get_attribute('innerHTML')
#xmr
xmr_cmc_outterHTML = driver.find_element_by_xpath('//*[@id="id-monero"]/td[4]/a')
xmr_cmc_innerHTML = xmr_cmc_outterHTML.get_attribute('innerHTML')
#eos
eos_cmc_outterHTML = driver.find_element_by_xpath('//*[@id="id-eos"]/td[4]/a')
eos_cmc_innerHTML = eos_cmc_outterHTML.get_attribute('innerHTML')
#qtum
qtum_cmc_outterHTML = driver.find_element_by_xpath('//*[@id="id-qtum"]/td[4]/a')
qtum_cmc_innerHTML = qtum_cmc_outterHTML.get_attribute('innerHTML')
#btg
btg_cmc_outterHTML = driver.find_element_by_xpath('//*[@id="id-bitcoin-gold"]/td[4]/a')
btg_cmc_innerHTML = btg_cmc_outterHTML.get_attribute('innerHTML')
#etc
etc_cmc_outterHTML = driver.find_element_by_xpath('//*[@id="id-ethereum-classic"]/td[4]/a')
etc_cmc_innerHTML = etc_cmc_outterHTML.get_attribute('innerHTML')
#zec
zec_cmc_outterHTML = driver.find_element_by_xpath('//*[@id="id-zcash"]/td[4]/a')
zec_cmc_innerHTML = zec_cmc_outterHTML.get_attribute('innerHTML')

driver.quit()

#Output to CSV

with open('CryptoData.csv', 'w') as csvfile:
    fieldnames = ['Coin', 'Symbol', 'AverageValue', 'BithumbValue', 'ArbOpp']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator = '\n')

    writer.writeheader()
    writer.writerow({'Coin': 'Bitcoin', 'Symbol': 'BTC', 'AverageValue': btc_cmc_innerHTML, 'BithumbValue': btc_bithumb_innerHTML})
    writer.writerow({'Coin': 'Ripple', 'Symbol': 'XRP', 'AverageValue': xrp_cmc_innerHTML, 'BithumbValue': xrp_bithumb_innerHTML})
    writer.writerow({'Coin': 'Ethereum', 'Symbol': 'ETH', 'AverageValue':eth_cmc_innerHTML, 'BithumbValue': eth_bithumb_innerHTML})
    writer.writerow({'Coin': 'Bitcoin Cash', 'Symbol': 'BCH', 'AverageValue': bch_cmc_innerHTML, 'BithumbValue': bch_bithumb_innerHTML})
    writer.writerow({'Coin': 'Litecoin', 'Symbol': 'LTC', 'AverageValue': ltc_cmc_innerHTML, 'BithumbValue': ltc_bithumb_innerHTML})
    writer.writerow({'Coin': 'Dash', 'Symbol': 'DASH', 'AverageValue': dash_cmc_innerHTML, 'BithumbValue': dash_bithumb_innerHTML})
    writer.writerow({'Coin': 'Monero', 'Symbol': 'XMR', 'AverageValue': xmr_cmc_innerHTML, 'BithumbValue': xmr_bithumb_innerHTML})
    writer.writerow({'Coin': 'EOS', 'Symbol': 'EOS', 'AverageValue': eos_cmc_innerHTML, 'BithumbValue': eos_bithumb_innerHTML})
    writer.writerow({'Coin': 'Qtum', 'Symbol': 'QTUM', 'AverageValue': qtum_cmc_innerHTML, 'BithumbValue': qtum_bithumb_innerHTML})
    writer.writerow({'Coin': 'Bitcoin Gold', 'Symbol': 'BTG', 'AverageValue': btg_cmc_innerHTML, 'BithumbValue': btg_bithumb_innerHTML})
    writer.writerow({'Coin': 'Ethereum Classic', 'Symbol': 'ETC', 'AverageValue': etc_cmc_innerHTML, 'BithumbValue': etc_bithumb_innerHTML})
    writer.writerow({'Coin': 'Zcash', 'Symbol': 'ZEC', 'AverageValue': zec_cmc_innerHTML, 'BithumbValue': zec_bithumb_innerHTML})

#print time 
elapsed_time = time.time() - start_time
print("%.2f" % elapsed_time, " seconds")

