'''
 Write a copyfile function that takes one mandatory argument—the name of
an input file—and any number of additional arguments: the names of files to
which the input should be copied. Calling copyfile('myfile.txt', 'copy1
.txt', 'copy2.txt', 'copy3.txt') will create three copies of myfile.txt:
one each in copy1.txt, copy2.txt, and copy3.txt
'''

import shutil

def copyfile(input_file, *output_files):
    for output_file in output_files:
        output_file_path = '../assets/' + output_file
        shutil.copy(input_file, output_file_path)    



if __name__ == "__main__":
    copyfile('../assets/text.txt', 'text2.txt', 'text3.txt')