'''
Ask the user for a directory name. Show all of the files in the directory, as well
as how long ago the directory was modified. You will probably want to use a combination of os.stat and the Arrow package on PyPI (http://mng.bz/nPPK)
to do this easily
'''

import arrow
import os

def get_files(directory):
    output = {}
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            output[filename] = arrow.get(os.stat(filepath).st_mtime).format('YYYY-MM-DD HH:mm:ss')
    for key, val in output.items():
        print(f"{key} : {val}")

if __name__ == '__main__':
    dirname = input("Enter a directory name: ")
    get_files(dirname)
