'''
Redo this previous exercise, but replace each grandchild’s name (currently a string) with
a dict. Each dict will contain two name-value pairs, name and age. Produce a list
of the grandchildren’s names, sorted by age, from eldest to youngest
'''
import operator

def grandchildrens_names(dic):
    return [child['name'] for child in sorted([grand for parent in dic for grand in dic[parent]], key=operator.itemgetter('age'), reverse=True)]



if __name__ == "__main__":
    family = {
    'Alice': [{'name': 'Bob', 'age': 10}, {'name': 'Charlie', 'age': 8}, {'name': 'David', 'age': 6}],
    'Eve': [{'name': 'Frank', 'age': 7}, {'name': 'Grace', 'age': 5}]
    }
    print(grandchildrens_names(family))