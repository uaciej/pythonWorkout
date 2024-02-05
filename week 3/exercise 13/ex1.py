'''
For this exercise, write a Python function, format_sort_records, that takes the
PEOPLE list and returns a formatted string that looks like the following:

Trump Donald 7.85
Putin Vladimir 3.63
Xi Jinping 10.60

Notice that the last name is printed before the first name (taking into account that
Chinese names are generally shown that way), followed by a decimal-aligned indication
of how long it’ll take for each leader to arrive in London. Each name should be printed
in a 10-character field, and the time should be printed in a 5-character field, with one
space character of padding between each of the columns. Travel time should display
only two digits after the decimal point, which means that even though the input for Xi
Jinping’s flight is 10.603 hours, the value displayed should be 10.60

'''
import operator

PEOPLE =  [('Donald', 'Trump', 7.85),
('Vladimir', 'Putin', 3.626),
('Jinping', 'Xi', 10.603)]

def format_sort_records(tuple_list):
    output = []
    template = '{1:10} {0:10} {2:5.2f}'
    for person in sorted(tuple_list, key=operator.itemgetter(1, 0)): 
        output.append(template.format(*person))
    return output


if __name__ == "__main__":
    print('\n'.join(format_sort_records(PEOPLE)))