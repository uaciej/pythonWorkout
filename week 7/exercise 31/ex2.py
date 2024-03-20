'''
Write a new function, funcfile, that will take two arguments—a filename and a
function. The output from the function should be a string, the result of invoking the function on each word in the text file. You can think of this as a generic
version of plfile, one that can return any string value
'''

def funcfile(filename, func):
    with open(filename) as f:
        return ' '.join(func(word) for line in f for word in line.split())



if __name__ == "__main__":
    print(funcfile('../assets/bruh.txt', lambda x: x + 'bruh'))