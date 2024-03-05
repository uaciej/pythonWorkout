'''
Ask the user for the name of a directory. Iterate through each file in that directory (ignoring subdirectories), getting (via os.stat) the size of the file and
when it was last modified. Create a JSON-formatted file on disk listing each filename, size, and modification timestamp. Then read the file back in, and identify
which files were modified most and least recently, and which files are largest and smallest, in that directory. 
'''

import arrow
import os
import json

def get_files_data(directory):
    output = []
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            this_file_data = {
            'filename' : filename,
            'size' : os.stat(filepath).st_size,
            'last_modified' : arrow.get(os.stat(filepath).st_mtime).format('YYYY-MM-DD HH:mm:ss')
            }
            output.append(this_file_data)
    with open('../filedata.json', 'w') as json_file:
        json.dump(output, json_file)

def read_files_data(file):
    with open(file) as f:
        data = json.load(f)
        data_sorted_by_size = sorted(data, key=lambda x: x['size'])
        data_sorted_by_timestamp = sorted(data, key=lambda x: x['last_modified'])
        output = {
            "Biggest file" : data_sorted_by_size[-1]['filename'],
            "Smallest file" : data_sorted_by_size[0]['filename'], 
            "Most recently modified file" : data_sorted_by_timestamp[-1]['filename'],
            "Least recently modified file" : data_sorted_by_timestamp[0]['filename']
            }
        for k, v in output.items():
            print(f"{k} : {v}")  

if __name__ == '__main__':
    dirname = input("Enter a directory name: ")
    get_files_data(dirname)
    read_files_data('../filedata.json')