'''
 Convert /etc/passwd from a CSV-style file into a JSON-formatted file. The
JSON file will contain the equivalent of a list of Python tuples, with each tuple
representing one line from the file.
'''
import csv
import json

def csv_to_json(file):
    with open(file, 'r') as csv_file, open('../passwords.json', 'w') as json_file:
        r = csv.reader(csv_file, delimiter='\t')
        data = [tuple(line) for line in r if line]

        json.dump(data, json_file)

if __name__ == "__main__":
    csv_to_json('../passwords.csv')