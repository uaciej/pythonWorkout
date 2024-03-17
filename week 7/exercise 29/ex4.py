'''
Define a list of five dicts. Each dict will have two key-value pairs, name and age,
containing a person’s name and age (in years). Use a list comprehension to
produce a list of dicts in which each dict contains three key-value pairs:
the original name, the original age, and a third age_in_months key, containing the person’s age in months. 
However, the output should exclude any of the input dicts representing people over 20 years of age. 
'''


def change_dics(lst_of_dics):
    return [{"name": dic['name'], "age": dic['age'], "age_in_months": dic['age'] * 12} for dic in lst_of_dics if dic['age'] < 21]



if __name__ == "__main__":
    people = [
    {"name": "Alice", "age": 10},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 15},
    {"name": "Diana", "age": 18},
    {"name": "Eve", "age": 20}
]
    print(change_dics(people))