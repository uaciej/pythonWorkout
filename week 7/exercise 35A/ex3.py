'''
 Create a dict based on the config file, as in the previous exercise, but this time,
all of the values should be integers. This means that you’ll need to filter out
(and ignore) those values that can’t be turned into integers
'''

def read_dic(file):
    with open(file) as f:
        return {key: int(val) for line in f for key, val in [line.rstrip('\n').split('=')] if val.isdigit()}
    

if __name__ == "__main__":
    print(read_dic('../assets/config.txt'))