'''
Create a dict whose keys are filenames and whose values are the lengths of the
files. The input can be a list of files from os.listdir (http://mng.bz/YreB) or
glob.glob (http://mng.bz/044N)
'''
import os


def filename_dic(path):
    return {file : len(file) for file in os.listdir(path)}


if __name__ == "__main__":
    print(filename_dic('../../week 5/'))