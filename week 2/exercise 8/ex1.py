'''
In this exercise, you’ll explore this idea by writing a function, strsort, that takes a
single string as its input and returns a string. The returned string should contain the
same characters as the input, except that its characters should be sorted in order, from
the lowest Unicode value to the highest Unicode value.
'''

def string_sort(a_string):
    return ''.join(sorted(a_string))


if __name__ == '__main__':
    print(string_sort('halapeno'))