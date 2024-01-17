'''
Write a function that takes a list of dicts and returns a single dict that combines
all of the keys and values. If a key appears in more than one argument, the
value should be a list containing all of the values from the arguments. 
'''

def sum_dict(*items):
    out = {}
    for dic in items:
        for k, v in dic.items():
            if k not in out:
                out[k] = [v]
            else:
                out[k].append(v)
    return out


if __name__ == "__main__":
    d1 = {"a": 1, "b": 2}
    d2 = {"c": 3, "d": 4}
    d3 = {"c": 5, "e": 6}
    print(sum_dict(d1, d2, d3))