'''
Use a nested list comprehension to transform a list of dicts into a list of two 
element (name-value) tuples, each of which represents one of the name-value
pairs in one of the dicts. If more than one dict has the same name-value pair,
then the tuple should appear twice
'''


def dic_to_tup(lst):
    return [(key, elem[key]) for elem in lst for key in elem]



if __name__ == "__main__":
    lst = [
    {'name': 'John', 'age': 30, 'city': 'New York'},
    {'name': 'Alice', 'age': 25, 'city': 'San Francisco'},
    {'name': 'Bob', 'age': 35, 'city': 'Los Angeles'},
    {'name': 'Emma', 'age': 28, 'city': 'Chicago'}
]
    print(dic_to_tup(lst))