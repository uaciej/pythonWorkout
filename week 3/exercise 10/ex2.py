'''
Write a function, mysum_bigger_than, that works the same as mysum, except that
it takes a first argument that precedes *args. That argument indicates the
threshold for including an argument in the sum. Thus, calling mysum_bigger
_than(10, 5, 20, 30, 6) would return 50—because 5 and 6 aren’t greater than
10. This function should similarly work with any type and assumes that all of the
arguments are of the same type. Note that > and < work on many different types
in Python, not just on numbers; with strings, lists, and tuples, it refers to their
sort order.
'''

def mysum_bigger_than(threshold, *items):
    if not items:
        return items
    output_type = type(items[0])
    output = output_type()
    for item in items[1:]:
        if item > threshold:
            output += item
        
    return output

if __name__ == "__main__":
    print("10, 5, 20, 30, 6 = ", mysum_bigger_than(10, 5, 20, 30, 6))
    print("'c','abc','def','ghi' = ", mysum_bigger_than('c','abc','def','ghi'))
    print("('b','c','d'),('a','b','c'),('d','e','f') = ", mysum_bigger_than(('b','c','d'),('a','b','c'),('d','e','f')))
    print("[2,4],[1,2,3],[4,5,6] = ", mysum_bigger_than([2,4],[1,2,3],[4,5,6]))