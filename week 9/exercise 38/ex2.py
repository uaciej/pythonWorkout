'''
Write a Beverage class whose instances will represent beverages. Each beverage
should have two attributes: a name (describing the beverage) and a temperature.
Create several beverages and check that their names and temperatures are all
handled correctly
'''

class Beverage():
    def __init__(self, name, temp):
        self.name = name
        self.temp = temp


def chug():
    drink = print
    fridge = [Beverage(n,t) for n,t in zip(['pilsner', 'corona', 'ipa'],[6,9,10])]
    for beer in fridge:
        drink(beer.name, beer.temp)


if __name__ == "__main__":
    chug()