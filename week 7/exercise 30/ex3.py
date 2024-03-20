'''
Define a dict that represents the children and grandchildren in a family. (See
figure 7.1 for a graphic representation.) Each key will be a child’s name, and
each value will be a list of strings representing their children (i.e., the family’s
grandchildren). Thus the dict {'A':['B', 'C', 'D'], 'E':['F', 'G']} means
that A and E are siblings; A’s children are B, C, and D; and E’s children are F and
G. Use a list comprehension to create a list of the grandchildren’s names.
'''

def grandchildrens_names(dic):
    return [grand for parent in dic for grand in dic[parent]]



if __name__ == "__main__":
    family = {
    'Alice': ['Bob', 'Charlie', 'David'],
    'Eve': ['Frank', 'Grace']
    }
    print(grandchildrens_names(family))