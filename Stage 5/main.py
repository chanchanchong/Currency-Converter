# Work on project. Stage 5/6: JSON and the Rates

# Description
# In the previous stages, we worked with different real-world
# currencies but the exchange rates were fixed. Unfortunately (or
# not, depending on your political stance), we dont' really have
# fixed exchange rates in today's world. At this stage, you will
# have to work with the Internet to get the information! The
# FloatRates site contains a special JSON page for each currency.
# Your task is to make requests to these pages and download the
# actual data on the exchange rates of the US dollar and the euro.
# Remember, that the data is stored in JSON format.

# Objectives
# There are many currency codes, for example, RUB, ARS, HNL,
# AUD, MAD, etc. Choose the one you like best and return the
# information about the exchange rates from the site specified
# above for only two currencies: USD and EUR.

# 1. Select one currency code, take it as the user input.
# 2. Make a request to https://www.floatrates.com/daily/YOUR_CURRENCY_COSE.json
#    Don't forget that you need to put the code in lowercase.
# 3. Print your result for USD and EUR.

# Example

# The greater-than symbol followed by a space ( > ) represents
# the user input. Note that it's not part of the input.

#       The results of your output may differ, as the service
#       updates the data once in twelve hours. Don't hesitate to
#       print the whole string for your own interest, but it is not a
#       part of the stage.

# The output for HNL:
# > HNL
# {'code': 'USD', 'alphaCode': 'USD', 'numericCode': '840', 'name': 'U.S. Dollar', 'rate': 0.040212252288502, 'date': 'Sun, 5 Jul 2020 12:00:01 GMT', 'inverseRate': 24.868042526579}
# {'code': 'EUR', 'alphaCode': 'EUR', 'numericCode': '978', 'name': 'Euro', 'rate': 0.035775653590882, 'date': 'Sun, 5 Jul 2020 12:00:01 GMT', 'inverseRate': 27.951970114527}

import requests

class CurrencyConverter:
    def __init__(self):
        self.r = None
        self.code = ""
        self.url = 'http://www.floatrates.com/daily/{}.json'

    def user_input(self):
        return input()

    def request(self):
        self.code = self.user_input().lower()
        self.r = requests.get(self.url.format(self.code))

    def output(self):
        print(self.r.json()['usd'])
        print(self.r.json()['eur'])

    def start(self):
        self.request()
        self.output()


def main():
    cur = CurrencyConverter()
    cur.start()


if __name__ == '__main__':
    main()