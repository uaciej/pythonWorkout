'''
 Create a new LogFile class that expects to be initialized with a filename.
Inside of __init__, open the file for writing and assign it to an attribute,
file, that sits on the instance. Check that it’s possible to write to the file via
the file attribute.
'''

class LogFile():
    def __init__(self, file):
        self.file = open(file, 'w')


if __name__ == "__main__":
    loggedFile = LogFile('../assets/text.txt')
    for _ in range(69):
        loggedFile.file.writelines('Bruh\n')
        