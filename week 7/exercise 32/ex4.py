'''
Find a configuration file in which the lines look like “name=value.” Use a dict
comprehension to read from the file, turning each line into a key-value pair.
'''

def file_to_dic(file):
    with open(file) as f:
        return {key : val for line in f for key, val in [line.rstrip('\n').split('=')]}


if __name__ == "__main__":
    print(file_to_dic('../assets/config.cfg'))