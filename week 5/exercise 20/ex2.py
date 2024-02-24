'''
Ask the user to enter the name of a text file and then (on one line, separated by
spaces) words whose frequencies should be counted in that file. Count how
many times those words appear in a dict, using the user-entered words as the
keys and the counts as the values.
'''

def  count_words(file, word_list):
    count = {word : 0 for word in word_list}
    with open(file, 'r') as f:
        for line in f:
           words_in_line = line.split()
           for word in words_in_line:
               word = word.lower()
               if word in word_list:
                   count[word] += 1
    return count


if __name__ == "__main__":
    file = input("What file should be opened: ")
    words = input("Enter list of words to count frequency: ").split()
    print(count_words(file, words))