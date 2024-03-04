'''
 For a slightly different challenge, turn each line in the file into a Python dict.
This will require identifying each field with a unique column or key name. If
you’re not sure what each field in /etc/passwd does, you can give it an arbitrary name.
'''

import csv
import json

def csv_to_json2(file):
    with open(file, 'r') as csv_file, open('../passwords2.json', 'w') as json_file:
        r = csv.reader(csv_file, delimiter='\t')
        data = [{line[0]: line[1]} for line in r if line]

        json.dump(data, json_file)

if __name__ == "__main__":
    csv_to_json2('../passwords.csv')