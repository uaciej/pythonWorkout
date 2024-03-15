'''
Now that you’ve written a function to create passwords, write create_password_checker, which checks that a given password meets the IT staff’s acceptability criteria. 
In other words, create a function with four parameters: min_uppercase, min_lowercase, min_punctuation, and min_digits. 
These represent the minimum number of uppercase letters, lowercase letters, punctuations,
and digits for an acceptable password. The output from create_password_
checker is a function that takes a potential password (string) as its input and
returns a Boolean value indicating whether the string is an acceptable password.
'''
import string

def create_password_checker():
    params = {
        'min_uppercase': 1,
        'min_lowercase': 1,
        'min_punctuation': 1,
        'min_digits': 1,
    }
    def check(password):
        count = {'upper': 0, 'lower': 0, 'punct': 0, 'digit': 0}
        for char in password:
            if char.isupper():
                count['upper'] += 1
            elif char.islower():
                count['lower'] += 1
            elif char.isdigit():
                count['digit'] += 1
            elif char in string.punctuation:
                count['punct'] += 1
        if count['upper'] < params['min_uppercase'] or count ['lower'] < params['min_lowercase'] \
           or count['punct'] < params['min_punctuation'] or count['digit'] < params['min_digits']:
            return False
        return True
    return check



if __name__  == '__main__':
    my_checker = create_password_checker()
    print(my_checker("Abcde1!")) #True
    print(my_checker("abcde1!") )#False
    print(my_checker("ABCDE1!")) #False