# CryptoFund - Trade Algo
# Alex Markowitz & Mickey Friedman
# Version 1.0 - 4/22/18
import krakenex
from pykrakenapi import KrakenAPI
import numpy as np

#API stuff
k = krakenex.API()
k.load_key('kraken.key')

# Buy assets with unweighted index
def buy_assets(dollar_amount, currency_list):
    n_currencies = np.size(currency_list)
    amt_per_currency = dollar_amount/n_currencies

    for currency in currency_list:
        k.query_private('AddOrder', {'pair': currency,
                                 'type': 'buy',
                                 'ordertype': 'market',
                                 'price': amt_per_currency})

# Periodically query to construct a price history
# date is a string that gives the date of the query to sort the data for further analysis
def construct_price_history(date):
    Data = k.query_public('AssetPairs')
    np.savetxt(Data,'data_query'+date+'.csv', delimiter=',')

#Algorithm
def main():
    balance = k.query_private('Balance')
    orders = k.query_private('OpenOrders')

    balance = balance['result']
    orders = orders['result']

    dollar_amount = k.TradeBalance(???, "ZUSD")
    currency_list = ??
    buy_assets(dollar_amount, currency_list)

#run main program
main()
