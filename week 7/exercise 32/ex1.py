'''
For this exercise, first create a dict of any size, in which the keys are unique and the
values are also unique. (A key may appear as a value, or vice versa.) Here’s an example:
d = {'a':1, 'b':2, 'c':3}
Turn the dict inside out, such that the keys and the values are reversed.
'''

def dic_turner(dic):
    return {value: key for key, value in dic.items()}




if __name__ == "__main__":
    dic = {letter : num for letter, num in zip('abcdefghi',range(9))}
    print(dic_turner(dic))