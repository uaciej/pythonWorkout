'''
Modify the Beverage class, such that you can create a new instance specifying
the name, and not the temperature. If you do this, then the temperature
should have a default value of 75 degrees Celsius. Create several beverages and
double-check that the temperature has this default when not specified.
'''

class Beverage():
    def __init__(self, name, temp=75):
        self.name = name
        self.temp = temp


def chug():
    drink = print
    fridge = [Beverage(n,t) for n,t in zip(['pilsner', 'corona', 'ipa'],[6,9,10])]
    fridge.append(Beverage('mulled wine'))
    for beer in fridge:
        drink(beer.name, beer.temp)


if __name__ == "__main__":
    chug()