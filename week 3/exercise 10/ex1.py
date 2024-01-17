'''
Sum the elements of a list—regardless of whether those elements are integers, floats, strings,
or even lists
'''


def mysum(*items):
    if not items:
        return items
    output = items[0]
    for item in items[1:]:
        output += item
    return output


if __name__ == "__main__":
    print("1,2,3 = ", mysum(1,2,3))
    print("('a','b','c')('d','e','f') = ", mysum(('a','b','c'),('d','e','f')))
    print("[1,2,3][4,5,6] = ", mysum([1,2,3],[4,5,6]))