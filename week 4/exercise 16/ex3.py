'''
 Write a function that takes any even number of arguments and returns a dict
based on them. The even-indexed arguments become the dict keys, while the
odd-numbered arguments become the dict values. Thus, calling the function
with the arguments ('a', 1, 'b', 2) will result in the dict {'a':1, 'b':2} being
returned.
'''

def make_dict(*args):
    output = {}
    temp = ''
    for arg in args:
        if not temp:
            temp = arg
        else:
            output[temp] = arg
            temp = ''
    
    return output

if __name__ == "__main__":
    print(make_dict('a', 1, 'b', 2, 'c', 3))