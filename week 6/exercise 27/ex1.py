'''
In this exercise, we’re going to create a password-generation function. Actually,
we’re going to create a factory for password-generation functions. That is, I might
need to generate a large number of passwords, all of which use the same set of characters. (You know how it is. Some applications require a mix of capital letters, lowercase
letters, numbers, and symbols; whereas others require that you only use letters; and
still others allow both letters and digits.) You’ll thus call the function create_password
_generator with a string. That string will return a function, which itself takes an integer
argument. Calling this function will return a password of the specified length, using
the string from which it was created
'''

import random

def create_password_generator(user_string):
    def password_generator(length):
        out = ''
        for _ in range(length):
            out += random.choice(user_string)
        return out
    return password_generator


if __name__  == '__main__':
    alpha_password = create_password_generator('abcdef')
    symbol_password = create_password_generator('!@#$%')
    print(alpha_password(5)) # efeaa
    print(alpha_password(10)) # cacdacbada
    print(symbol_password(5)) # %#@%@
    print(symbol_password(10))  # @!%%$%$%%#