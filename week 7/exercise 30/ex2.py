'''
Write a version of the flatten function mentioned earlier called flatten_odd
_ints. It’ll do the same thing as flatten, but the output will only contain odd
integers. Inputs that are neither odd nor integers should be excluded. Inputs
containing strings that could be converted to integers should be converted;
other strings should be excluded.
'''

def flatten_odd_ints(lst_of_lsts):
    return [int(elem) for lst in lst_of_lsts for elem in lst if int(elem) % 2 != 0]



if __name__ == "__main__":
    print(flatten_odd_ints([[1, 2], [3, 4], ['5', '6']]))