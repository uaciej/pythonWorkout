'''
Write a function, apply_to_each, that takes two arguments: a function that takes
a single argument, and an iterable. Return a list whose values are the result of
applying the function to each element in the iterable. (If this sounds familiar, it
might be—this is an implementation of the classic map function, still available in
Python. You can find a description of map in chapter 7.)
'''

def apply_to_each(func, lst):
    out = []
    for elem in lst:
        out.append(func(elem))
    return out



if __name__  == '__main__':
    print(apply_to_each(lambda x: int(x) * 2, '12345'))