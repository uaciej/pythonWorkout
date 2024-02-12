'''
Write a function, dictdiff, that takes two dicts as arguments. The function returns
a new dict that expresses the difference between the two dicts.
 If there are no differences between the dicts, dictdiff returns an empty dict. For
each key-value pair that differs, the return value of dictdiff will have a key-value pair
in which the value is a list containing the values from the two different dicts. If one of
the dicts doesn’t contain that key, it should contain None. The following provides some
examples
'''

def dictdiff(d1, d2):
    output = {}
    all_keys = d1.keys() | d2.keys()

    for key in all_keys:
        if d1.get(key) != d2.get(key):
            output[key] = [d1.get(key), d2.get(key)]
    
    return output
    

if __name__ == "__main__":
    d1 = {'a':1, 'b':2, 'c':3}
    d2 = {'a':1, 'b':2, 'c':4}
    print(dictdiff(d1, d2))
    d3 = {'a':1, 'b':2, 'd':3}
    d4 = {'a':1, 'b':2, 'c':4}
    print(dictdiff(d3, d4)) 