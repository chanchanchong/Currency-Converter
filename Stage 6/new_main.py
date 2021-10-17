import requests
import json


def main():
    url = "https://www.floatrates.com/daily/{}.json"
    cache_list = ['usd', 'eur']
    # Receive the current currency
    current_currency = input().lower()
    # Retrieve the data from the website dictionary
    currency_dict = requests.get(url.format(current_currency)).json()
    # Save the exchange rates for usd and eur
    cache = {x: y for x, y in currency_dict.items() if x in cache_list}
    with open('currency.json', 'w') as file:
        json.dump(cache, file, indent=4)
    # read the currency to exchange for and the amount of money
    # starts the loop
    while True:
        new_currency = input().lower()
        if new_currency == "":
            break
        amount = float(input())
        # if the new currency is in the cache [usd, eur] get it from the file
        # otherwise get in from the dictionary
        print("Checking the cache...")
        if new_currency in cache:
            print("Oh! It is in the cache!")
            with open('currency.json', 'r') as file:
                cache = json.load(file)
            # calculate the amount
            rate = cache[f'{new_currency}']['rate']
            print(f"You received {round(amount * rate, 2)} {new_currency.upper()}.")
        # otherwise get it from the site and calculate the amount
        else:
            print("Sorry, but it is not in the cache!")
            rate = currency_dict[f'{new_currency}']['rate']
            # save the info to the file
            cache.update({x: y for x, y in currency_dict.items() if x == new_currency})
            with open('currency.json', 'w') as file:
                json.dump(cache, file, indent=4)
            # print the results
            print(f"You received {round(amount * rate, 2)} {new_currency.upper()}.")


if __name__ == '__main__':
    main()
