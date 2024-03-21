'''
 Assume that you have a list of dicts, in which each dict contains two name-value
pairs: name and hobbies, where name is the person’s name and hobbies is a set
of strings representing the person’s hobbies. What are the three most popular
hobbies among the people listed in the dicts?
'''
from collections import Counter 


def popular(lst):
    return Counter([val for s in [elem[hobby] for elem in lst for hobby in elem if hobby == 'hobbies'] for val in s]).most_common(3)



if __name__ == "__main__":
    list_of_dicts = [
    {'name': 'Jeff', 'hobbies': {'reading', 'hiking', 'exploiting the working class', 'mass genocide', 'tax fraud'}},
    {'name': 'Alice', 'hobbies': {'painting', 'gardening', 'mass genocide', 'tax fraud'}},
    {'name': 'Bill', 'hobbies': {'playing guitar', 'traveling', 'exploiting the working class', 'tax fraud'}},
    {'name': 'Emma', 'hobbies': {'cooking', 'photography', 'tax fraud'}}
]
    print(popular(list_of_dicts))