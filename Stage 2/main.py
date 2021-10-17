# Stage 2/6: Talking numbers

# Description

# Holy moly! Suddenly you remember that back in 2008 you
# purchased several conicoins! Are you officially rich? Well, we
# need to find it out. You need to write a program that shows
# how much you can get after selling your conicoins. One
# conicoin is 100 dollars. Read your amount of the conicoins as
# the input, convert them into dollars, and output the result.
# Also, express your joy, it's important.

# Objective

# Find out if you are rich.
#   1. Input the amount of your conicoins.
#   2. Calculate the number of dollars you receive after the
#      conversion. 1 conicoin = 100 dollars, print the result as
#   3. Wooho! You are rich!

# Example

# The greater-than symbol followed by a space ( > ) represents
# the user input. Note that it's not part of the input.

# Output:

# 42
# I have 42 conicoins.
# 42 conicoins cost 4200 dollars.
# I am rich! Yippee!

# write your code here!
class CurrencyConverter:

    def __init__(self):
        self.dollars = 0
        self.greeting_message = "Meet a conicoin!"
        self.coins = 0
        self.message = "I have {coins} conicoins.\n{coins} conicoins cost {dollars} dollars.\nI am rich! Yippee!"

    def start(self):
        self.converter()

    def user(self):
        return int(input())

    def converter(self):
        self.coins = self.user()
        self.dollars = self.coins * 100
        print(self.message.format(coins=self.coins, dollars=self.dollars))

def main():
    Cur = CurrencyConverter()
    Cur.start()


if __name__ == '__main__':
    main()

