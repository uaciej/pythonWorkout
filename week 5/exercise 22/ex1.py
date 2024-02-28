'''
For this exercise, create a function, passwd_to_csv, that takes two filenames as
arguments: the first is a passwd-style file to read from, and the second is the name of a
file in which to write the output.
 The new file’s contents are the username (index 0) and the user ID (index 2).
Note that a record may contain a comment, in which case it will not have anything at
index 2; you should take that into consideration when writing the file. The output file
should use TAB characters to separate the elements
'''

import csv

def passwd_to_csv(passwd_filename, csv_filename):
    with open(passwd_filename, 'r') as passwd, open(csv_filename, 'w') as csvfile:
        o = csv.writer(csvfile, delimiter='\t')
        for line in passwd:
            if not line.startswith(('#', '\n')):
                words = line.split(':')
                o.writerow((words[0], words[2]))

if __name__  == "__main__":
    passwd_to_csv('../passwords.txt', '../passwords.csv')