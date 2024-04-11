'''
 Many programs’ functionality is modified via configuration files, which are often
set using name-value pairs. That is, each line of the file contains text in the form
of name=value, where the = sign separates the name from the value. I’ve 
prepared one such sample config file at http://mng.bz/rryD. Download this file,
and then use a dict comprehension to read its contents from disk, turning it into
a dict describing a user’s preferences. Note that all of the values will be strings.
'''

def read_dic(file):
    with open(file) as f:
        return {key: val for line in f for key, val in [line.rstrip('\n').split('=')]}
    

if __name__ == "__main__":
    print(read_dic('../assets/config.txt'))