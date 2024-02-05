'''
If you find tuples annoying because they use numeric indexes, you’re not alone!
Reimplement this exercise using namedtuple objects (http://mng.bz/gyWl),
defined in the collections module. Many people like to use named tuples
because they give the right balance between readability and efficiency
'''

from collections import namedtuple

Person = namedtuple('Person', ['name', 'lastname', 'travel_time'])

trump = Person('Donald', 'Trump', 7.85)
putin = Person('Vladimir', 'Putin', 3.626)
xi = Person('Jinping', 'Xi', 10.603)

PEOPLE =  [trump, putin, xi]

def format_sort_records(tuple_list):
    output = []
    template = "{lastname:10} {name:10} {travel_time:5.2f}"
    for person in sorted(tuple_list, key=lambda x: (x.lastname, x.name)):
        output.append(template.format(**person._asdict()))
    return output


if __name__ == "__main__":
    print('\n'.join(format_sort_records(PEOPLE)))