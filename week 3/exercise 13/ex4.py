'''
Extend this exercise by allowing the user to sort by two or three of these fields,
not just one of them. The user can specify the fields by entering them separated
by commas; you can use str.split to turn them into a list. 
'''

import operator
import sys

MOVIES = [
    ('Nomadland', 107, 'Chloé Zhao'),
    ('The Trial of the Chicago 7', 129, 'Aaron Sorkin'),
    ('Minari', 115, 'Lee Isaac Chung'),
    ('Promising Young Woman', 115, 'Emerald Fennell'),
    ('Judas and the Black Messiah', 126, 'Shaka King'),
    ('Mank', 131, 'David Fincher'),
    ('Sound of Metal', 120, 'Darius Marder'),
    ('The Father', 97, 'Florian Zeller'),
    ('News of the World', 118, 'Paul Greengrass'),
    ('Borat Subsequent Moviefilm', 96, 'Jason Woliner')
]

def format_sort_records(tuple_list):
    output = []
    x = input('What should we sort the list by? (n)ame, (l)ength, (d)irector: ').split()
    template = "{0:30} directed by {2:20} - Length: {1} minutes"
    x = [0 if item in ('name', 'n') else
     1 if item in ('length', 'l') else
     2 if item in ('director', 'd') else
     item for item in x]
    try:
        for movie in sorted(tuple_list, key=operator.itemgetter(*x)): 
            output.append(template.format(*movie))
    except:
        print("Invalid entry.")
        sys.exit

    return output

if __name__ == "__main__":
    print('\n'.join(format_sort_records(MOVIES)))