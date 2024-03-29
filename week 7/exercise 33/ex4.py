'''
 Write a function that takes a directory name (i.e., a string) as an argument. The
function should return a dict in which the keys are the names of files in that
directory, and the values are the file sizes. You can use os.listdir or glob
.glob to get the files, but because only regular files have sizes, you’ll want to 
filter the results using methods from os.path. To determine the file size, you can
use os.stat or (if you prefer) just check the length of the string resulting from
reading the file. 
'''
import os

def dir_to_dic(dir):
    opj = os.path.join
    return {file : os.stat(opj(dir, file)).st_size for file in os.listdir(dir) if os.path.isfile(opj(dir, file))}



if __name__ == "__main__":
    print(dir_to_dic('../assets'))