'''
This exercise, the result of which you’ll use in the next one, asks that you create a
dict whose keys are the (lowercase) letters of the English alphabet, and whose values
are the numbers ranging from 1 to 26. And yes, you could simply type {'a':1, 'b':2,
'c':3} and so forth, but I’d like you to do this with a dict comprehension
'''
import string


let_num_dic = {k:v for k,v in zip(string.ascii_letters, range(1,27))}

print(let_num_dic)