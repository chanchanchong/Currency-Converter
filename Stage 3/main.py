# Stage 3/6: More interaction

# Description
# We are going to make our program more complex. As you remember,
# the conicoin rate was fixed in the previous stage. But in the real world,
# things are different. It's time to write a program that takes your
# conicoins and an up-to-date conicoin exchange rate, then counts how
# many dollars you would get, and print the result.

# Objectives
#   1. Get the number of conicoins from the user input.
#   2. Get the exchange rate from the user input.
#   3. Calculate and print hte result.

# Example

# The greater-than symbol followed by a space ( > ) represents the user
# input. Note that it's not part of the input.

# Example 1:
# Please, enter the number of conicoins you have: > 13
# Please, enter the exchange rate: > 2
# The total amount of dollars: 26

# Example 2:
# Please, enter the number of conicoins you have: > 128
# Please, enter the exchange rate: > 3.21
# The total amount of dollars: 410.88

class CurrencyConverter:
    def __init__(self):
        self.exchange = 0
        self.dollars = 0
        self.coins = 0
        self.conicoin_question = "Please, enter the number of conicoins you have: "
        self.exchange_question = "Please, enter the exchange rate: "
        self.amount_message = "The total amount of dollars:"

    def start(self):
        self.converter()

    def user(self, question):
        return input(question)

    def converter(self):
        self.coins = int(self.user(self.conicoin_question))
        self.exchange = float(self.user(self.exchange_question))
        self.dollars = self.coins * self.exchange
        print(self.amount_message, round(self.dollars) if self.dollars % 1 == 0 else round(self.dollars, 2))


def main():
    cur = CurrencyConverter()
    cur.start()


if __name__ == '__main__':
    main()