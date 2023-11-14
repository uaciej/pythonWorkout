from decimal import *

def my_decimal_func():
    x = Decimal(input("Provide x: "))
    y = Decimal(input("Provide y: "))

    return(x + y)

if __name__ == "__main__":
    print(my_decimal_func())