'''
 Create a dict whose keys are currency names and whose values are the price of
that currency in U.S. dollars. Write a function that asks the user what currency
they use, then returns the dict from the previous exercise as before, but with its
prices converted into the requested currency. 
'''
from ex3 import books_dic

currency_prices = {
    "Euro": 1.11,
    "British Pound": 1.33,
    "Japanese Yen": 0.0091,
    "Canadian Dollar": 0.79,
    "Australian Dollar": 0.73,
    "Swiss Franc": 1.10,
    "Chinese Yuan": 0.16
}

def convert_prices(currency):
    try:
        ratio = currency_prices[currency]
    except:
        return "Not a valid currency"
    
    return {k : {'first_name': v['first_name'], 'last_name' : v['last_name'], 'price' : "{:.2f}".format(v['price'] / ratio)} 
            for k,v in books_dic.items()}


if __name__ == "__main__":
    print(convert_prices(input("What type of currency do you use?: ")))