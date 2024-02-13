'''
 Write a function , dict_partition, that takes one dict (d) and a function (f) as
arguments. dict_partition will return two dicts, each containing key-value
pairs from d. The decision regarding where to put each of the key-value pairs
will be made according to the output from f, which will be run on each keyvalue pair in d. If f returns True, then the key-value pair will be put in the first
output dict. If f returns False, then the key-value pair will be put in the second
output dict. 
'''

def dict_partition(dic, func):
    d1 = {}
    d2 = {}
    for k, v in dic.items():
        if func(k, v):
            d1[k] = v
        else:
            d2[k] = v

    return d1, d2


if __name__ == "__main__":
    dic = {
        'a' : 1,
        'b' : 2,
        'c' : 3,
        'd' : 4,
        'e' : 5,
        'f' : 6,
           }
    func = lambda x,y: x.isalpha() and y % 2 == 0
    print(dict_partition(dic, func))