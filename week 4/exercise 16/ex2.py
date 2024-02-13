'''
 The dict.update method merges two dicts. Write a function that takes any
number of dicts and returns a dict that reflects the combination of all of them.
If the same key appears in more than one dict, then the most recently merged
dict’s value should appear in the output.
'''

def update_dict(*dic):
    for d in dic[1:]:
        dic[0].update(d)
    return dic[0]


if __name__ == "__main__":
    d1 = {'a':1, 'b':2, 'c':3}
    d2 = {'a':1, 'b':2, 'c':4}
    d3 = {'a':1, 'b':2, 'd':3}
    d4 = {'a':1, 'b':2, 'c':4}
    print(update_dict(d1, d2, d3, d4))