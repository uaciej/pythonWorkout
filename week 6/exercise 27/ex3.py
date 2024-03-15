'''
 Write a function, getitem, that takes a single argument and returns a function
f. The returned f can then be invoked on any data structure whose elements
can be selected via square brackets, and then returns that item. So if I invoke
f = getitem('a'), and if I have a dict d = {'a':1, 'b':2}, then f(d) will return
1. (This is very similar to operator.itemgetter, a very useful function in many
circumstances.)
'''

def getitem(key):
    def f(data_struct):
        return data_struct.get(key)
    return f

if __name__ == "__main__":
    f = getitem('a')
    d = {'a':1, 'b':2}
    print(f(d))  # Output: 1