# Stage 4/6: Going global

# Description:

# You can convert your conicoins into dollars, cool. What if
# you want a different currency? What if you're going to
# Morocco tomorrow? You'll need some dirhams, that's
# for sure. We need to improve our converter.

# Take the imaginary exchange rates below and modify
# your program to work with 5 different currencies:

# - RUB - Russian Ruble; 1 conicoin = 2.98 RUB;
# - ARS - Argentine Peso; 1 conicoin = 0.82 ARS;
# - HNL - Honduran Lempira; 1 conicoin = 0.17 HNL;
# - AUD - Australian Dollar; 1 conicoin = 1.9622 AUD;
# - MAD - Moroccan Dirham; 1 conicoin = 0.208 MAD;

# Take the number of conicoins as the user input, convert
# it to the specified currencies, and round the result to
# two decimals using the Python built-in function. Notice
# that the input number can have a fractional part!

# Objectives

# 1. Get the number of conicoins from user input.
# 2. Print how much you will get in all five currencies
#    mentioned above.

# Examples

# The greater-than symbol followed by a space ( > )
# represents the user input. Note that it's not part of the
# input.

# Be aware that the dictionary elements are unordered.

# Example 1:
# > 17
# I will get 50.66 RUB from the sale of 17.0 conicoins.
# I will get 13.94 ARS from the sale of 17.0 conicoins.
# I will get 2.89 HNL from the sale of 17.0 conicoins.
# I will get 33.36 AUD from the sale of 17.0 conicoins.
# I will get 3.54 MAD from the sale of 17.0 conicoins.

# 3.5
# I will get 10.43 RUB from the sale of 3.5 conicoins.
# I will get 2.87 ARS from the sale of 3.5 conicoins.
# I will get 0.6 HNL from the sale of 3.5 conicoins.
# I will get 6.87 AUD from the sale of 3.5 conicoins.
# I will get 0.73 MAD from the sale of 3.5 conicoins.

class CurrencyConverter:
    def __init__(self):
        self.message = "I will get {} {} from the sale of {} conicoins."
        self.currency = {"RUB": 2.98, "ARS": 0.82, "HNL": 0.17, "AUD": 1.9622, "MAD": 0.208}
        self.conicoins = 0


    def start(self):
        self.converter()
    def user(self):
        return float(input())

    def converter(self):
        self.conicoins = self.user()
        self.report()


    def report(self):
        for currency, price in self.currency.items():
            print(self.message.format(round(price * self.conicoins, 2), currency, self.conicoins))

def main():
    cur = CurrencyConverter()
    cur.start()


if __name__ == '__main__':
    main()