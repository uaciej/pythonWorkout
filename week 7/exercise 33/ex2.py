'''
 Expand the transform_values exercise, taking two function arguments, rather
than just one. The first function argument will work as before, being applied to
the value and producing output. The second function argument takes two 
arguments, a key and a value, and determines whether there will be any output at
all. That is, the second function will return True or False and will allow us to
selectively create a key-value pair in the output dict.
'''


def transform_values(func1, func2, dic):
    return {key: func1(val) for key, val in dic.items() if func2(key,val)}



if __name__ == "__main__":
    dic = {k:v for k,v in zip('abcdefg', range(7))}
    
    def checker(a,b):
        return (a.isalpha() and b % 2 == 0)
    
    print(transform_values(lambda x: x**2, checker, dic))