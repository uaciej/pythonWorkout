'''
 Write a “factorial” function that takes any number of numeric arguments and
returns the result of multiplying them all by one another
'''

def factorial(*args):
    out = 1
    for arg in args:
        out = out * arg
    return out

if __name__ == "__main__":
    print(factorial(1, 2, 3, 4, 5, 6))