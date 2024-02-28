'''
Extend this exercise by asking the user to enter a space-separated list of integers, indicating which fields should be written to the output CSV file. Also ask
the user which character should be used as a delimiter in the output file. Then
read from /etc/passwd, writing the user’s chosen fields, separated by the user’s
chosen delimiter.
'''

import csv

def passwd_to_csv(passwd_filename, csv_filename, user_info, user_delim):
    with open(passwd_filename, 'r') as passwd, open(csv_filename, 'w') as csvfile:
        o = csv.writer(csvfile, delimiter=user_delim)
        for line in passwd:
            if not line.startswith(('#', '\n')):
                words = line.split(':')
                o.writerow((words[int(i)]  for i in user_info))

if __name__  == "__main__":
    user_info = input("Wchich fields should be written to the output file?: ").split()
    user_delim = input("Which character should be used as a delimiter?: ")
    passwd_to_csv('../passwords.txt', '../passwords2.csv',  user_info, user_delim)