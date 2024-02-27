'''
In this exercise, write two functions. find_longest_word takes a filename as an
argument and returns the longest word found in the file. The second function, find-
_all_longest_words, takes a directory name and returns a dict in which the keys are
filenames and the values are the longest words from each file
'''
import os

def find_longest_word(file):
    with open(file, 'r') as f:
        longest_word = ''
        for line in f:
            for word in line.split():
                if len(word) > len(longest_word):
                    longest_word = word
    return longest_word


def find_all_longest_words(directory):
    output = {}
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            output[filename] = find_longest_word(filepath)

    for key, val in output.items():
        print(f"{key}: {val}")


if __name__ == "__main__":
    find_all_longest_words('..')