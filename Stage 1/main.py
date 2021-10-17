# Stage 1/6: Cryptocurrencies are the new black

#  Description
# Today we start our new project. It will be a simple currency
# converter. Every person sometimes needs to convert one
# currency to another. But we need to start easy, so for now, all
# you need to do is to print "Meet a conicoin!" Please, make sure
# that the output formatting of your program follows the example
# output formatting.

# Objectives
# Imagine that there is a cryptocurrency called conicoin ("coni" is
# just an anagram of the word "coin"). Greet conicoin as shown in
# the example below.

# Example
# Output:
# Meet a conicoin!

# write your code here!
class CurrencyConverter:

    def __init__(self):
        self.greeting_message = "Meet a conicoin!"

    def start(self):
        print(self.greeting_message)


def main():
    Cur = CurrencyConverter()
    Cur.start()


if __name__ == '__main__':
    main()