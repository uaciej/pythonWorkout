'''
As in the exercise, take a list of integers and turn them into strings. However,
you’ll only want to produce strings for integers between 0 and 10. Doing this
will require understanding the if statement in list comprehensions as well.
'''

def nums_to_strings(int_range):
    return [str(num) for num in int_range if num in range(11)]


if  __name__ == '__main__':
    print(nums_to_strings(range(-10,15)))