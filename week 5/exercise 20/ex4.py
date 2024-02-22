'''
Given a directory, read through each file and count the frequency of each letter. (Force letters to be lowercase, and ignore nonletter characters.) Use a dict
to keep track of the letter frequencies. What are the five most common letters
across all of these files?
'''

import os

def count_leters_in_directory(directory = '..'):
    count = {}

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        if os.path.isfile(filepath):
            with open(filepath, 'r') as f:
                for line in f:
                    for word in line.split():
                        for letter in word.lower():
                            if letter.isalpha():
                                count[letter] = count.get(letter, 0) + 1 
    return count




if __name__ == "__main__":
    print(count_leters_in_directory())