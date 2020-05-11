import requests, sys
from currency.models import Currencies
from CurrencyXchange import constants

def get_currency_converted_balance(prev, current, balance):
    try:
        print('Current Currency ',current)  # INR
        print('Previous Currency ',prev)    # USD
        url = constants.EXCHANGE_API
        res = requests.get(url, params={'base':prev, 'symbols':current}).json()   # USD
        curr_rate = res['rates'][current]  #USD
        balance = balance*curr_rate
        print("This is balance : ",balance)
        return balance
    except Exception as e:
        print('Exception in API currency converted balance ...',e)
        print("Line no : {}".format(sys.exc_info()[-1].tb_lineno))
