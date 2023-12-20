'''
 Don’t write one function that finds the largest element of a string, another that
does the same for a list, and a third that does the same for a tuple. Write just
one function that works on all of them.
'''

def largest_elem(iterable):
    return max(iterable)


if __name__ == "__main__":
    # Test cases
    print (largest_elem("abc5"))
    print (largest_elem([1, 2, 3, 4]))
    print (largest_elem((1, 2, 3, 4)))
    