'''
 In this exercise, we’re going to create a slight variation on map, one that applies
a function to each of the values of a dict. The result of invoking this function,
transform_values, is a new dict whose keys are the same as the input dict, but whose
values have been transformed by the function.
'''

def transform_values(func, dic):
    return {key: func(val) for key, val in dic.items()}


if __name__ == "__main__":
    dic = {k:v for k,v in zip('abcdefg', range(7))}
    print(transform_values(lambda x: x**2, dic))