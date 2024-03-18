'''
Write a function that takes a
list of lists (just one element deep) and returns a flat, one-dimensional version of the
list.
'''


def flatten(lst_of_lsts):
    return [elem for lst in lst_of_lsts for elem in lst]


if __name__ == "__main__":
    print(flatten([[1, 2], [3, 4]]))