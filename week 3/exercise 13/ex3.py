'''
Define a list of tuples, in which each tuple contains the name, length (in minutes), and director of the movies nominated for best picture Oscar awards last
year. Ask the user whether they want to sort the list by title, length, or director’s
name, and then present the list sorted by the user’s choice of axis.
'''
import operator
import sys

MOVIES = [
    ('Nomadland', 107, 'Chloé Zhao'),
    ('The Trial of the Chicago 7', 129, 'Aaron Sorkin'),
    ('Minari', 115, 'Lee Isaac Chung'),
    ('Promising Young Woman', 113, 'Emerald Fennell'),
    ('Judas and the Black Messiah', 126, 'Shaka King'),
    ('Mank', 131, 'David Fincher'),
    ('Sound of Metal', 120, 'Darius Marder'),
    ('The Father', 97, 'Florian Zeller'),
    ('News of the World', 118, 'Paul Greengrass'),
    ('Borat Subsequent Moviefilm', 96, 'Jason Woliner')
]

def format_sort_records(tuple_list):
    output = []
    x = input('What should we sort the list by? (n)ame, (l)ength, (d)irector: ')
    template = "{0:30} directed by {2:20} - Length: {1} minutes"
    match x:
        case 'name' | 'n':
            for movie in sorted(tuple_list, key=operator.itemgetter(0)): 
                output.append(template.format(*movie))
        case 'length' | 'l':
            for movie in sorted(tuple_list, key=operator.itemgetter(1)): 
                output.append(template.format(*movie))
        case 'director' | 'd':
            for movie in sorted(tuple_list, key=operator.itemgetter(2)): 
                output.append(template.format(*movie))
        case _:
            print("Invalid entry.")
            sys.exit

    return output

if __name__ == "__main__":
    print('\n'.join(format_sort_records(MOVIES)))