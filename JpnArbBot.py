import time
import datetime
import random
from selenium import webdriver
import decimal

driver = webdriver.Edge('C:\Program Files\Python\Python36\MicrosoftWebDriver.exe')
driver.get('https://cryptowat.ch/gemini/btcusd');
time.sleep(1)
gem_out = driver.find_element_by_id('price-ticker')
btcgem_inner = gem_out.get_attribute('innerHTML')
btcgem = btcgem_inner[len("<weak></weak><span>"):-len(" USD</span>")]
a = float(btcgem)
print("Gem BTC USD: ", a)
time.sleep(1)
driver.get('https://cryptowat.ch/bitflyer/btcjpy');
fly_out = driver.find_element_by_id('price-ticker')
btcfly_inner = fly_out.get_attribute('innerHTML')
btcfly = btcfly_inner[len("<weak></weak><span>"):-len(" JPY</span>")]
b = float(btcfly)
print("Fly BTC JPY: ", b)
driver.get('https://www.barchart.com/forex/quotes/%5EUSDJPY');
jpyusd_out = driver.find_element_by_class_name('last-change')
jpyusd_inner = jpyusd_out.get_attribute('innerHTML')
c = float(jpyusd_inner)
print("USD/JPY: ", c)
arb = ((a/b)/c)
print ("The current arb is :", arb)
driver.quit()
