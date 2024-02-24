'''
Create a dict in which the keys are the names of files on your system and the values are the sizes of those files. To calculate the size, you can use os.stat
(http://mng.bz/dyyo).
'''
import os


def file_sizes(directory = '..'):
    count = {}

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        if os.path.isfile(filepath):
            size = os.stat(filepath).st_size
            count[filename] = size

    return count




if __name__ == "__main__":
    print(file_sizes())