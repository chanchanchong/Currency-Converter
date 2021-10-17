import requests
import json

class CurrencyConverter:
    def __init__(self):
        self.url = "https://www.floatrates.com/daily/{}.json"
        self.cache_list = ['usd', 'eur']
        self.currency_dict = {}
        self.cache = {}
        self.current_currency = ""
        self.new_currency = ""
        self.amount = 0
        self.check_message = "Checking the cache..."
        self.in_cache_message = "Oh! It is in the cache!"
        self.not_cache_message = "Sorry, but it is not in the cache!"
        self.received_message = "You received {} {}."
        self.rate = 0
        self.total = 0

    def currency(self):
        return input().lower()


    def start(self):
        # Receives the current currency
        self.current_currency = self.currency()
        # Retrieve the data from the website dictionary
        self.currency_dict = requests.get(self.url.format(self.current_currency)).json()
        # making the dictionary for saving the exchange rates
        self.cache = {x: y for x, y in self.currency_dict.items() if x in self.cache_list}
        # Save the exchange rates for usd and eur
        with open('currency.json', 'w') as file:
            json.dump(self.cache, file, indent=4)
        # read the currency to exchange for and the amount of money
        # starts the loop
        while True:
            self.new_currency = self.currency()
            if self.new_currency == "":
                break
            self.amount = float(input())
            # if the new currency is in the cache [usd, eur] get it from the file
            # otherwise get in from the dictionary since we already store it
            print(self.check_message)
            if self.new_currency in self.cache:
                print(self.in_cache_message)
                with open('currency.json', 'r') as file:
                    self.cache = json.load(file)
                # calculate the amount
                self.rate = self.cache[f'{self.new_currency}']['rate']
                self.total = round(self.amount * self.rate, 2)
                print(self.received_message.format(self.total, self.new_currency.upper()))
            else:
                print(self.not_cache_message)
                self.rate = self.currency_dict[f'{self.new_currency}']['rate']
                self.total = round(self.amount * self.rate, 2)
                # save the new currency to the file
                self.cache.update({x: y for x, y in self.currency_dict.items() if x == self.new_currency})
                with open('currency.json', 'w') as file:
                    json.dump(self.cache, file, indent=4)
                # print the results
                print(self.received_message.format(self.total, self.new_currency.upper()))


def main():
    cur = CurrencyConverter()
    cur.start()


if __name__ == '__main__':
    main()