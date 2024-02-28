'''
 Write a function that writes a dict to a CSV file. Each line in the CSV file should
contain three fields: (1) the key, which we’ll assume to be a string, (2) the value,
and (3) the type of the value (e.g., str or int).
'''
import csv

def dict_to_csv(dic):
    with open('../dicToCSV.csv', 'w') as f:
        writer = csv.writer(f)
        for key, val in dic.items():
            writer.writerow((key, val, type(val).__name__))



if __name__ == "__main__":
    dic = {'name': 'John', 'age': 25, 'city': 'New York'}
    dict_to_csv(dic)